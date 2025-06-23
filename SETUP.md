# Portfolio Setup Instructions

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Quick Start

1. **Clone or navigate to your portfolio directory:**

   ```bash
   cd alan-portfolio
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your personal photos:**

   - Add your headshot as `app/static/img/me.jpg`
   - Add hobby images:
     - `app/static/img/music_festival.jpg`
     - `app/static/img/food.jpg`
     - `app/static/img/gaming.jpg`
     - `app/static/img/travel.jpg`
     - `app/static/img/placeholder.jpg` (fallback image)

4. **Set environment variables (optional):**

   ```bash
   cp example.env .env
   # Edit .env file with your preferred settings
   ```

5. **Run the application:**

   ```bash
   python -m flask --app app run --debug
   ```

6. **Open your browser:**
   - Go to `http://localhost:5000`
   - Your portfolio is now running!

## 📁 Required Images

Make sure to add these images to `app/static/img/`:

- **me.jpg** - Your professional headshot (square format recommended)
- **music_festival.jpg** - Music festival photo
- **food.jpg** - Food/dining photo
- **gaming.jpg** - Gaming setup or related image
- **travel.jpg** - Travel destination photo
- **placeholder.jpg** - Default image for missing photos

## 🎨 Customization

- Edit `data.py` to update your personal information
- Modify templates in `app/templates/` for layout changes
- Add custom CSS in `app/static/styles/main.css`

## 🐛 Troubleshooting

**Port already in use?**

```bash
python -m flask --app app run --debug --port 5001
```

**Missing images?**

- Check that image files are in the correct `app/static/img/` directory
- Ensure file names match exactly (case-sensitive)
- The placeholder.jpg will show for missing images

## 📦 Dependencies

All required packages are in `requirements.txt`:

- Flask
- python-dotenv

## 🎯 Submission Checklist

- ✅ All pages load without errors
- ✅ Navigation works between all sections
- ✅ Personal photo displays correctly
- ✅ Hobby images show properly
- ✅ Travel map displays with your locations
- ✅ Contact information is accurate
- ✅ Resume data is up to date
