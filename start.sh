#!/bin/bash

cd /root/git/HackAndRollBE
source venv/bin/activate
uvicorn src.main:app --port 8090
