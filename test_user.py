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

if __name__=='__main__':
    unittest.main()