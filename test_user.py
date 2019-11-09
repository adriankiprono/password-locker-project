import unittest # getting the unittest module
from user import User #import the user class

class TestUser(unittest.TestCase):
    '''
    the subclass of the unittest module that defines
    the test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User("king","kong","king@gmail.com","qweasdzxc","0712345678")# create contact object
        
    def test_init(self):
        '''
        function test_init test case if the object correctly 
        initialized
        '''
        self.assertEqual(self.new_user.first_name,"king")
        self.assertEqual(self.new_user.last_name,"kong")
        self.assertEqual(self.new_user.email,"king@gmail.com")
        self.assertEqual(self.new_user.password,"qweasdzxc")
        self.assertEqual(self.new_user.phone_number,"0712345678")
    def test_save_user(self):
        '''
        function test_save test case to see if the user object is on the 
        user list
        '''
        self.new_user.save_user()# saving the user the user object
        self.assertEqual(len(User.user_list),1)
    # def test_save_mulliple_user(self):
    #     '''
    #     the function test case to check if we save multiple
    #     user object in our user_list
    #     '''
    #     self.new_user.save_user()# saving the user object
    #     self.assertEqual(len(User.user_list),2)
    def tearDown(self):
        '''
        this method clears each test case has run
        '''
        User.user_list=[]
    def test_save_mulliple_user(self):
        '''
        the function test case to check if we save multiple
        user object in our user_list
        '''
        self.new_user.save_user()# saving the user object
        test_user=User("king","kong","king@gmail.com","qweasdzxc","0712345678")# new user object
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    



if __name__=='__main__':
    unittest.main()