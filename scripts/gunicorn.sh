#!/bin/bash

sudo cp /home/ubuntu/cds-demo/required-files/gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
