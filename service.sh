#!/bin/bash

sudo apt-get update -y
sudo apt-get install python3-venv -y

cd /home/ubuntu
git clone https://github.com/akshitsaini111/BAck.git

cd BAck

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
uvicorn app.main:app --host 0.0.0.0 --port 6969