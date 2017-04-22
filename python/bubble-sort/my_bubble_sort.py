# --------------------------------------------------------------------------- #
# Implement a bubble sort in Python 3.5


# Declare an example array using a list
# my_list = [1,2,3,4,5]
# my_array = arr.array('B', my_list)

# Print the array
# for my_array_element in my_array:
#     print(my_array_element)

# This is the definition of the bubble sort function.
# Sort an array using the bubble sort algorithm.
# NOTE: This is not an in-place algorithm.
def my_bubble_sort( original_sequence ):

    # DEBUG:
    # Can I import a library from within a function?
    import copy
    import array as arr

    # Initialize a deep copy of my_sequence.
    new_sequence = copy.deepcopy(original_sequence)

    # Bubble sort algorithm
    n = len(new_sequence)
    my_dummy_var = None
    was_swapped = True

    while was_swapped:
        was_swapped = False
        for i in range(n):
            if (i > 0) and (new_sequence[i-1] > new_sequence[i]):
                my_dummy_var = new_sequence[i-1]
                new_sequence[i-1] = new_sequence[i]
                new_sequence[i] = my_dummy_var
                was_swapped = True
        n = n - 1

    # Return
    return new_sequence
