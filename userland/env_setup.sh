#!/bin/bash

set -e -u -o pipefail

sudo apt update
sudo apt upgrade

echo "Installing git and python3"
sudo apt-get install git python3

echo "Cloning repository"
cd
git clone https://github.com/seedhaval/scripts

echo "Transfering control to env_setup.py to carry out chechpointed setup"
python3 ~/scripts/userland/env_setup.py
