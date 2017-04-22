import sys
import array
import math
import random
import datetime
import csv

# Input parameters:
# arg1 : size of random sequence to be generated
# arg2 : random number generator seed
# arg3 : name for file to be printed
number_of_observations = int(sys.argv[1])
random_seed = int(sys.argv[2])
outfile_path = sys.argv[3]

# Array variables
random_value_array = []
current_random_number = 0

# Seed the random number generator
random.seed(random_seed)

# Perform the random number generation procedures
for cur_obv in range(number_of_observations):

    # Generate a random number with the total number of bits,
    # and a second random number using a better generator
    current_random_number = random.triangular(0,1,1)

    # Add the current list of chunks into the random_value_array
    random_value_array.append(current_random_number)

# Open the output file
# NOTE: This is a basic example, in a serious context this
# should be enclosed in a try/except statement.
outfile = open( outfile_path, 'w' )

# Write the values in cur_value to the output file
# TODO: Check that the file is open before calling write()
# if using this outside of basic exercises.
for cur_value in random_value_array:
    outfile.write(str(cur_value))
    outfile.write('\n')
