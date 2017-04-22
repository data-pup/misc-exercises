import random
import copy

# Arrays for holding the seed and generated sequences for each RNG state.
my_rng_states = []
my_generated_sequences = []

# Program parameters control number and size of randomly-generated sequences.
# These also control minimum and maximum values
# for the generated array elements.
number_of_sequences = 5
size_of_sequences = 25
random_minimum = 0
random_maximum = 100

# Seed the random number generator and save these states into my_rng_states.
def create_seeds():
    for current_sequence in range(number_of_sequences):
        random.seed()
        my_state = random.getstate()
        my_rng_states.append(my_state)

# This will clear the RNG states array.
def clear_seeds():
        my_rng_states.clear()

# Fill each sequence with randomly generated numbers, using the saved states.
def fill_sequences():
    for current_sequence in range(number_of_sequences):

        # Declare a new sequence variable, and set the RNG state.
        random.setstate(my_rng_states[current_sequence])
        my_new_sequence = []

        # Append new random numbers to the sequence.
        for current_element in range(size_of_sequences):
            my_new_sequence.append(random.randint(random_minimum,random_maximum))

        # Copy the generated sequence into the generated sequences list.
        my_generated_sequences.append(copy.deepcopy(my_new_sequence))

# Now, print the sequences to stdout, one at a time.
def print_sequences():
    for current_sequence in range(number_of_sequences):
        title_string = "Sequence #{}:".format(current_sequence)
        print(title_string)
        print(my_generated_sequences[current_sequence])
        print("")

# Now, clear the sequences and repeat the process.
def clear_sequences():
    my_generated_sequences.clear()

# This function will print a line of hyphens, for output formatting.
def print_hyphen_line():
    my_line = ""
    for i in range(80):
        my_line = my_line + "-"
    print(my_line)

# This is the main function.
def main():
    create_seeds()
    for i in range(2):
        title_string = "Sequence Generation Process Iteration #{}".format(i+1)
        print(title_string)
        print_hyphen_line()
        fill_sequences()
        print_sequences()
        clear_sequences()
    clear_seeds()

if __name__ == '__main__':
    main()
