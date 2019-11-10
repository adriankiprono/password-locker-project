import unittest # getting the unittest module
from user import User #import the user class
from user import Credential #import the credential class

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
    def test_delete_user(self):
        '''
        the test_del_user test case to check if we deleted the user object in the
        user _list
        '''
        self.new_user.save_user()# saving the user object 
        test_user=User("king","kong","king@gmail.com","qweasdzxc","0712345678")# new contact object
        test_user.save_user()

        self.new_user.delete_user()# deleting the user object
        
        self.assertEqual(len(User.user_list),1)
    def test_find_user(self):
        '''
        test case to check if a user can be found email 
        and display the information
        '''
        self.new_user.save_user()
        test_user=User("king","kong","king@gmail.com","qweasdzxc","0712345678")
        test_user.save_user()

        found_user=User.find_by_email("king@gmail.com","qweasdzxc")
        
        self.assertEqual(found_user.email,test_user.email)
class TestCredential(unittest.TestCase):
    '''
    class for test case that check the behaviours of the credential class
    '''
    def setUp(self):
        '''
        set up method to run before each test case
        '''
        self.new_credential=Credential("kingkong","qweasdzxc","facebook")
    def test_init_credential(self):
        '''
        to test if the credential object is prpperly initilize
        '''
        self.assertEqual(self.new_credential.user_name,"kingkong")
        self.assertEqual(self.new_credential.password,"qweasdzxc")
        self.assertEqual(self.new_credential.account_name,"facebook")
    def test_save_credential(self):
        '''
        function to test if we can save the credential in credential list
        '''
        self.new_credential.save_credential()# method that saves the credential object
        self.assertEqual(len(Credential.credential_list),1)
    def tearDown(self):
        '''
        setdown method if clear each test case after they have run
        '''
        Credential.credential_list=[]#empty 
    def test_delete_credential(self):
        '''
        function for  test case to see if we can delete the 
        credential object from credential list
        '''
        self.new_credential.save_credential()
        test_credential=Credential("kingkong","qweasdzxc","facebook")
        self.new_credential.delete_credential()# deleting the credential object from the list
        self.assertEqual(len(Credential.credential_list),0)
    def test_find_credential(self):
        '''
        function for test case to test if we can find the credential object from the list
        '''
        self.new_credential.save_credential()
        test_credential=Credential("kingkong","qweasdzxc","facebook")
        test_credential.save_credential()

        find_credential=Credential.find_by_user_name("kingkong")
        self.assertEqual(find_credential.user_name,test_credential.user_name)
    
    



    



if __name__=='__main__':
    unittest.main()