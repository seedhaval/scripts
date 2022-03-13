#!/usr/bin/perl

# This perl script generates an ImageMagick script to create 7 segment display.
# Author : Shah, Dhaval
# Date : July 18, 2015
# The output ImageMagick script is written to stdout.
# Usage : perl CreateIMScript.pl "0891" > IMScript.sh
# Here 0891 is the number that is to be displayed and can be replaced
# by any other number that needs to be displayed
# The ImageMagick script will be saved to IMScript.sh

use strict;
use warnings;


my $number = shift;
my @digits;
my $counter;
my $digit;
my $line;
my $p1;
my $p2;
my $OUTFILE;
my $filenum = 1;

my $COLOR_OFF = '"#400000"';
my $COLOR_ON = "red";
my $COLOR_BACKGROUND = "black";


my %GRAPH;
my %GEOMETRY;
my %EDGE;


$GRAPH{"0"} = "1234560";
$GRAPH{"1"} = "0230000";
$GRAPH{"2"} = "1204507";
$GRAPH{"3"} = "1234007";
$GRAPH{"4"} = "0230067";
$GRAPH{"5"} = "1034067";
$GRAPH{"6"} = "1034567";
$GRAPH{"7"} = "1230000";
$GRAPH{"8"} = "1234567";
$GRAPH{"9"} = "1234067";


$EDGE{1} = "10,10";
$EDGE{2} = "40,10";
$EDGE{3} = "40,40";
$EDGE{4} = "40,70";
$EDGE{5} = "10,70";
$EDGE{6} = "10,40";


$GEOMETRY{1} = "1 2";
$GEOMETRY{2} = "2 3";
$GEOMETRY{3} = "3 4";
$GEOMETRY{4} = "4 5";
$GEOMETRY{5} = "5 6";
$GEOMETRY{6} = "6 1";
$GEOMETRY{7} = "6 3";


print "#!/bin/bash\n\n";


@digits = split( "", $number );
foreach $digit (@digits){
	$OUTFILE = "tmp_" . sprintf("%02d", $filenum) . ".png" ;
	print "convert -size 60x80 xc:$COLOR_BACKGROUND \\\n";
	$counter = 1;
	foreach $line (split( "", $GRAPH{$digit} )){
		( $p1, $p2 ) = split(" ", $GEOMETRY{$counter}) ;
		if( $line eq "0" ){
			print "-stroke $COLOR_OFF -strokewidth 3 -draw \"line $EDGE{$p1} $EDGE{$p2}\" \\\n";
		}else{
			print "-stroke $COLOR_ON -strokewidth 3 -draw \"line $EDGE{$p1} $EDGE{$p2}\" \\\n";
		}
		$counter = $counter + 1;
	}
	print "$OUTFILE\n\n";
	
	$filenum = $filenum + 1;
}

print "convert tmp_*.png +append Output.png\n";

