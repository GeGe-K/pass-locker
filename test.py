import unittest  # Importing the unittest module
from user import User,Credentials  # Importing the user and credentials classes 

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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","20Maroon07") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","20Maroon07") 
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","20Maroon07") 
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","Gloria") # new contact
        test_user.save_user()

        found_user = User.find_by_username("Test")

        self.assertEqual(found_user.username,test_user.username)

    def test_display_all_users(self):
        '''
        returns a list of all users saved 
        '''

        self.assertEqual(User.display_user(), User.user_list)

class TestCredentials(unittest.TestCase):
    '''
    Test class that define test cases for the credentials class behaviour.

    Args:
        unittest.TestCase: TestCase class that helps in cresting test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Git","GeGe-K","2012bfc") #Create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"Git")
        self.assertEqual(self.new_credentials.username,"GeGe-K")
        self.assertEqual(self.new_credentials.password,"2012bfc")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # Saving the new credentials

    def tearDown(self):
        '''
        tearDown method that does clean up after each test has been run
        '''  
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        '''
        method that checks if we can save multiple credentials objects to credentials_list
        '''  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","Gloria Givondo","thegram")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        tests if we can delete a credential from our credentials list
        '''  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","Gloria Givondo","thegram")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #Deletes credentials object
        self.assertEqual (len(Credentials.credentials_list),1)

    def test_find_credentials_by_account(self):
        '''
        Test to check if we can find a credential by the account name and display more information about it
        '''  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","Gloria Givondo","thegram")
        test_credentials.save_credentials()

        found_credentials =Credentials.find_by_account("Instagram")
        self.assertEqual(found_credentials.password,test_credentials.password)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram", "Gloria Givondo", "thegram")
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Instagram")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        returns a list of all credentials saved 
        '''  

        self.assertEqual( Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()
