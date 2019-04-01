#!/bin/bash

sudo unlink /etc/nginx/sites-enabled/*
sudo cp /home/ubuntu/cds-demo/required-files/chatApp /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/chatApp /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart



