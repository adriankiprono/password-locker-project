#!usr/bin/env python3.8

from user import User #import the user class
from user import Credential #import the credential class
def create_user(first_name,last_name,email,password,phone_number):
    '''
    function to create a new user
    '''
    new_user=User(first_name,last_name,email,password,phone_number)
    return new_user

