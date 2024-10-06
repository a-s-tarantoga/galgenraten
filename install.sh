#!/bin/bash

python3.12 -m venv .
source ./bin/activate
python3.12 -m pip install requests beautifulsoup4

deactivate