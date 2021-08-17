#!/usr/bin/python3
from resources import database_user
import re


class User:
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$")

    # User constructor
    # NOTE: We allow empty first name and last name due to login, but register requires these fields
    def __init__(self, email, first_name=None, last_name=None):
        # raise an exception if an improper email is sent in
        if not User.is_valid_email(email):
            raise Exception('Invalid email for User')

        # raise an exception if an improper first name is sent in
        # a User can be initialized without a name, so None can pass
        if (first_name is not None) or (last_name is not None):
            if not (User.is_valid_name(first_name) and User.is_valid_name(last_name)):
                raise Exception('Invalid first and or last name for User')

        # if exception wasn't raised, valid variables were received
        # setting variables
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    # register the user
    def register(self, password):
        successful_register = False

        if (User.is_valid_name(self.first_name)) and (User.is_valid_name(self.last_name)):
            database = database_user.DatabaseUser()
            successful_register = database.register(self.first_name, self.last_name, self.email, password)
            database.close()

        return successful_register

    # log the user in
    def login(self, password):
        database = database_user.DatabaseUser()
        successful_login, user_name = database.login(self.email, password)
        database.close()

        return successful_login, user_name

    # get the id of the user
    # will return None (null) if the user is not in our system
    def get_id(self):
        database = database_user.DatabaseUser()
        user_id = database.get_user_id(self.email)
        database.close()

        return user_id

    # check for a valid email
    # if the email is a string and matches the regex defined in our User class, return true
    # otherwise: return False
    @staticmethod
    def is_valid_email(email):
        is_valid_email = False

        if isinstance(email, str) and re.match(User.EMAIL_REGEX, email):
            is_valid_email = True

        return is_valid_email

    # check for a valid name
    # if the name is None (null), empty, or not a string, return false
    # otherwise: return True
    @staticmethod
    def is_valid_name(name):
        is_valid_name = not((name is None) or (not name) or (not isinstance(name, str)))
        return is_valid_name

    # string representation of a User
    # covers a User without a (valid) name
    def __str__(self):
        if User.is_valid_name(self.first_name) and User.is_valid_name(self.last_name):
            name_string = f"User full name: {self.first_name} {self.last_name}"
        else:
            name_string = "User has no name."

        return f"User email: {self.email} " + name_string

    # overwrite the display of internal representation for list use
    __repr__ = __str__

    # checking equality between our Users
    # Users are equal if they have the same email
    # Different names do not matter
    def __eq__(self, other):
        # if the 'other' input we're comparing is not an instance of our class
        # return False
        if not isinstance(other, User):
            return False

        return self.email == other.email
