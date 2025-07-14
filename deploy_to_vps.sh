#!/bin/bash

# Deployment script for Alan's Portfolio to VPS
# Usage: ./deploy_to_vps.sh

VPS_HOST="root@209.38.77.52"
VPS_PORTFOLIO_DIR="/root/alan-portfolio"

echo "Deploying Alan's Portfolio to VPS..."

# Copy the updated Flask app to VPS
echo "Copying updated Flask app..."
scp -i ~/.ssh/id_ed25519 app/__init__.py ${VPS_HOST}:${VPS_PORTFOLIO_DIR}/app/

# Copy the setup script
echo "Copying setup script..."
scp -i ~/.ssh/id_ed25519 vps_setup.sh ${VPS_HOST}:/root/

# Copy the improved systemd service file
echo "Copying systemd service file..."
scp -i ~/.ssh/id_ed25519 myportfolio.service ${VPS_HOST}:/etc/systemd/system/

# Run the setup script on VPS
echo "Running setup script on VPS..."
ssh -i ~/.ssh/id_ed25519 ${VPS_HOST} << 'EOF'
chmod +x /root/vps_setup.sh
/root/vps_setup.sh
EOF

# Restart the systemd service
echo "Restarting systemd service..."
ssh -i ~/.ssh/id_ed25519 ${VPS_HOST} << 'EOF'
systemctl daemon-reload
systemctl restart myportfolio
systemctl enable myportfolio
systemctl status myportfolio --no-pager
EOF

echo "Deployment complete!"
echo "Your portfolio should now be accessible at http://209.38.77.52:5000" 