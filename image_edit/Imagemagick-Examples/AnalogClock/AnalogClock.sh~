#!/bin/bash

# This script creates an analog clock
# Author : Shah, Dhaval
# Date : July 26, 2015
# Usage : ./AnalogClock.sh hour minute
# For e.g. :
# ./AnalogClock.sh 6 35
# ./AnalogClock.sh 23 30
# ./AnalogClock.sh 8 25

export HOUR=$1
export MINUTE=$2

export CLOCKRADIUS=200
export NUMRADIUS=20

export BACKCOLOR=YELLOW
export NUMCOLOR=BROWN
export HANDCOLOR=BLACK

OUTERDIAMETER=$((CLOCKRADIUS * 2))
convert \
	-size "$OUTERDIAMETER"x"$OUTERDIAMETER" xc:none \
	-fill "$BACKCOLOR" \
	-gravity center \
	-stroke "$HANDCOLOR" \
	-strokewidth 2 \
	-draw "circle $CLOCKRADIUS,$CLOCKRADIUS 0,$CLOCKRADIUS" \
	tmp_outercircle.png

INNERDIAMETER=$((NUMRADIUS * 2))
function createSmallerCircle {
	convert \
		-size "$INNERDIAMETER"x"$INNERDIAMETER" \
		-gravity center \
		-background transparent \
		-font Ubuntu-Bold \
		-fill "$NUMCOLOR" \
		-pointsize 24 \
		label:"$1" \
		tmp_innercircle_$1.png
}

createSmallerCircle 3
createSmallerCircle 6
createSmallerCircle 9
createSmallerCircle 12

POSX3=$((OUTERDIAMETER - INNERDIAMETER))
POSY3=$((CLOCKRADIUS - NUMRADIUS))
POSX6=$((CLOCKRADIUS - NUMRADIUS))
POSY6=$((OUTERDIAMETER - INNERDIAMETER))
POSX9=0
POSY9=$((CLOCKRADIUS - NUMRADIUS))
POSX12=$((CLOCKRADIUS - NUMRADIUS))
POSY12=0

convert tmp_outercircle.png \
	\( tmp_innercircle_3.png -repage +"$POSX3"+"$POSY3" \) \
	\( tmp_innercircle_6.png -repage +"$POSX6"+"$POSY6" \) \
	\( tmp_innercircle_9.png -repage +"$POSX9"+"$POSY9" \) \
	\( tmp_innercircle_12.png -repage +"$POSX12"+"$POSY12" \) \
	-flatten \
	tmp_base.png

HOURLENGTH=$((CLOCKRADIUS - INNERDIAMETER - INNERDIAMETER))
MINUTELENGTH=$((CLOCKRADIUS - INNERDIAMETER))

HOURLENGTH2=$((HOURLENGTH * 2))
MINUTELENGTH2=$((MINUTELENGTH * 2))

MINUTEROTATION=$((MINUTE * 6))
HOURROTATION=$((HOUR * 30))

convert	-size "4"x"$HOURLENGTH2" xc:none \
	-stroke "$HANDCOLOR" \
	-strokewidth 3 \
	-draw "line 1,1 1,$HOURLENGTH" \
	-stroke TRANSPARENT \
	-strokewidth 3 \
	-fill transparent \
	-draw "line 1,$HOURLENGTH 1,$HOURLENGTH2" \
	tmp_hourline.png

convert	-size "4"x"$MINUTELENGTH2" xc:none \
	-stroke "$HANDCOLOR" \
	-strokewidth 3 \
	-draw "line 1,1 1,$MINUTELENGTH" \
	-stroke TRANSPARENT \
	-strokewidth 3 \
	-fill transparent \
	-draw "line 1,$MINUTELENGTH 1,$MINUTELENGTH2" \
	tmp_minuteline.png

convert tmp_base.png \
	\( tmp_hourline.png -gravity center -background transparent -rotate "$HOURROTATION" \) \
	-composite \
	tmp_out.png

convert tmp_out.png \
	\( tmp_minuteline.png -gravity center -background transparent -rotate "$MINUTEROTATION" \) \
	-composite \
	out.png

rm tmp*
display out.png


