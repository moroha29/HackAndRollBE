#!/bin/bash

source venv/bin/activate
uvicorn src.main:app --port 8090
