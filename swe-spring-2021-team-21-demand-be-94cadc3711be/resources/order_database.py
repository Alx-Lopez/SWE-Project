#!/usr/bin/python3
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append((rootdir + "/common-services-be"))
from resources import database_connect


class OrderDatabase(database_connect.DatabaseConnect):
    """
    Used for interacting with the order and address tables in the database.

    Functions:
        record_address(street_address, city, state, zipcode)
        record_order(user_id, address_id)
        update_order(order_number, vehicle_number)
    """

    # records an address in the database if it does not already exist
    # returns the id of the address record
    def record_address(self, street_address, city, state, zipcode):
        address_id = None
        try:
            # check if that email already exists
            with self.connection.cursor() as cursor:
                # select the id of the address to see if it already exists
                sql = "SELECT `address_id` FROM `address` WHERE `street_address`=%s AND `city`=%s AND `state`=%s AND " \
                      "`zipcode`=%s"
                cursor.execute(sql, (street_address, city, state, zipcode))
                result = cursor.fetchall()

            if len(result) == 0:
                # if the address does not already exist, insert it into the db
                with self.connection.cursor() as cursor:
                    # create a new address entry in the database with the information received
                    sql = 'INSERT INTO `address` (`address_id`,`street_address`,`city`,`state`,`zipcode`)' \
                          ' VALUES (null, %s, %s, %s, %s)'
                    cursor.execute(sql, (street_address, city, state, zipcode))
                    address_id = self.connection.insert_id()
                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()
            else:
                for entry in result:
                    address_id = entry['address_id']
        except Exception:
            print("Failure to record address")

        # return that the order was successfully recorded and processed
        return address_id

    # records the order in the database with the vehicle set to null
    # returns the order_number of the order created
    def record_order(self, user_id, address_id):
        order_number = None
        try:
            # adding the request to the db
            with self.connection.cursor() as cursor:
                # create a new order entry in the database with the information received in the POST
                sql = 'INSERT INTO `orders` (`order_number`,`vehicle_number`,`user_id`,`address_id`)' \
                      ' VALUES (null, null, %s, %s)'
                cursor.execute(sql, (user_id, address_id))
                # select the id of the order that was just added
                order_number = self.connection.insert_id()

            # commit to save changes and close the cursor
            self.connection.commit()
            cursor.close()

        except Exception:
            print("Failure to record order")

        # return that the order was successfully recorded and processed
        return order_number

    # updates the order record in the database to include a vehicle
    # returns True iff the update is successful, False otherwise
    def update_order(self, order_number, vehicle_number):
        successful_update = False
        try:
            with self.connection.cursor() as cursor:
                # select the order number to ensure it exists
                sql = "SELECT `order_number` FROM `orders` WHERE `order_number`=%s"
                cursor.execute(sql, order_number)  # execute the sql statement with the variable(s) given here
                result = cursor.fetchone()  # since we are using a DictCursor, result should be a dict

            # check that the result is not None before continuing
            if result is not None:
                # update the order entry if it exists
                with self.connection.cursor() as cursor:
                    # update the order with a vehicle number
                    sql = "UPDATE `orders` SET `vehicle_number`=%s WHERE `order_number`=%s"
                    cursor.execute(sql, (vehicle_number, order_number))

                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()

                successful_update = True  # if no errors, update was successful
        except Exception:
            print("Failure to update order")

        # return whether the vehicle was successfully added
        return successful_update

    # TODO: ADD METHOD FOR LINKING THE ORDER TO THE PRODUCTS AND AMOUNTS INCLUDED
