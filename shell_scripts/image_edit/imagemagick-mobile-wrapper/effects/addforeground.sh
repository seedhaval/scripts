filename=$1
posx=$2
posy=$3
convert tmp.gif $filename -geometry +"$posx"+"$posy" -composite tmp.gif

