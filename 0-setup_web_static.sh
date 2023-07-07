#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Welcome to our AirBnB" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

CONFIG_FILE="/etc/nginx/sites-available/default"

if ! sudo grep -q "location /hbnb_static" "$CONFIG_FILE"; then
	sudo sed -i '/^server {/a\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$CONFIG_FILE"
fi

sudo service nginx restart
