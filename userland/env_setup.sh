#!/bin/bash

set -e -u -o pipefail
echo "Installing git and python3"
sudo apt-get install git python3

echo "Cloning repository"
cd
git clone https://github.com/seedhaval/scripts
