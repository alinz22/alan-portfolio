#!/bin/bash

# Redeploy script for Alan's Portfolio Site
# Updated to use Docker Compose for container orchestration

echo "========================================="
echo "Starting redeploy process..."
echo "========================================="

# Step 1: cd into your project folder
cd /root/alan-portfolio
echo "✅ Changed to project directory"

# Step 2: Run git fetch && git reset origin/main --hard to make sure the git repository has the latest changes from the main branch on GitHub
echo "Fetching latest changes from GitHub..."
git fetch && git reset origin/main --hard
echo "✅ Repository updated to latest main branch"

# Step 3: Stop and remove existing containers
echo "Stopping existing containers..."
docker compose -f docker-compose.prod.yml down
echo "✅ Existing containers stopped and removed"

# Step 4: Build and start new containers in detached mode
echo "Building and starting new containers..."
docker compose -f docker-compose.prod.yml up -d --build
echo "✅ New containers built and started"

# Step 5: Check container status
echo ""
echo "Checking container status..."
docker compose -f docker-compose.prod.yml ps

# Step 6: Display logs from the last 10 lines
echo ""
echo "Recent logs from myportfolio container:"
docker compose -f docker-compose.prod.yml logs --tail=10 myportfolio

echo ""
echo "========================================="
echo "Redeploy completed successfully! ✨"
echo ""
echo "Site is available at:"
echo "  HTTP:  http://pe-week1-demo.duckdns.org"
echo "  HTTPS: https://pe-week1-demo.duckdns.org"
echo ""
echo "Note: HTTPS certificates will be automatically generated"
echo "by Let's Encrypt on first access."
echo "=========================================" 