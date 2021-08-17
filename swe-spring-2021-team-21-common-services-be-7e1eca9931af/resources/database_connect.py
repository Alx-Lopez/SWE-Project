#!/usr/bin/python3
import pymysql
import pymysql.cursors
from decouple import config


class DatabaseConnect:

    # initialize the database object by starting a connection
    def __init__(self):
        # get data from .env
        USER = config('USER')
        KEY = config('KEY')
        DB = config('DB')
        # connect to the database with PyMySQL
        self.connection = pymysql.connect(host='localhost',
                                          user=USER,
                                          password=KEY,
                                          database=DB,
                                          cursorclass=pymysql.cursors.DictCursor)

    # close the connection when you are completely finished with the database object
    def close(self):
        self.connection.close()
