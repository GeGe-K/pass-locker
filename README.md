# Password Locker

## Autour

### *Gloria Givondo* (2018/11/02)

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display guides for navigation | **In terminal: $./run.py** | Hello, welcome to your Password Locker. What is your name? (once you enter your name):Use these known short codes to operate :  cu-> Create new user. si -> Sign in.  ex ->exit Password Locker.|
| Display prompt for creating an account | **Enter: cu** | Enter username and password.|
| Display prompt for login in | **Enter: si** | Enter your account username password to login |
| Once logged in | **Welcome to your  account** |  Use these short codes:cc -> Create new credential. fa -> Find credentials. da -> Delete credentials. dc -> Display your credentials list.  ex ->Log Password Locker. |
| Display prompt for creating a credential | **Enter: cc** | Create new credentials, account, username and password |
|Display prompt for finding credentials |**Enter: fa**| Find credentials, account, username and password|
| Display prompt for deleting credentials |**Enter: da**|Once the account is selected **Your Instagram credentials have been successfully been deleted**|
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Log out account  | **Enter: ex** | Exit password locker |

* To completely interact with this application,you will need to sign up to have an account,then login to your account and work in there.

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* Git


### Cloning
* In your terminal:
        
        $ git clone https://github.com/GeGe-K/pass-locker.git 
         $ cd pass-locker 

## Running the Application
* To run the application, in your terminal:

       $ chmod +x run.py (to make it executable)
       $ ./run.py 
      
        
## Testing the Application
* To run the tests for the class file and check if it functions well:

        $ python3.6 test.py 
        
## Technologies Used
* Python3.6
* Visual Studio Code text editor

## Known Bugs

There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**
