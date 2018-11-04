import unittest  # Importing the unittest module
from user import User  # Importing the user class 

class TestUser(unittest.TestCase):
    '''
    Test class that define test cases for the user class behaviour.

    Args:
        unittest.TestCase: TestCase class that helps in cresting test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gloria","maroon") #Create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Gloria")
        self.assertEqual(self.new_user.password,"maroon") 
        
if __name__ == '__main__':
    unittest.main()