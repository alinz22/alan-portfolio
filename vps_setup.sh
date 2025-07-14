#!/bin/bash

# VPS Setup Script for Alan's Portfolio
# This script installs and configures MySQL for the Flask application

echo "Starting VPS setup for Alan's Portfolio..."

# Update system packages
echo "Updating system packages..."
dnf update -y

# Install MySQL server
echo "Installing MySQL server..."
dnf install -y mysql-server

# Start and enable MySQL service
echo "Starting MySQL service..."
systemctl start mysqld
systemctl enable mysqld

# Secure MySQL installation and create database
echo "Configuring MySQL..."
mysql << 'EOF'
ALTER USER 'root'@'localhost' IDENTIFIED BY 'rootpassword';
CREATE DATABASE myportfolio;
CREATE USER 'myportfolio'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON myportfolio.* TO 'myportfolio'@'localhost';
FLUSH PRIVILEGES;
EOF

# Create .env file in the portfolio directory
echo "Creating .env file..."
cat > /root/alan-portfolio/.env << 'EOF'
URL=localhost:5000
MYSQL_HOST=localhost
MYSQL_USER=myportfolio
MYSQL_PASSWORD=password
MYSQL_DATABASE=myportfolio
FLASK_SECRET=production_secret_key_change_this
EOF

# Make sure the Flask app can access the database
echo "Testing database connection..."
cd /root/alan-portfolio
source python3-virtualenv/bin/activate
python3 -c "import app; print('Database setup successful!')"

echo "VPS setup complete!"
echo "You can now restart the systemd service:"
echo "systemctl restart myportfolio"
echo "systemctl status myportfolio" 