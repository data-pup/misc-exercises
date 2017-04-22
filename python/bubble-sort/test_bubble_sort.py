# Test the bubble sort function defined in the my_bubble_sort.py module

# TODO: Finish the memory testing function. This should first
# Declare an array, using a list, and then delete the list. Check that
# This does not delete the elements in the array.
#
# Then, try the same thing and alter values in one object or another.
#     TODO: Subgoal for this should be to write a method that
#           will print the original and new arrays in individual lines.
#           (This will be helpful for demonstrating the sort process.)
# --------------------------------------------------------------------------- #

# Library imports.
# --------------------------------------------------------------------------- #
import unittest
import my_bubble_sort
import random

# Helper functions:
# --------------------------------------------------------------------------- #

# This function will print each list of data using formatted output.
def print_each_array(original_data, new_data):

    # Print the original list.
    print("Original list:")
    print(original_data)

    # Print the new list.
    print("New list:")
    print(new_data)

# This function will print a line of hyphens, for output formatting.
def print_hyphen_line():
    for i in range(80):
        print("-",end="")
    print("")

# Create a random string of values
# INPUT: size of list, minimum element value, maximum element value
# OUTPUT:
#   my_list : a list containing randomly
#   generated integers where a <= x <= b.
def create_a_random_list(size_of_list,min_rand_value,max_rand_value):
    random.seed()
    my_list = []

    # Fill the list with randomly generated values within the given range.
    for i in range(size_of_list):
        my_list.append(random.randint(min_rand_value,max_rand_value))

    # Return the list
    return my_list

# This is the test class for my bubble sort function.
# --------------------------------------------------------------------------- #
class PyBubbleSortTestCase(unittest.TestCase):

    # Test 01:
    # This tests the bubble sort function, with a simple example.
    # The purpose of this function is to make sure that the return object
    # is not allocated using a shallow copy. Make edits to the list and
    # see that each list behaves differently.
    def test01_deepcopy_check(self):
        print("Test 01 beginning...")
        print_hyphen_line()

        original_list = [1, 2, 3]
        new_list = my_bubble_sort.my_bubble_sort(original_list)

        print_each_array(original_list, new_list)
        self.assertEqual(original_list, new_list)

        print("Making edits...")
        original_list[0] = 0
        new_list[0] = 4
        correct_original_list_edit = [0,2,3]
        correct_new_list_edit = [4,2,3]

        self.assertEqual(original_list, correct_original_list_edit)
        self.assertEqual(new_list, correct_new_list_edit)

        print("After edits:")
        print_each_array(original_list, new_list)
        print_hyphen_line()

    # This function runs a basic sort example on a 3-element array.
    # Use the built-in sort method from the list class to check that
    # the bubble_sort function returned a correct result.
    def test02_basic_sort_test(self):
        print("Test 02 beginning...")
        print_hyphen_line()

        original_list = [1, 3, 2]
        new_list = my_bubble_sort.my_bubble_sort(original_list)
        print_each_array(original_list, new_list)

        original_list.sort()
        self.assertEqual(original_list, new_list)
        print_hyphen_line()

    # This test will alphabetize the words in a lorem ipsum paragraph.
    def test03_sort_lorem_ipsum(self):
        print("Test 03 beginning...")
        print_hyphen_line()
        my_string = 'lorem ipsum dolor sit amet consectetur adipiscing elit'
        my_words = my_string.split(sep=" ")
        my_sorted_words = my_bubble_sort.my_bubble_sort(my_words)
        my_words.sort()
        self.assertEqual(my_words, my_sorted_words)
        print(my_sorted_words)
        print_hyphen_line()

    # This function will test the sorting function on a
    # randomly generated list. Note that this uses the random library.
    def test04_sort_randomly_generated_list(self):
        print("Test 04 beginning...")
        print_hyphen_line()
        # Sequence parameters
        size_of_list = 100
        min_rand_value = 0
        max_rand_value = 100
        my_list = create_a_random_list(size_of_list,min_rand_value,max_rand_value)
        my_sorted_list = my_bubble_sort.my_bubble_sort(my_list)
        print_each_array(my_list,my_sorted_list)
        my_list.sort()
        self.assertEqual(my_list,my_sorted_list)
        print_hyphen_line()

    # Check that this function will not raise an exception
    # if called on an empty list object.
    def test05_test_call_on_empty_object(self):
        print("Test 05 beginning...")
        print_hyphen_line()
        my_list = []
        my_sorted_list = my_bubble_sort.my_bubble_sort(my_list)
        print_hyphen_line()



# --------------------------------------------------------------------------- #
# Invoke the test suite.
if __name__ == '__main__':
    unittest.main()
