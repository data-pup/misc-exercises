 /* This is a simple example of generating a sequence of random numbers,
 * using a dynamic array in C++. For this exercise, we will use hard-coded
 * values as a proof of concept, but these can be passed in through argv.
*/
#include <stdlib.h>
#include <iostream>


int main()
{
    // Initialize the pseudo-random number generator's seed value, and
    // the size of the array that we should create.
    unsigned int seed = 123;
    unsigned int array_size = 10;

    // Allocate the arrays that we will use.
    double* rand = new double [array_size];
    double* scaled_rand = new double [array_size];

    // Seed the random number generator.
    srandom(seed);

    // Fill the array with a sequence of pseudo-random numbers, and
    // scale each number to a value between 0 and 1, using RAND_MAX.
    for( unsigned int i = 0; i < array_size; i++ )
    {
        rand[i] = random();
        scaled_rand[i] = rand[i] / RAND_MAX;
    }

    // Because this is a simple example, delete the arrays at this point.
    // (Use a debugger like gdb or lldb to view the variables.)
    delete [] rand;
    delete [] scaled_rand;
    return 0;
}
