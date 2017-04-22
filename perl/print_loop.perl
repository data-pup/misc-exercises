#!/usr/bin/perl
use strict;
use warnings;

# This loop will print a number to the terminal.

# Counters for the while loop
my $loop_counter = 0;
my $loop_maximum = 10;

# Print loop_counter until it reaches the maximum value
while( $loop_counter < $loop_maximum ) {
    print $loop_counter;
    $loop_counter = $loop_counter + 1
}
