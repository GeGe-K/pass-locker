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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # Saving the new user
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()