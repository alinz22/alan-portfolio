# Alan Mong - Portfolio Site

Welcome to my personal portfolio site built with Flask! This portfolio showcases my experience as a full-stack software engineer and Meta SRE Fellow, featuring my projects, work experience, education, hobbies, and travel adventures.

## 🚀 Live Features

- **Home Page**: Introduction with tech stack badges and key stats
- **About Page**: Professional photo, work experience timeline, and education
- **Projects Page**: Featured projects with live links (TaskStars, InfraWatch)
- **Hobbies Page**: Personal interests with images and descriptions
- **Travel Page**: Interactive map showing 11+ cities across 4 countries
- **Responsive Design**: Modern dark theme with hover animations

## 🐳 Docker Deployment

This portfolio is containerized using Docker and orchestrated with Docker Compose for easy deployment.

### Quick Deploy with Docker Compose

```bash
# Clone the repository
git clone https://github.com/alinz22/alan-portfolio.git
cd alan-portfolio

# Copy and configure environment variables
cp example.env .env
# Edit .env with your MySQL credentials

# Run with Docker Compose
docker compose up -d

# View logs
docker compose logs -f
```

### Production Deployment

For production deployment on a VPS with HTTPS:

```bash
# Configure your domain and email
cp example.env .env
# Edit .env and set CERTBOT_EMAIL to your email

# Update nginx configuration
# Edit user_conf.d/myportfolio.conf and replace pe-week1-demo.duckdns.org
# with your actual domain name

# Deploy with the production compose file
docker compose -f docker-compose.prod.yml up -d

# Or use the redeploy script
./redeploy-site.sh
```

The production setup includes:

- **Nginx reverse proxy** with automatic HTTPS
- **Let's Encrypt** SSL certificates (auto-renewed)
- **HTTP to HTTPS** redirect
- **Docker networking** for secure container communication

The `redeploy-site.sh` script handles:

- Pulling latest changes from GitHub
- Stopping existing containers
- Building and starting new containers
- Displaying container status

## ✅ Completed Tasks

### GitHub Tasks

- [x] Create Issues for each task below
- [x] Progress on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks

- [x] Add a photo of yourself to the website
- [x] Add an "About yourself" section to the website
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks

- [x] Get your Flask app running locally on your machine
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies
- [x] Add a menu bar that dynamically displays other pages in the app

## 🛠️ Installation

### Prerequisites

- Python 3.8+ and pip installed
- macOS/Linux/Windows

### Setup Instructions

1. **Clone and navigate to the portfolio:**

   ```bash
   cd alan-portfolio
   ```

2. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Add your images (optional):**

   - Place photos in `app/static/img/`
   - Required: `me.jpg`, `loved_ones.jpg`, `music_festival.jpg`, `food.jpg`, `travel.jpg`, `placeholder.jpg`
   - See `IMAGES_NEEDED.md` for details

4. **Set up environment variables (optional):**
   ```bash
   cp example.env .env
   # Edit .env with your preferred settings
   ```

## 🚀 Usage

### Start the Development Server

```bash
export FLASK_APP=app && flask run --debug --port 5001
```

You should see:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

### Access Your Portfolio

Open your browser and navigate to:

- **Main site**: http://localhost:5001
- **About page**: http://localhost:5001/about
- **Projects**: http://localhost:5001/projects
- **Hobbies**: http://localhost:5001/hobbies
- **Travel map**: http://localhost:5001/travel

## 📁 Project Structure

```
alan-portfolio/
├── app/
│   ├── __init__.py          # Flask app and routes
│   ├── templates/           # HTML templates
│   │   ├── base.html       # Base template with navigation
│   │   ├── home.html       # Homepage with stats and tech stack
│   │   ├── about.html      # About page with timeline
│   │   ├── projects.html   # Projects showcase
│   │   ├── hobbies.html    # Hobbies with images
│   │   └── travel.html     # Interactive travel map
│   └── static/
│       ├── img/            # Images and photos
│       └── styles/         # CSS files
├── data.py                 # Portfolio data (experience, projects, etc.)
├── requirements.txt        # Python dependencies
├── example.env            # Environment variables template
└── README.md              # This file
```

## 🎨 Features & Technologies

### Frontend

- **Flask** with Jinja2 templating
- **Bootstrap 5** for responsive design
- **Font Awesome** icons throughout
- **Leaflet.js** for interactive travel map
- **Custom CSS** with animations and hover effects

### Data Management

- **Dynamic content** driven by `data.py`
- **Modular structure** for easy updates
- **Responsive design** for all devices

### Pages

- **Home**: Hero section, stats cards, tech stack, contact links
- **About**: Professional photo, experience timeline, education table
- **Projects**: Featured projects with external links
- **Hobbies**: Personal interests with images
- **Travel**: Interactive world map with visited locations

## 🔧 Customization

### Update Your Information

Edit `data.py` to customize:

- Work experience and internships
- Education details
- Projects and descriptions
- Tech skills and tools
- Hobbies and interests
- Travel locations

### Modify Styling

- Edit templates in `app/templates/`
- Update CSS in `app/static/styles/main.css`
- Customize colors and animations in `app/templates/base.html`

## 🐛 Troubleshooting

**Flask not found?**

```bash
pip3 install flask python-dotenv
```

**Port already in use?**

```bash
python3 -m flask --app app run --debug --port 5002
```

**Images not showing?**

- Check that image files are in `app/static/img/`
- Ensure filenames match exactly (case-sensitive)
- Add a `placeholder.jpg` for missing images

## 📈 Stats & Highlights

- **2+ Internships** (AVEVA, Swing Phi, Meta SRE Fellowship)
- **2× President's Honor List** at Cal Poly Pomona
- **10+ Projects** in portfolio
- **20+ Technologies** in tech stack
- **11+ Cities** visited across 4 countries

## 🎓 About Alan

Full-stack software engineer and Meta SRE Fellow graduating December 2026 from Cal Poly Pomona. Passionate about building scalable tools and systems, with experience across startup and enterprise environments.

## 📞 Contact

- **Email**: alanmongx@gmail.com
- **LinkedIn**: [linkedin.com/in/alan-mong](https://linkedin.com/in/alan-mong)
- **GitHub**: [github.com/alinz22](https://github.com/alinz22)

---

_This portfolio was built as part of the MLH Fellowship Production Engineering program._
