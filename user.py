class User:
    '''
    Class that generates new instances of users.
    '''

    user_list = []  # empty account user list

    # Init method
    def __init__(self,username,password):

        '''
        Initialises the user
        '''

        self.username = username
        self.password = password
    
    def save_user(self):

        '''
        save_user method saves user objects into user_list 
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''
  
        User.user_list.remove(self) 

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: Username to search for
        Returns :
            Username of person that matches the name.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user  

    @classmethod
    def user_exist(cls,name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False
    
    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list  

class Credentials:
    '''
    Class that generates new instances of the user's credentials
    '''

    credentials_list = []  # Empty credentials list

    # Init method
    def _init_(self,account,username,password):

        '''
        Initialises the user's credentials
        '''

        self.account = account
        self.username = Username
        self.password = password
        self.email = email

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list 
        '''

        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self) 

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in an account and returns credentials that matches that account.

        Args:
            account: account to search for
        Returns :
            credentials of person that matches the account.
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def credentials_exist(cls,account):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            account: account to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list 
    
    # @ classmethod
    # def copy_email(cls,number):
    #     user_found = User.find_by_name(name)
    #     pyperclip.copy(User_found.email)