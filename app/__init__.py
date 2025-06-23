from flask import Flask, render_template
from dotenv import load_dotenv
import os
from data import WORK_EXPERIENCE, EDUCATION, PROJECTS, TECH_SKILLS, HOBBIES, TRAVEL_LOCATIONS

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev_key")

PAGES = [
    {"endpoint": "home", "name": "Home", "icon": "fas fa-home"},
    {"endpoint": "about", "name": "About", "icon": "fas fa-user"},
    {"endpoint": "projects", "name": "Projects", "icon": "fas fa-rocket"},
    {"endpoint": "hobbies", "name": "Hobbies", "icon": "fas fa-heart"},
    {"endpoint": "travel", "name": "Travel", "icon": "fas fa-map-marked-alt"},
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
