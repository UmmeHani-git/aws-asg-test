#!/bin/bash

yum update -y
yum install -y python3 git nginx

cd /home/ec2-user

git clone https://github.com/YOUR_USERNAME/flipkart-advanced.git

cd flipkart-advanced

pip3 install -r requirements.txt

# Start Flask in background
nohup python3 app.py > app.log 2>&1 &

# Configure Nginx
cp nginx.conf /etc/nginx/conf.d/default.conf

systemctl enable nginx
systemctl start nginx
