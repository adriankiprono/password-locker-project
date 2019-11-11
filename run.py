#!usr/bin/env python3.8

from user import User #import the user class
from user import Credential #import the credential class
def create_user(first_name,last_name,email,password,phone_number):
    '''
    function to create a new user
    '''
    new_user=User(first_name,last_name,email,password,phone_number)
    return new_user
def save_user(first_name,last_name,email,password,phone_number):
    '''
    function to save user
    '''
    user.save_user
def delete_user(user):
    '''
    function to delete user
    '''
    user.delete_user
def find_user(email,password):
    '''
    function to find user
    '''
    return User.find_by_email(email,password)
def create_credential(user_name,password,account_name):
    '''
    function to create credential
    '''
    new_credential=Credential(user_name,password,account_name)
    return new_credential
def save_credential(credential):
    '''
    function to save credential
    '''
    credential.save_credential()


