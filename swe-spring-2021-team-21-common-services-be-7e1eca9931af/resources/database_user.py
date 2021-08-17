#!/usr/bin/python3
from resources import database_connect


class DatabaseUser(database_connect.DatabaseConnect):

    # attempt to register a user
    def register(self, f_name, l_name, email, password):
        successful_reg = False
        # check if that email already exists
        with self.connection.cursor() as cursor:
            # select the id of any entries that match the email to see if the user is already registered
            sql = "SELECT `user_id` FROM `user` WHERE `email`=%s"
            cursor.execute(sql, email)  # execute the sql statement with the variable(s) given here
            result = cursor.fetchone()  # since we are using a DictCursor, result should be a tuple of dicts

        # if the length of the result is 0, this means the user is not registered yet and we can continue
        if result is None:
            # Since the user does not exist yet, we can add them to the DB
            with self.connection.cursor() as cursor:
                # create a new user entry in the database with the information received in the POST
                sql = "INSERT INTO `user` (`user_id`,`f_name`,`l_name`,`email`, `password`) VALUES " \
                      "(null, %s, %s, %s, %s)"
                cursor.execute(sql, (f_name, l_name, email, password))

            # commit to save changes and close the cursor
            self.connection.commit()
            cursor.close()

            successful_reg = True  # if no errors, registration was successful

        # return that the user was successfully registered
        return successful_reg

    # attempt to log in a user
    def login(self, email, entered_password):
        successful_login = False
        name = None
        with self.connection.cursor() as cursor:
            # select the password from the database entry that matches the given email
            sql = "SELECT `password`,`f_name` FROM `user` WHERE `email`=%s"
            cursor.execute(sql, email)  # execute the sql statement with the variable(s) given here
            result = cursor.fetchone()  # since we are using a DictCursor, result should be a tuple of dicts

        # Check the length of result, if the email is in the db this value should be 1 and we want to continue.
        # Otherwise, we will simply send a 200 response to signal incorrect login/stay on the page
        if result is not None:
            # once the password is received, compare this to the password stored in result
            # if the passwords are the same, set the return value to True
            if entered_password == result['password']:
                successful_login = True
                name = result['f_name']

        # close the cursor
        cursor.close()

        # return that the login was successful
        return successful_login, name

    # returns the id of the user with the given email
    def get_user_id(self, email):
        user_id = None
        with self.connection.cursor() as cursor:
            # select the user_id from the database entry that matches the given email
            sql = "SELECT `user_id` FROM `user` WHERE `email`=%s"
            cursor.execute(sql, email)  # execute the sql statement with the variable(s) given here
            result = cursor.fetchone()  # since we are using a DictCursor, result should be a tuple of dicts

        # Check the length of result, if the email is in the db this value should be 1 and we want to continue
        if result is not None:
            user_id = result['user_id']

        # close the cursor
        cursor.close()

        # return the user_id
        return user_id
