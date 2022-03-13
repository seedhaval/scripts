#!/bin/bash

declare -A vars

function pre_func {
	vars["state"]=$(set +o)
}

function post_func {
	eval ${vars["state"]}
} 

function move_file_name_simply {
	pre_func
	set -e

	inp_fldr=$1
	out_fldr=$2
	ext=$3

	i=$(date '+%y%m%d%H%M%S')
	for fl in $inp_fldr/*.$ext; do
		ofl=$out_fldr/$i.$ext
		echo "Moving $fl to $out_fldr/$ofl"
		
		mv "$fl" $ofl
		i=$(( i + 1 ))
	done

	post_func
}
typeset -fx move_file_name_simply

function get_video_duration {
	ffprobe -v error -sexagesimal -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 $1 | cut -d '.' -f 1
}
typeset -fx get_video_duration

function get_modified_time {
	stat -c '%y' $1 | cut -d '.' -f 1
}
typeset -fx get_modified_time

function get_image_height {
	identify -format '%h' $1
}
typeset -fx get_image_height

function get_file_extension {
	filename=$(basename -- "$1")
	echo "${filename##*.}"
}
typeset -fx get_file_extension

function scale_image {
	fl=$1
	sc=$2

	mogrify -resize ${sc}% $fl 
}
typeset -fx scale_image
