#!/bin/bash
# Instalar Apache2 en una máquina vulnerable
sudo apt update
sudo apt install apache2 -y
sudo systemctl start apache2
echo "<h1>Servidor Web Vulnerable</h1>" | sudo tee /var/www/html/index.html
sudo ufw allow 80/tcp
