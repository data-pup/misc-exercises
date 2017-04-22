import copy

class Py_stack:

    # Initializers
    # ----------------------------------------------------------------------- #
    def __init__(self):
        self._my_list = []


    # Mutating methods
    # ----------------------------------------------------------------------- #
    # Stack push method
    # OUTPUT: N/A
    def push( self, push_value ):
        '''Places push_value at the top of the stack.'''
        self._my_list.append( copy.deepcopy(push_value) )


    # Stack pop method
    # OUTPUT: Pop off the top of the stack, or return None
    # if the stack is empty.
    def pop( self ):
        '''The pop method returns the value at the top of the stack,
            or None if the stack is empty. This element is removed from
            the stack.'''

        # Return None in the case of an empty stack.
        if len(self._my_list) == 0:
            return None
        else:
            # Find the last element in the array, remove it from the stack,
            # and return that value. NOTE: Use the top function to do this.
            # XXX XXX TODO Broken. Set variable to top index, go from there.
            my_top_value = self._my_list.pop( len(self._my_list)-1 )
            return my_top_value


    # Stack clear method
    # OUTPUT: N/A
    def clear( self):
        '''The clear method clears the stack of its contents.'''
        self._my_list.clear()


    # Stack fill method
    # OUTPUT: N/A
    def fill(self, supplied_list):
        '''This method will fill the stack with the contents of a list.
            Note that the bottom of the stack is at index 0.'''
        self._my_list = copy.deepcopy(supplied_list)


    # Accessors
    # ----------------------------------------------------------------------- #
    # Stack top method
    # OUTPUT: The top of the stack, or None if the stack is empty.
    def top( self ):
        '''The top method returns the value at the top of the stack,
            without removing the value from the stack. Returns None if the
            stack is empty.'''

        # Return None in the case of an empty stack.
        if len(self._my_list) == 0:
            return None
        else:
            return self._my_list[ len(self._my_list)-1 ]


    # Stack count method
    # OUTPUT: An integer value, representing the number of
    # elements in the stack.
    def count( self ):
        '''The count method returns an integer value, representing
            the number of elements in the stack..'''
        return len(self._my_list)


    # Empty check method
    # OUTPUT: True if self.count() == 0, False otherwise.
    def isEmpty(self):
        '''This method returns True if the stack is empty, and returns
            False otherwise.'''
        if self.count() > 0:
            return False
        else:
            return True
