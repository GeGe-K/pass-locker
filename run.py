#!/usr/bin/env python3.6
from user import User,Credentials

# creating user
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User (username,password)
    return new_user

# save user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

# delete user
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

# find user
def find_user(username):
  '''
  Function that finds a user by username and returns the user
  '''
  return User.find_by_username(username)

# existing user
def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return  User.user_exists(username)

# displaying user
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def create_credentials(account,username,password):
    '''
    Function that creates a new credential
    '''
    new_credentials = Credentials (account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    saves a credential
    '''
    credentials.save_credentials()


def delete_credentials(account):
    '''
    deletes a credential
    '''
    Credentials.delete_credentials(account)

def find_credentials(account):
    '''
    finds a credential by account and returns the credentials
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    checks if a credential exists with that account and returns a Boolean value
    '''
    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    returns all saved credentials
    '''
    return Credentials.display_credentials()



def main():
    print("Hello, welcome to your Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: cu - create a new user, li - log in to your account, dc - display credentials, fa - find account, fu - find a user, cc- create new credentials, da- delete account, ex - exit password locker")
        in_short_code = input().lower()


        if in_short_code == 'cu':
            print("Create a new account by following the steps below:")
            print("Enter any username you wish to use for your account")
            username = input()
            print("Enter password:")
            password = input()

            save_users(create_user(username,password))
            print('\n')
            print(f"Thank you {username}, you may now proceed to open up your account")
            print('\n')

        elif in_short_code == 'si':
          print('\n')
          print("Enter your account username:")
          username =input()
          print("Enter Password:")
          password=input()
          if check_existing_users(username):
            saved_user = find_user(username)  
            print(f"Welcome to your account {saved_user.username}")  
            print('\n')

        elif in_short_code =='ex' :
            print("Try again later,Goodbye!...")
            break
            
        elif in_short_code == 'cc':
                        print('\n')
                        print("Follow the following steps to create new credentials;")
                        print('\n')
                        print("Enter the account i.e Instagram/Facebook/Twitter")
                        account=input()
                        print("Enter your username for the new account:")
                        username=input()
                        print("Enter password:")
                        password=input()
                        save_credentials(create_credentials(account,username,password))
                        print('\n')
                        print(f"You have successfully created new credentials for your new {account} account.")
                        print('\n')

        elif in_short_code == 'dc':
                        print('/n')
                        if display_credentials():
                            print("Below is a list of all your credentials:")
                            print('\n')
                            for credential in display_credentials():
                                print(f"Name of Account: {credentials.account}")
                                print(f"Username: {credentials.username}")
                                print(f"Password: {credentials.password}")
                                print('\n')
                        else:
                            print("\n Sorry,You do not have any credentials to display")

        elif in_short_code == 'fa':
          print("Enter name of account you'd wish to search for")
          search_account=input()
          if check_existing_credentials(search_account):
            search_credentials= find_credentials(search_account)
            print(f"Name of the account: {search_account}")
            print(f"Account Username: {search_credentials.username}")
            print(f"Account Password: {search_credentials.password}")

          else:
            print("Sorry,The entered credential does not exist")      

        elif in_short_code == 'da':
          print("Which account do you wish to delete?")
          delete_account=input()
          if check_existing_credentials(delete_account):
            search_delete_credentials= find_credentials(delete_account)
            delete_credentials(search_delete_credentials)

            print(f"Your {delete_account} credentials have been successfully deleted")

          else:
            print("Sorry, credential does not exist")   

        elif in_short_code == 'ex':
          print("Goodbye...")
          break

    else:
           print("Short code not found,Please use the short codes")

       

        
                
if __name__ == '__main__':
    main()
