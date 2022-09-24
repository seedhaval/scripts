#!/bin/bash
set -e -u -o pipefail

cd /mnt/c/Users/Dell/Desktop/google_drive_bkp/
pdfunite $( find mind_maps -newer ~/.print_taken -iname '*.pdf' ) combined.pdf
