import hashlib
import re
import os
from Utils import overrides
from PyQt5.QtWidgets import QMessageBox
userData = 'UserInfo.txt'

'''
Utility function to hash a password. Used by Authenticator and AccountCreator
'''
def hash_pass(password):
    encodedPass = str(password).encode('utf-8')
    hashedPass = hashlib.md5(encodedPass).hexdigest()
    return hashedPass
        
'''
Authenticator: Holds credentials and provides functions to check validity of the credentials
'''
class Authenticator():
    def __init__(self, username, password):
        self.username = str(username)
        print(self.username)
        self.password = str(password)  
        self.hashedPass = hash_pass(self.password)
        self.return_string = ''

    '''
    Uses username and raw password combo from the UI form and checks with the MySQL server to make sure user entered correct credentials
    Returns True iff hashed password and username matches database combination
    '''
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword():
            # Connect to the MySQL server and check username + password combo
            # If authenticated, return true and set session token
            print("Valid credentials") #Remove this once the above part is implemented
            return True
        else:
            print("Invalid credentials")  #Remove this once the above part is implemented
            return False

    def isValidUsername(self):
        print(self.username)
        if len(self.username) < 3 or len(self.username) > 16:
            self.return_string = "Invalid Username"
            return False
        return True

    def isValidPassword(self):
        print(self.password)
        if len(self.password) < 8 or len(self.password) > 64:
            self.return_string = "Invalid Password"
            return False
        return True
        

'''
This will take data from the create_account UI form, which already contains login credentials for future user
'''
class AccountCreator(Authenticator):
    def __init__(self, username, password, re_password, email):
        super().__init__(username, password)
        self.re_password = str(re_password)
        self.email = str(email)
     
    
    @overrides(Authenticator)
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword() and self.isValidEmail():
            #Connect to DB, create new user, setup table
            return True, 'Valid'
        else:
            return False, self.return_string

    @overrides(Authenticator)
    def isValidPassword(self):
        if super().isValidPassword():
            if (self.password == self.re_password):
                return True
            else:
                self.return_string = "Passwords don't match"
                return False
        else:
            return False

    def isValidEmail(self):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            self.return_string = "Invalid Email"
            return False
        return True
