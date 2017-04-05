'''This is a quine implemented in Python. When executed, this program will
print its own source code.'''

import os

# Define the main function.
def main():
    '''This is the main function.'''
    # Use the os module to find the current working directory.
    my_cwd = os.getcwd()
    # Concatenate the name of this file to the end of the current working directory.
    my_filename = 'quine.py'
    my_filepath = my_cwd + '/' + my_filename
    # Open the file, and print the contents of the stream to stdout.
    my_stream = open(my_filepath, 'r')
    print(my_stream.read())

# If called directly, invoke the main function.
if __name__ == '__main__':
    main()
