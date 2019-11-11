#! /usr/bin/env python3.8

from user import User #import the user class
from user import Credential #import the credential class
import string
import random

def create_user(first_name,last_name,email,password,phone_number):
    '''
    function to create a new user
    '''
    new_user=User(first_name,last_name,email,password,phone_number)
    return new_user
def save_user(user):
    '''
    function to save user
    '''
    User.save_user(user)
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def delete_user(user):
    '''
    function to delete user
    '''
    User.delete_user()
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


def delete_credential(credential):
    '''
    function to delete credential
    '''
    credential.delete_credential()
def find_credential(user_name):
    '''
    function to find credential
    '''
    return Credential.find_by_user_name(user_name)
def display_credential():
    '''
    function to display all credential
    '''
    return Credential.display_credential
def copy_credential(cls):
    '''
    function to copy credential
    '''
    return Credential.copy_credential(password)
def random_password(pass_len):
    '''
    generates a random password for the user.
    '''
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(pass_len))
    
    
def main():
    print("Hello Welcome to your password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    
    print("do  you want a new account user or do you have one already  \n 1 \n 2")
    short_code = input().lower()

    if short_code =='1':
       
        print("New User")
        print("-"*10)

        print ("first_name ....")
        first_name = input()

        print("last_name ...")
        last_name = input()

        print("phone_number ...")
        phone_number = input()

        print("email ...")
        email = input()


        while True:

            print("do you want to a scp -secured password  \n ucp -do you want to create your own")
            password_option=input().lower().strip()
            if password_option=='ucp':
                password = input("enter your password")
                break
            elif password_option =='scp':
                print("how long do you want you password to be ?")
                pass_len = int(input())
                password=random_password(pass_len)
                break
            else:
                print("invalid choice please select from the option")
        save_user(create_user(first_name,last_name,email,password,phone_number))
        print("*"*85)
        print(f"Hello {first_name},{last_name},{email} Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "2":
        print("*"*50)
        print("Enter your first_name and your Password to log in:")
        print('*' * 50)
        first_name = input("first_name: ")
        password = input("password: ")
        login = login_user(first_name,password)
        if login_user == login:
            print(f"Hello {first_name}.Welcome To your  user  account")  
            print('\n')
        
        else:
            print(f"Sorry we could not find your account. try again")
            print("\n")
    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n scp - Generate A  secure randomn password \n de - Delete credential \n EX -  to Exit  \n")
        short_code = input()
        if short_code=='cc':
            print("account_name")
            account_name=input()
            print("\n")
            print("user_name")
            user_name=input()
            print("\n")
            print("password")
            while True:
    
                print("do you want to a scp -secured password  \n ucp -do you want to create your own")
                password_option=input().lower().strip()
                if password_option=='ucp':
                    password = input("enter your password")
                    break
                elif password_option =='scp':
                    print("how long do you want you password to be ?")
                    pass_len = int(input())
                    password=random_password(pass_len)
                    break
            else:
                print("invalid choice please select from the option")
        save_credential(create_credential(user_name,password,account_name))
        print(f"Hi! there . here is your credential {account_name}{user_name}{password}")
        elif short_code=='dc':
            if display_credential():
                print("here is a list of all accounts")


            
    
    





if __name__ == '__main__':
    main()



        




