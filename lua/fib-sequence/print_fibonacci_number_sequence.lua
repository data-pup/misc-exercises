-- This script prints the nth Fibonacci number.

-- These hold the two current sums being computed
fib_1 = 1
fib_2 = 1

-- This is the number n that we will use to find the number of loops to run.
my_n = 10

-- Print the first two numbers before continuing
print(fib_1)
print(fib_2)

-- This is the loop to calculate the sum of the last two numbers, and
-- store the next two numbers that we will add.
loop_iterator = 1
while loop_iterator < my_n
do
    my_sum = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = my_sum

    print(my_sum)

    loop_iterator = loop_iterator + 1
end

