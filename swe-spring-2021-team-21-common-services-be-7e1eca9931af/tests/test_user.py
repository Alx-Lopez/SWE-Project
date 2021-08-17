from unittest import TestCase, mock
import sys
sys.path.insert(1, '../')
from user import User


class TestUser(TestCase):

    # This will build these users before every test case
    def setUp(self):
        print('setup')

        # Users we regularly use within our test cases
        self.user_new = User('rgrimes@twd.net', 'Rick', 'Grimes')
        self.user_existing = User('larryboy@vt.com')

    # Called after every test case, assuming setUp() was successful
    def tearDown(self):
        print('tearDown\n')

    # Testing that invalid Users cannot be created
    # An exception is raised if someone attempts to create a user
    # with an invalid email format
    def test_invalid_user(self):
        print(f'Testing test_invalidUser')
        # MUST do this when testing exceptions/assertions
        # you will FAIL with exceptions/assertions otherwise
        # Testing that an empty string raises an Exception
        with self.assertRaises(Exception):
            User('')

        # Testing that sending None raises an Exception
        with self.assertRaises(Exception):
            User(None)

        # Testing that sending input that isn't a string
        # raises an Exception
        with self.assertRaises(Exception):
            User(2)
        with self.assertRaises(Exception):
            User(3.33)

        # Testing that sending invalid string values
        # raises an Exception
        with self.assertRaises(Exception):
            User('a')
        with self.assertRaises(Exception):
            User('a@')
        with self.assertRaises(Exception):
            User('a@a')
        with self.assertRaises(Exception):
            User('a@a.')

    # Testing register function
    # This patch will allow us to manage the database response
    # TODO: improve our use of mock
    @mock.patch('user.User.register')
    def test_register(self, mock_pymysql):
        print(f'Testing test_register')

        # Setting up the rest of the patch
        mock_pymysql.return_value = True

        # Trying to register a new user
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.user_new.register('P@ssW0rd'))

        # Setting up the patch for our next tests
        mock_pymysql.return_value = False

        # Trying to re-register our newly created user
        # Our patch should prove that this doesn't work
        # assuming it reaches the database call
        self.assertFalse(self.user_new.register('L337!nSuch'))

        # Trying to register an existing user
        # You cannot register again with an existing user, return False
        self.assertFalse(self.user_existing.register('P@ssW0rd'))

    # Testing login function
    # This patch will allow us to manage the database response
    # TODO: improve our use of mock
    @mock.patch('user.User.login')
    def test_login(self, mock_pymysql):
        print(f'Testing test_login')

        # Setting up the rest of the patch
        mock_pymysql.return_value = True

        # Trying to login with an existing user
        # We are assuming this is the proper password of the user
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.user_existing.login('sillys0NGSwM3!'))

        # Setting up the patch for our next tests
        mock_pymysql.return_value = False

        # Trying to login an existing user with the wrong password
        # Our patch should prove that this doesn't work
        # assuming it reaches the database call
        self.assertFalse(self.user_existing.login('iM@Ba4a4a'))

        # Trying to login a user that is not registered
        self.assertFalse(self.user_new.login('P@ssW0rd'))

    # Testing isValidEmail() class function
    # Technically tested when constructing a User
    # but it doesn't hurt to double down on it
    def test_email(self):
        print(f'Testing test_email')

        # Testing that the email of our valid Users is valid
        self.assertTrue(User.is_valid_email(self.user_new.email))
        self.assertTrue(User.is_valid_email(self.user_existing.email))

        # Testing other valid email syntax
        self.assertTrue(User.is_valid_email('test@test.test'))
        self.assertTrue(User.is_valid_email('a@a.a'))
        self.assertTrue(User.is_valid_email('student@stedwards.edu'))

        # Testing invalid email syntax
        self.assertFalse(User.is_valid_email(''))
        self.assertFalse(User.is_valid_email(None))
        self.assertFalse(User.is_valid_email(2))
        self.assertFalse(User.is_valid_email(3.33))
        self.assertFalse(User.is_valid_email('key smash'))
        self.assertFalse(User.is_valid_email('@.'))
        self.assertFalse(User.is_valid_email('6789998212@souljaboy'))
        self.assertFalse(User.is_valid_email('almost@valid.'))
        self.assertFalse(User.is_valid_email('almost@.valid'))

    # Testing isValidName() class function
    def test_names(self):
        print(f'Testing test_names')

        # Testing that the first and last name of our new User is valid
        self.assertTrue(User.is_valid_name(self.user_new.first_name))
        self.assertTrue(User.is_valid_name(self.user_new.last_name))

        # Testing other valid name syntax
        self.assertTrue(User.is_valid_name('Cristina :b'))
        self.assertTrue(User.is_valid_name('Literally anything'))
        self.assertTrue(User.is_valid_name('Whatever display name you want'))
        self.assertTrue(User.is_valid_name('As long as it\'s something'))
        self.assertTrue(User.is_valid_name('This is a formality since people can have symbols/digits in their names'))
        self.assertTrue(User.is_valid_name('or really long names'))

        # Testing invalid name syntax
        self.assertFalse(User.is_valid_name(''))
        self.assertFalse(User.is_valid_name(None))
        self.assertFalse(User.is_valid_name(2))
        self.assertFalse(User.is_valid_name(3.33))


if __name__ == '__main__':
    TestCase.main()
