#!/bin/bash

# Redeploy script for Alan's Portfolio Site
# Updated to use systemd service instead of tmux

echo "Starting redeploy process..."

# Step 1: cd into your project folder
cd /root/alan-portfolio

# Step 2: Run git fetch && git reset origin/main --hard to make sure the git repository has the latest changes from the main branch on GitHub
echo "Fetching latest changes from GitHub..."
git fetch && git reset origin/main --hard

# Step 3: Enter the python virtual environment and install python dependencies
echo "Activating virtual environment and installing dependencies..."
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 4: Restart myportfolio service
echo "Restarting myportfolio service..."
systemctl restart myportfolio
systemctl status myportfolio

echo "Redeploy completed successfully!"
echo "Site is available at: http://209.38.77.52:8000" 