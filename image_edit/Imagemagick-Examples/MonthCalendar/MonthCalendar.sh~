#!/bin/bash

# This script creates a calendar image
# Author : Shah, Dhaval
# Date : July 19, 2015
# Usage : ./MonthCalendar.sh <month> <year>
# For e.g. :
# ./MonthCalendar.sh july 2015
# ./MonthCalendar.sh june 2002
# ./MonthCalendar.sh may 2015
# The inbuilt calendar provided by bash is used to get data
# This data is then formatted using ImageMagick

cal $1 $2 > tmp.txt

num=0
while IFS='' read -r value || [[ -n $value ]]; do
	line[$num]=$value
	num=$((num + 1))
done < tmp.txt

function createImage {
	convert \
		-size 700x75 \
		-background "#FFFFCC" \
		-font $2 \
		-fill "#FF0000" \
		-pointsize 48 \
		-gravity center \
		label:"$1" \
		$3
}

createImage "${line[0]}" Ubuntu-Bold tmp_0.png
createImage "${line[1]}" Ubuntu-Mono-Regular tmp_1.png
createImage "${line[2]}" Ubuntu-Mono-Regular tmp_2.png
createImage "${line[3]}" Ubuntu-Mono-Regular tmp_3.png
createImage "${line[4]}" Ubuntu-Mono-Regular tmp_4.png
createImage "${line[5]}" Ubuntu-Mono-Regular tmp_5.png
createImage "${line[6]}" Ubuntu-Mono-Regular tmp_6.png
createImage "${line[7]}" Ubuntu-Mono-Regular tmp_7.png
createImage "  " Ubuntu-Mono-Regular tmp_8.png


convert tmp_*.png -append tmp1.png

echo "convert tmp1.png \\" > tmp.sh
for i in `seq 1 8`;
do
	YVALUE=$(($i * 75))
	XVALUE=$(($i * 72))
	echo "-stroke black -strokewidth 1 -draw \"line 72,$YVALUE 576,$YVALUE\" \\" >> tmp.sh
	echo "-stroke black -strokewidth 1 -draw \"line $XVALUE,75 $XVALUE,600\" \\" >> tmp.sh
done
echo "out.png" >> tmp.sh

sh tmp.sh
rm tmp*
display out.png


