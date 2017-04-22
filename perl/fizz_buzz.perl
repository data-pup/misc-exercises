#!/usr/bin/perl
use strict;
use warnings;

# This script will print the fizz buzz exercise in perl.
# If the current_loop counter is divisible by 3, print "Fizz."
# If the current_loop counter is divisible by 5, print "Buzz."
# Otherwise, print the current_loop counter.

my $current_loop = 0;
my $loop_maximum = 100;

while( $current_loop < $loop_maximum ){

    if($current_loop % 3 == 0){ print "Fizz"; }
    if($current_loop % 5 == 0){ print "Buzz"; }


    if( ($current_loop % 3 != 0) && ($current_loop % 5 != 0) ) {
        print $current_loop;
    }

    print "\n";
    $current_loop++;
}
