#!/bin/bash
set -e -u -o pipefail

cd ~/scripts
git add .
git commit -m "${1}"
git push
