#!/bin/bash

function getinput(){
	read -n 1 out
	
	c='dummy'
	while [ "$c" != "" ]
	do
		read -n 1 -t 0.3 c
		out="$out$c"
	done

	echo $out
}

function refreshbuf(){
	clist=`ls -1 "$cwd"`
	cbuf=`echo "$clist" | nl `
	max=`echo "$clist" | wc -l`
}

cwd="/home/dhaval"
refreshbuf

while true
do
	echo
	echo "$cbuf"
	echo 
	printf "enter option : "
	out=`getinput`
	echo
	case $out in
		[0-9]*)
				if ((1<=out && out<= max)); then
					nd=`echo "$clist" | head -$out | tail -1`
					cwd="$cwd/$nd"
					refreshbuf
				fi
				;;
		u)
				cwd="$(dirname "$cwd")"
				refreshbuf
				;;
		b)
				pushd "$cwd"
				bash
				popd
				refreshbuf
				;;
		v)
				printf 'enter file # to edit : '
				tout=`getinput`
				echo
				tf=`echo "$clist" | head -$tout | tail -1`
				vim "$cwd/$tf"
				;;
		c)
				printf 'enter file # to cat : '
				tout=`getinput`
				echo
				tf=`echo "$clist" | head -$tout | tail -1`
				cat "$cwd/$tf"
				;;
		h)
				clist=`ls -a1 "$cwd"`
				cbuf=`echo "$clist" | nl `
				max=`echo "$clist" | wc -l`
				;;
		l)
				ls -al "$cwd"
				;;
		e)
				nautilus "$cwd" &
				;;
		x)
				exit
				;;
	esac
done

