width=$1
height=$2
offsetx=$3
offsety=$4

convert tmp.gif -crop "$width"x"$height"+"$offsetx"+"$offsety" +repage tmp.gif
