#!/usr/bin/perl
## script: fltr_bin_toops.pl
## description: filter from bin_toops.txt only those 2-toops
## whose keys consist of one small cap and one large cap
## author: vladimir kulyukin
use strict;
use warnings;
while ( <> ) { print $1 . "\t" . $2 . "\n" if ( $_ =~ /^([a-z][A-Z])\t(\d+)$/ ); }


