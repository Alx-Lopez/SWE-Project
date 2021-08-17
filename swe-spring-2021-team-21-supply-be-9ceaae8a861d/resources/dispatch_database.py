#!/usr/bin/python3
import logging
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append((rootdir + "/common-services-be"))
from resources import database_connect


class DispatchDatabase(database_connect.DatabaseConnect):
    """
    Used for interacting with the dispatch table in the database.

    Functions:
        dispatch_record(order_number, vehicle_number)
    """

    def dispatch_record(self, order_number, latitude, longitude, record_status):
        record_id = None
        try:
            # insert the new record into the database
            with self.connection.cursor() as cursor:
                # create a new dispatch record in the database with the information received
                sql = "INSERT INTO `dispatch` (`record_id`,`order_number`,`latitude`,`longitude`,`record_status`," \
                      "`record_datetime`,`vehicle_number`) VALUES (null, %s, %s, %s, %s, now(), null)"
                cursor.execute(sql, (order_number, latitude, longitude, record_status))
                record_id = self.connection.insert_id()
                logging.info(record_id)
            # commit to save changes and close the cursor
            self.connection.commit()
            cursor.close()

        except Exception:
            logging.info("Failure to create dispatch record")

        # return whether the record id if successfully added, None otherwise
        return record_id

    # update the status of the dispatch record and add a vehicle when one has been selected
    def update_record(self, record_id, record_status, vehicle_number):
        successful_update = False
        try:
            # update the record that belongs to record_id
            with self.connection.cursor() as cursor:
                # update the record status and the vehicle number
                sql = "UPDATE `dispatch` SET `record_status`=%s,`vehicle_number`=%s WHERE `record_id`=%s"
                cursor.execute(sql, (record_status, vehicle_number, record_id))

            # commit to save changes and close the cursor
            self.connection.commit()
            cursor.close()
            successful_update = True
        except Exception:
            print("Failure to update dispatch record")

        # return whether the record id if successfully added, None otherwise
        return successful_update

    # select a single record that contains the vehicle and the status record_status
    # returns a tuple that will either contain dicts of vehicle_numbers or be empty if no records found
    def select_record_by_status(self, vehicle_number, record_status):
        try:
            # select all records marked with record_status containing the vehicle
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `dispatch` WHERE `vehicle_number`=%s AND `record_status`=%s"
                cursor.execute(sql, (vehicle_number, record_status))
                # take a single record from the selection
                record = cursor.fetchone()  # since we are using a DictCursor, result should be a dict
                cursor.close()
        except Exception:
            print("Failure to select vehicles")

        # return the resulting record
        return record
