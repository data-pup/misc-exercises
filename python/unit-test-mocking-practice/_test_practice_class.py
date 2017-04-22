import unittest
from unittest import mock

import practice_class

class MyMockClassTestCase(unittest.TestCase):
  '''This is the test bench for the MyMockClass.'''

  def test01_original_call_and_mock_call(self):
    '''This is a basic example of calling a method and checking the result,
      and performing the same process after attaching a mock object.'''

    # Define the correct answers for the original and mock functions.
    # [Use these to check if the returned values were correct.]
    original_function_return_val = 'I called the original function!'
    mock_function_return_val = 'I called the mock function!'

    # Create an instance of the MyMockClass, and then invoke the method.
    test01_practice_class = practice_class.MyMockClass()
    my_return_val = test01_practice_class.my_method()
    self.assertEqual(original_function_return_val, my_return_val)

    # Next, let's create a mock of the function.
    test01_mock_function= mock.Mock()
    test01_mock_function.return_value = mock_function_return_val
    test01_practice_class.my_method  = test01_mock_function

    # Call the method again, and check that we returned the mock value.
    my_return_val = test01_practice_class.my_method()
    self.assertEqual(mock_function_return_val, my_return_val)



def patched_my_method(self):
  return 'I called the helper function!'

@mock.patch('practice_class.MyMockClass.my_method', patched_my_method)
class PatchedMyMockClassTestCase(unittest.TestCase):

  def test02_mocking_with_a_helper_funciton(self):
    '''This test will define a helper function, and use the helper function
      as a mock for the MyMockClass method. Check the result after calling.'''

    helper_function_return_val = 'I called the helper function!'

    test02_practice_class = practice_class.MyMockClass()
    my_return_val = test02_practice_class.my_method()

    self.assertEqual(helper_function_return_val, my_return_val)


# Invoke main:
if __name__ == '__main__':
  unittest.main()
