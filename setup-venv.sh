#!/usr/bin/env bash

set -u;

virtualenv venv -p python3
source venv/bin/activate

which python

pip install --upgrade pip
pip install -r requirements.txt
