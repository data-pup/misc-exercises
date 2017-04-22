#!/usr/local/bin/lua

-- This is the iterator for the while loop, and the maximum loop value.
loop_iterator = 0
loop_maximum = 10

-- Perform a while loop, and print the loop count at each point.
while loop_iterator < loop_maximum
do
    print(loop_iterator)
    loop_iterator = loop_iterator + 1
end
