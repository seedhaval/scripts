i have installed GNURoot Debian on my android phone. It provides a very good Linux environment.
i have also installed ImageMagick on this Linux environment. It was getting very difficult for me
to type whole ImageMagick commands on the phone. With the small keyboard, editing and writing
commands and providing full paths was tiresome. This inspired me on creating this mobile wrapper
program. This program is a wrapper around ImageMagick commands. When this program is called,
it expands the commands into ImageMagick commands and then runs them. It does not do any image
manipulation on its own. The main intention of this wrapper is to reduce keyboard strokes so that
it is easier to code on mobile device.

Say for example i want to scale file /home/images/d/1.jpg to 50%, then flip it vertically, then put
this image on top of /home/images/d/3.jpg at position (100,200). The output image is to be saved at
/home/images/e/1.png.
With the mobile wrapper script, the program is as small as

l d.1.j
sc 50
fv 
b d.3.j 100 200
s e.1.p

The config file is set as per my folder locations. It can be modified as required. I use
desktop.conf to test on desktop machine and use mobile.conf to test on mobile device. To call
wrapper, declare alias as 
alias imm="sh <basepath>/imm/bin/imm <basepath>/imm/conf/desktop.conf"

Save imm scripts as 1.imm, 2.imm, etc.
To run imm script 2.imm, run
imm 2

file extension should not be provided and it should always be .imm file. Whole intention is to reduce
number of keystrokes.

Specifying File Paths
======================
File paths can be specified as 
<directory alias>.<filename>.<extension alias>
Directory alias can be configured in configuration file. Desktop.conf or mobile.conf can be
used as reference for the configuration file.
the entry "adir=/home/user/images/d" indicates that "a" is alias for path "/home/user/images/d"
extension alias -
use j for jpg
use g gor gif
use p for png
note that extension alias is case sensitive. If you have extension as JPEG or JPG, then new entry
has to be made in sed.conf file.
The file path "d.1.g" will refer to
"/home/user/images/d/1.gif"

Intermediate Transformations
============================
Output of each command is stored to tmp.gif in current folder. To save output to another location
use "s" command after all transformations have been applied.

List of commands
================
l <path>
loads the file present at path
for example 
l d.1.j
all files are converted to tmp.gif when loaded. Gif format is used so that transparency can be achieved.

cb <width> <height>
create a blank image with transparent background. Width and height are pixels values.

s <path>
save current tmp.gif file to path.

sc <number>
scale image by number %

fv
flip the image vertically

fh
flip the image horizontally

f <path> <topx> <topy>
add image present at <path> to foreground at position <topx> <topy>

b <path> <topx> <topy>
add current image to foreground of <path> at position <topx> <topy>

r <number>
rotate image by number degrees

hx <number> <color>
provide help for x values. The image is split into <number> parts and a line in <color>
is drawn with the x co-ordinate of pixel mentioned.

hy <number> <color>
provide help for y values. The image is split into <number> parts and a line in <color>
is drawn with the y co-ordinate of pixel mentioned.

c <width> <height> <topx> <topy>
crop image with window size of <width>x<height> and window top left position at <topx> <topy>


