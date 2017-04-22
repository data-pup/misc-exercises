# This is a unittest test suite, to run tests on the py_stack class.
# NOTE: test method names begin 'test*'

import unittest
import py_stack

class PyStackTestCase(unittest.TestCase):

    def testConstructorDefault(self):
        my_stack = py_stack.Py_stack()


# These tests check the push(value) method.
# --------------------------------------------------------------------------- #
    def testPushIntegers(self):
        # Construct the stack class, and a list of values to
        # push to the stack.
        py_stack_testPushIntegers = py_stack.Py_stack()
        testPushIntegers_values = [1, 2, 3]

        # Push each value in testPushIntegers_values into the stack.
        for push_value in testPushIntegers_values:
            py_stack_testPushIntegers.push(push_value)

        # Check that the values have been pushed onto the stack.
        self.assertEqual( py_stack_testPushIntegers._my_list,
            testPushIntegers_values)

        # Clear the stack. Check that the list has been cleared.
        py_stack_testPushIntegers.clear()
        self.assertEqual(len(py_stack_testPushIntegers._my_list),0)


    def testPushFloats(self):
        # Construct the stack class, and a list of values to
        # push to the stack.
        py_stack_testPushFloats = py_stack.Py_stack()
        testPushFloats_values = [1.0, 2.0, 3.0]

        self.assertEqual(len(py_stack_testPushFloats._my_list),0)

        # Push each value in testPushFloats_values into the stack.
        for push_value in testPushFloats_values:
            py_stack_testPushFloats.push(push_value)

        # Check that the values have been pushed onto the stack.
        self.assertEqual(py_stack_testPushFloats._my_list,testPushFloats_values)

        # Clear the stack. Check that the list has been cleared.
        py_stack_testPushFloats.clear()
        self.assertEqual(len(py_stack_testPushFloats._my_list),0)


    def testPushNone(self):
        # This is a test to see what happens if a null value is passed as
        # a parameter to the py_stack's push function.
        # NOTE: This stack can hold a None value! As long as a parameter
        # is supplied that is equal to None. stack.push() would fail.
        py_stack_testPushNone = py_stack.Py_stack()
        testPushNone_values = [None, None, None]

        # Push each value in testPushNone_values into the stack.
        for push_value in testPushNone_values:
            py_stack_testPushNone.push(push_value)

        # Check that the values have been pushed onto the stack.
        self.assertEqual(py_stack_testPushNone._my_list,testPushNone_values)

        # Clear the stack. Check that the list has been cleared.
        py_stack_testPushNone.clear()
        self.assertEqual(len(py_stack_testPushNone._my_list),0)


# These tests check whether the pop() method works.
# --------------------------------------------------------------------------- #
    def testPopEmpty(self):
        # This test makes sure that calling pop() on an empty stack does not
        # fail. pop() should return None if called on an empty stack.
        py_stack_testPopEmpty = py_stack.Py_stack()
        my_pop_value_testPopEmpty = py_stack_testPopEmpty.pop()

        # Check that the length is still 0, and check that
        # my_pop_value_testPopEmpty == None.
        self.assertEqual(len(py_stack_testPopEmpty._my_list),0)
        self.assertEqual(my_pop_value_testPopEmpty,None)


    def testPopReverse(self):
        # This test checks the functionality of reversing an array by using
        # push and pop. Push each element of a list into a stack, and pop them
        # off of the stack until it is empty. The original list should be
        # reversed after this.
        py_stack_testPopReverse = py_stack.Py_stack()
        my_value_list_testPopReverse = [1, 2, 3, 4, 5]
        my_new_value_list_testPopReverse = []

        # Push the elements in the list into the stack.
        for my_value_testPopReverse in my_value_list_testPopReverse:
            py_stack_testPopReverse.push(my_value_testPopReverse)

        # Call pop() until the stack is empty.
        while py_stack_testPopReverse.isEmpty() == False:
             my_new_value_list_testPopReverse.append(py_stack_testPopReverse.pop())

        # Assert that the new value list is the reverse of the original.
        my_value_list_testPopReverse.reverse()
        self.assertEqual(my_value_list_testPopReverse,
            my_new_value_list_testPopReverse)


# These tests check whether the fill(supplied_list) method works.
# --------------------------------------------------------------------------- #
    def testFillEmpty(self):
        # This test checks that the fill method can handle an empty list.
        my_value_list_testFillEmpty = []
        py_stack_testFillEmpty = py_stack.Py_stack()

        py_stack_testFillEmpty.fill(my_value_list_testFillEmpty)

        self.assertListEqual(py_stack_testFillEmpty._my_list,
            my_value_list_testFillEmpty)


    def testFill(self):
        # This test checks that the fill method can handle a list of integers.
        my_value_list_testFill = [1, 2, 3]
        py_stack_testFill = py_stack.Py_stack()

        # Fill the stack with the list of integers.
        # Check that the stack is equal to the supplied list.
        py_stack_testFill.fill(my_value_list_testFill)
        self.assertListEqual(py_stack_testFill._my_list,
            my_value_list_testFill)

        # Pop off the top value, check that it is correct. The top value
        # should be equal to the last element in the value list.
        my_pop_value_testFill = py_stack_testFill.pop()
        self.assertEqual(my_pop_value_testFill,
            my_value_list_testFill[len(my_value_list_testFill)-1])


# These tests check whether the clear() method works.
# NOTE: This is implied by the tests above, (some use the clear() method)
# but these are included to be thorough.
# --------------------------------------------------------------------------- #
    def testClear(self):
        # Fill the stack with a list of integers. This is assuming the tests
        # above on the fill() method work correctly.
        my_value_list_testClear = [1, 2, 3]
        py_stack_testClear = py_stack.Py_stack()
        py_stack_testClear.fill(my_value_list_testClear)

        # Invoke the clear() method, and check that it emptied the stack.
        py_stack_testClear.clear()
        self.assertTrue( len(py_stack_testClear._my_list) == 0)

        # Make sure that the clear() method works when called again as well,
        # after the list is emptied.
        py_stack_testClear.clear()
        self.assertTrue( len(py_stack_testClear._my_list) == 0)


# These tests check whether the accessor methods work correctly.
# These include top(), count(), and isEmpty()
# --------------------------------------------------------------------------- #
    def testAccessorsEmpty(self):
        # This test is designed to check that the accessors all
        # work correctly on an empty stack made using the default initializer.
        py_stack_testAccessorsEmpty = py_stack.Py_stack()

        # Check that top() == None, count() == 0, isEmpty() == True
        self.assertIsNone( py_stack_testAccessorsEmpty.top() )
        self.assertEqual( py_stack_testAccessorsEmpty.count(), 0)
        self.assertTrue( py_stack_testAccessorsEmpty.isEmpty() )


    def testAccessors(self):
        # This test is designed to check that the accessors all
        # work correctly on an empty stack made using the default initializer.
        py_stack_testAccessors = py_stack.Py_stack()

        py_stack_testAccessors.push(1)
        py_stack_testAccessors.push(2)
        py_stack_testAccessors.push(3)
        py_stack_testAccessors.push(4)
        py_stack_testAccessors.push(5)

        # Check that top() == None, count() == 0, isEmpty() == True
        self.assertEqual( py_stack_testAccessors.top(), 5)
        self.assertEqual( py_stack_testAccessors.count(), 5)
        self.assertFalse( py_stack_testAccessors.isEmpty() )


# Invoke testing
# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    unittest.main()
