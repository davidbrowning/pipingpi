#!/usr/bin/perl
## script: fltr_large_cap_toops.pl
## description: filter from bin_toops.txt only those 2-toops
## whose keys consist of two large caps.
## author: vladimir kulyukin
use strict;
use warnings;
while ( <> ) { print $1 . "\t" . $2 . "\n" if ( $_ =~ /^([A-Z][A-Z])\t(\d+)$/ ); }


