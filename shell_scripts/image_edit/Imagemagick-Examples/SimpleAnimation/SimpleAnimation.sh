#!/bin/bash

# This script creates a simple gif that animates the text "Simple".
# The generated gif is opened using the animate program provided by Imagemagick.
# Gif loop is executed once.
# Author : Shah, Dhaval
# Date : July 17, 2015
# Usage : ./SimpleAnimation.sh

function createImage {
	convert \
		-size 640x480 \
		-background "#990033" \
		-font Ubuntu-Light \
		-fill "#FFFFCC" \
		-pointsize $1 \
		-gravity center \
		label:Simple \
		$2
}

for i in `seq 1 10`;
do
	SUBTRACTVAL=$(($i * 2))
	POINTSIZE=$((74 - $SUBTRACTVAL))
	FILENAME=Output_`printf %03d $i`.png
	createImage $POINTSIZE $FILENAME
done

convert -delay 10 -loop 1 Output_*.png Output.gif
rm Output_*.png
animate Output.gif

