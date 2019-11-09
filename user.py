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





