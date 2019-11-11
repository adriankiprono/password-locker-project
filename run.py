#!/usr/bin/env python3.8

from user import User #import the user class
from user import Credential #import the credential class
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
def random_password():
    '''
    function to generate random random
    '''
    return password_character
def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new user ,du - display user, fu -find a user, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print ("first_name ....")
            first_name = input()

            print("last_name ...")
            last_name = input()

            print("email ...")
            phone_number = input()

            print("password ...")
            password = input()

            print(" phone_number...")
            email = input()


            save_user(create_user(first_name,last_name,email,password,phone_number)) # create and save new contact.
            print ('\n')
            print(f"New user {first_name} {last_name}  {email}created")
            print ('\n')

        elif short_code == 'du':

            if display_user():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_user():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'fu':

            print("Enter the number you want to search for")

            search_email = input()
            if check_existing_user(search_email):
                search_user = find_user(search_email)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That contact does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    
    main()






