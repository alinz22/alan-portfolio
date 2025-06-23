# 📸 Images You Need to Add

## 📍 **Location:** `app/static/img/`

You need to add these 5 image files to the `app/static/img/` directory:

### **Required Images:**

1. **`loved_ones.jpg`** - Photo of you with family/friends

   - _Example: Group dinner, family gathering, hanging with friends_

2. **`music_festival.jpg`** - You at a music festival or concert

   - _Example: Festival crowd, you with festival wristbands, concert venue_

3. **`food.jpg`** - Food/dining related photo

   - _Example: You cooking, restaurant meal, food you made_

4. **`travel.jpg`** - Travel destination photo

   - _Example: You at any of your travel locations, landmark photo_

5. **`placeholder.jpg`** - Default image for missing photos
   - _Any generic image as backup_

## 🔧 **How to Add Images:**

### **Option 1: Drag & Drop (Mac Finder)**

1. Open Finder and navigate to your portfolio folder
2. Go to `alan-portfolio/app/static/img/`
3. Drag your photos into this folder
4. Rename them exactly as listed above

### **Option 2: Terminal**

```bash
# Navigate to images folder
cd /Users/alan/Portfolio/alan-portfolio/app/static/img/

# Copy images from Downloads (adjust path as needed)
cp ~/Downloads/your-photo.jpg ./loved_ones.jpg
cp ~/Downloads/festival-pic.jpg ./music_festival.jpg
cp ~/Downloads/food-pic.jpg ./food.jpg
cp ~/Downloads/travel-pic.jpg ./travel.jpg
cp ~/Downloads/placeholder.jpg ./placeholder.jpg
```

## ✅ **Quick Test:**

After adding images, refresh your browser at:
**http://localhost:5001/hobbies**

The images should appear automatically!

## 📱 **Image Tips:**

- **Size**: Keep under 2MB each for fast loading
- **Format**: JPG or PNG works fine
- **Dimensions**: 800x600 pixels or similar works great
- **Quality**: Phone photos are perfect!

## 🎯 **Current Status:**

- ✅ `me.jpg` - Already added!
- ❌ `loved_ones.jpg` - Need to add
- ❌ `music_festival.jpg` - Need to add
- ❌ `food.jpg` - Need to add
- ❌ `travel.jpg` - Need to add
- ❌ `placeholder.jpg` - Need to add
