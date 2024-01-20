#!/bin/bash

cd /root/git/HackAndRollBE
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --port 8090
