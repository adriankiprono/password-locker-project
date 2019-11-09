class User:#class that generates instances of user

    User_list=[]  # empty user list variable
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



