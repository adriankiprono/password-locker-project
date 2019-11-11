#!/usr/bin/env python3.8

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
def save_credential(user_name,password,account_name):
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






    # if short_code == 'cu':
    #     print("New User")
    #     print("-"*10)

    #     print ("first_name ....")
    #     first_name = input()

    #     print("last_name ...")
    #     last_name = input()

    #     print("email ...")
    #     phone_number = input()

    #     print("password ...")
    #     password = input()

    #     print(" phone_number...")
    #     email = input()
    #     save_user(create_user(first_name,last_name,email,password,phone_number)) # create and save new contact.
    #     print ('\n')
    #     print(f"New user {first_name} {last_name}  {email}created . thanks for sign in up")
    #     print ('\n')
    #     while True:
    #         print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
    #         short_code = input().lower().strip()
    #         if short_code == "cc":
    #         #     print("Create New Credential")
    #         #     print("."*20)
    #         #     print("Account name ....")
    #         #     account = input().lower()
    #         #     print("Your Account username")
    #         #     userName = input()
    #         #     while True:
    #         #         print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
    #         #         password_Choice = input().lower().strip()
    #         #         if password_Choice == 'tp':
    #         #             password = input("Enter Your Own Password\n")
    #         #             break
    #         #         elif password_Choice == 'gp':
    #         #             password = generate_Password(username)
    #         #             break
    #         #         else:
    #         #             print("Invalid password please try again")
    #         #             save_credential(create_new_credential(account,userName,password))
    #         #             print('\n')
    #         #             print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
    #         #             print('\n')
    #         # elif short_code == "dc":
    #         #     if display_accounts_details():
    #         #         print("Here's your list of acoounts: ")
                    
    #         #         print('*' * 30)
    #         #         print('_'* 30)
    #         #         for account in display_accounts_details():
    #         #             print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
    #         #             print('_'* 30)
    #         #             print('*' * 30)
    #         #         else:
    #         #             print("You don't have any credentials saved yet..........")
    #         # elif short_code == "fc":
    #         #     print("Enter the Account Name you want to search for")
    #         #     search_name = input().lower()
    #         #     if find_credential(search_name):
    #         #         search_credential = find_credential(search_name)
    #         #         print(f"Account Name : {search_credential.account}")
    #         #         print('-' * 50)
    #         #         print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
    #         #         print('-' * 50)
    #         #     else:
    #         #         print("That Credential does not exist")
    #         #         print('\n')
    #         # elif short_code == "d":
    #         #     print("Enter the account name of the Credentials you want to delete")
    #         #     search_name = input().lower()
    #         #     if find_credential(search_name):
    #         #         search_credential = find_credential(search_name)
    #         #         print("_"*50)
    #         #         search_credential.delete_credential()
    #         #         print('\n')
    #         #         print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
    #         #         print('\n')
    #         #     else:
    #         #         print("That Credential you want to delete does not exist in your store yet")

            

    #         # elif short_code == 'du':

    #         #     if display_user():
    #         #         print("Here is a list of all your user")
    #         #         print('\n')

    #         #         for user in display_user():
    #         #             print(f"{user.first_name} {user.last_name} {user.email}")

    #         #             print('\n')
    #         #     else:
            #         print('\n')
            #         print("You dont seem to have any contacts saved yet")
            #         print('\n')

            # elif short_code == 'fu':

            #     print("Enter the email you want to search for")

            #     search_email = input()
            #     if check_existing_user(search_email):
            #         search_user = find_user(search_email)
            #         print(f"{search_contact.first_name} {search_contact.last_name}")
            #         print('-' * 20)

            #         print(f"Phone number.......{search_user.phone_number}")
            #         print(f"Email address.......{search_user.email}")
            #     else:
            #         print("That contact does not exist")
        
    # elif short_code == "ex":

    #     print("Bye .......")
    #     break
    # else:
    #     print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()



        




