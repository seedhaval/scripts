cmd=$1
parameter=$2

case $cmd in
	p)
		sudo poweroff
		;;
	ds)
		df -h /
		;;
	w)
		nmcli nm wifi on
		;;

	w0)
		nmcli nm wifi off
		;;

	b)
		xrandr --output LVDS1 --brightness $parameter
		;;	

	blo)
		rfkill block bluetooth
		;;

	*)
		echo "p  -> power off"
		echo "ds -> disk space"
		echo "w  -> wifi on"
		echo "w0 -> wifi off"
		echo "b  -> set brightness. enter value between 0.1 and 1.0"	
		echo "blo -> bluetooth off"
	
		;;
esac

