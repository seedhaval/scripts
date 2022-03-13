filename=$1
posx=$2
posy=$3
convert $filename tmp.gif -geometry +"$posx"+"$posy" -composite tmp.gif

