class User:
    """
    Class that generates new instances of users.
    """

    user_list = []  # empty account user list

    # Init method
    def __init__(self,username,password):

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
    def find_by_username(cls,name):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            name: Username to search for
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
            name: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.password == name:
                    return True

        return False
    
    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list  
    
    # @ classmethod
    # def copy_email(cls,number):
    #     user_found = User.find_by_name(name)
    #     pyperclip.copy(User_found.email)