parts=$1
color=$2

data=`identify -verbose tmp.gif | grep Geometry`
data=`echo $data | cut -d '+' -f 1 | cut -d ' ' -f 2`

width=`echo $data | cut -d 'x' -f 1`
height=`echo $data | cut -d 'x' -f 2`

div=$((width / parts))
div=`echo $div | cut -d '.' -f 1`

texty=$((height/2))
texty=`echo $texty | cut -d '.' -f 1`

posx=$div
while [ $posx -lt $width ]
do
	convert tmp.gif -stroke $color -draw "line $posx,1,$posx,$height" -pointsize 24 -annotate +"$posx"+"$texty" "$posx" tmp.gif
	posx=$((posx + div))
done

