parts=$1
color=$2

data=`identify -verbose tmp.gif | grep Geometry`
data=`echo $data | cut -d '+' -f 1 | cut -d ' ' -f 2`

width=`echo $data | cut -d 'x' -f 1`
height=`echo $data | cut -d 'x' -f 2`

div=$((height / parts))
div=`echo $div | cut -d '.' -f 1`

textx=$((width/2))
textx=`echo $textx | cut -d '.' -f 1`

posy=$div
while [ $posy -lt $height ]
do
	convert tmp.gif -stroke $color -draw "line 1,$posy,$width,$posy" -pointsize 24 -annotate +"$textx"+"$posy" "$posy" tmp.gif
	posy=$((posy + div))
done

