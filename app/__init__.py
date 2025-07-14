from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import MySQLDatabase, Model, CharField, TextField, DateTimeField
from playhouse.shortcuts import model_to_dict
import datetime
import os
from data import WORK_EXPERIENCE, EDUCATION, PROJECTS, TECH_SKILLS, HOBBIES, TRAVEL_LOCATIONS

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev_key")

# Database configuration - only initialize if all required variables are present
db_config = {
    'database': os.getenv("MYSQL_DATABASE"),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': os.getenv("MYSQL_HOST", "localhost"),
    'port': 3306,
}

# Check if all required database variables are present
db_enabled = all([
    db_config['database'],
    db_config['user'],
    db_config['password'],
    db_config['host']
])

if db_enabled:
    mydb = MySQLDatabase(**db_config)
    print(mydb)   # this is what produces the line the assignment wants
    
    class TimelinePost(Model):
        name = CharField()
        email = CharField()
        content = TextField()
        created_at = DateTimeField(default=datetime.datetime.now)

        class Meta:
            database = mydb

    # Initialize database connection and create tables
    try:
        mydb.connect()
        mydb.create_tables([TimelinePost])
        print("Database connected and tables created successfully")
    except Exception as e:
        print(f"Database connection failed: {e}")
        db_enabled = False
else:
    print("Database configuration incomplete - timeline features will be disabled")
    mydb = None
    TimelinePost = None

PAGES = [
    {"endpoint": "home", "name": "Home", "icon": "fas fa-home"},
    {"endpoint": "about", "name": "About", "icon": "fas fa-user"},
    {"endpoint": "projects", "name": "Projects", "icon": "fas fa-rocket"},
    {"endpoint": "hobbies", "name": "Hobbies", "icon": "fas fa-heart"},
    {"endpoint": "travel", "name": "Travel", "icon": "fas fa-map-marked-alt"},
    {"endpoint": "timeline", "name": "Timeline", "icon": "fas fa-clock"},
]

def render(page, **ctx):
    return render_template(
        f"{page}.html",
        title=ctx.pop("title", page.title()),
        pages=PAGES,
        active=page,
        **ctx
    )

@app.route("/")
def home():
    return render("home", title="Home", tech=TECH_SKILLS, projects=PROJECTS)

@app.route("/about")
def about():
    return render("about", title="About", work=WORK_EXPERIENCE, edu=EDUCATION)

@app.route("/projects")
def projects():
    return render("projects", title="Projects", projects=PROJECTS)

@app.route("/hobbies")
def hobbies():
    return render("hobbies", title="Hobbies", hobbies=HOBBIES)

@app.route("/travel")
def travel():
    return render("travel", title="Travel Map", locations=TRAVEL_LOCATIONS)

@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    if not db_enabled or not TimelinePost:
        return {'error': 'Database not configured'}, 500
    
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    if not db_enabled or not TimelinePost:
        return {'timeline_posts': []}
    
    return {
        'timeline_posts': [
            model_to_dict(p) 
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    if not db_enabled or not TimelinePost:
        return {'error': 'Database not configured'}, 500
    
    try:
        deleted = TimelinePost.delete_by_id(post_id)
        return {'deleted': bool(deleted)}
    except:
        return {'deleted': False}
