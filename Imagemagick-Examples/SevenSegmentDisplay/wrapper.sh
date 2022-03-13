# This is the wrapper script to generate seven segment display
# Author : Shah, Dhaval
# Date : July 18, 2015
# First perl script is called that generates the ImageMagick script
# Then the generated ImageMagick script is executed.
# Usage : ./wrapper.sh <number>
# Where <number> is the number that is to be displayed

perl CreateIMScript.pl $1 > tmp.sh
chmod 777 tmp.sh
./tmp.sh
rm tmp*
display Output.png

