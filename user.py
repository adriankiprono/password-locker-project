class User:#class that generates instances of user

    user_list=[]  # empty user list variable
    def __init__(self,first_name,last_name,email,password,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.phone_number=phone_number
        '''
        the _init_ method defines the properties of our
        objects
        '''
    def save_user(self):
        '''
        function save user and save_user method saves user object and 
        places it user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        function to delete the user object from the user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_email(cls,email,password):
        '''
        Method that takes in a email and password and returns a contact that matches that email.
        Args:
            email: email  to search for
        Returns :
            Contact of person that matches the number
        '''
        for user in cls.user_list:
            if user.email==email and user.password==password:
                return user
class Credential:# class that generates instances of credential object
    credential_list=[]# empty credential list class varaible
    def __init__(self,user_name,password,account_name):
        self.user_name=user_name
        self.password=password
        self.account_name=account_name
        '''
        the init method defines the properties of our
        objects
        '''
    def save_credential(self):
        '''
        function to save credential in the credential_list
        '''
        Credential.credential_list.append(self)
    def delete_credential(self):
        '''
        function to delete the object from the list 
        '''
        Credential.credential_list.remove(self)
    








    





