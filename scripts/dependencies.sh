#!/bin/bash
sudo apt-get install python3-pip python3-dev nginx git -y
pip3 install virtualenv -y
virtualenv /home/ubuntu/venv
chown ubuntu:ubuntu cds-demo
source /home/ubuntu/venv/bin/activate
pip3 install -r /home/ubuntu/cds-demo/requirements/base.txt
pip3 install django bcrypt django-extensions
pip3 install gunicorn -y
python3 /home/ubuntu/cds-demo/chatApp/manage.py collectstatic
cp /home/ubuntu/cds-demo/required-files/gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
cp /home/ubuntu/cds-demo/required-files/chatApp /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/learnDjango /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
