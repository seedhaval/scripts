#!/bin/bash

set -e -u -o pipefail

sudo apt update
sudo apt upgrade

echo "Installing git and python3"
sudo apt-get install ssh git python3

echo "setting up git"
ssh-keygen
read -p "Enter user name : " usr
read -p "Enter email : " eml
git config --global user.name "${usr}"
git config --global user.email "${eml}"
cat ~/.ssh/id_rsa.pub
echo ""
echo "Copy above ssh key to github and then press enter"
read a


echo "Cloning repository"
cd
git clone git@github.com:seedhaval/scripts.git

echo "Transfering control to env_setup.py to carry out checkpointed setup"
python3 ~/scripts/shell_scripts/userland/env_setup.py
