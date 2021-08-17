#!/usr/bin/python3
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append((rootdir + "/common-services-be"))
from resources import database_connect


class FleetDatabase(database_connect.DatabaseConnect):
    """
    Used for interacting with the fleet table in the database.

    Functions:
        add_fleet(user_id, service_type)
        remove_fleet(user_id, fleet_id)
        select_manager_fleets(user_id)
        select_fleets(service_type)
    """

    # attempt to add a fleet
    # returns True if the fleet was successfully added, False otherwise
    def add_fleet(self, user_id, service_type):
        success = False
        try:
            # insert the new fleet into the database
            with self.connection.cursor() as cursor:
                # create a new fleet entry in the database with the information received
                sql = "INSERT INTO `fleet` (`fleet_id`,`service_type`,`home_latitude`,`home_longitude`,`user_id`) " \
                      "VALUES (null, %s, %s, %s, %s)"
                cursor.execute(sql, (service_type, 30.2053, -90.7333, user_id))
            # commit to save changes and close the cursor
            self.connection.commit()
            cursor.close()
            success = True
        except Exception:
            print("Failure to add fleet")

        # return whether the fleet was successfully added
        return success

    # attempt to remove a fleet
    # returns True if the fleet was successfully removed, False otherwise
    def remove_fleet(self, user_id, fleet_id):
        successful_remove = False
        try:
            # check if that fleet exists
            with self.connection.cursor() as cursor:
                # select the id of any entries that match the fleet_id to see if the fleet exists
                sql = "SELECT `fleet_id` FROM `fleet` WHERE `fleet_id`=%s AND `user_id`=%s"
                cursor.execute(sql, (fleet_id, user_id))  # execute the sql statement with the variable(s) given here
                result = cursor.fetchone()  # since we are using a DictCursor, result should be a dict

            # ensure result is not None
            if result is not None:
                # delete the fleet from the database
                with self.connection.cursor() as cursor:
                    sql = "DELETE FROM `fleet` WHERE `fleet_id`=%s"
                    cursor.execute(sql, fleet_id)

                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()

                successful_remove = True  # if no errors, remove was successful
        except Exception:
            print("Failure to remove fleet")

        # return whether the fleet was successfully removed
        return successful_remove

    # selects the data of all fleets belonging to this fleet manager for purposes of displaying them
    # returns a tuple of dicts that represent each fleet
    def select_manager_fleets(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                # select all vehicles that belong to the given fleet
                sql = "SELECT * FROM `fleet` WHERE `user_id`=%s"
                cursor.execute(sql, user_id)  # execute the sql statement with the variable(s) given here
                fleets = cursor.fetchall()  # since we are using a DictCursor, result should be a tuple of dicts
                cursor.close()
        except Exception:
            print("Failure to select fleets")

        # return the resulting tuple of fleets
        return fleets

    # selects the data of all fleets for a given service type for getting available vehicles from
    # returns a tuple of dicts that represent each fleet
    def select_fleets(self, service_type):
        try:
            with self.connection.cursor() as cursor:
                # select all vehicles that belong to the given fleet
                sql = "SELECT * FROM `fleet` WHERE `service_type`=%s"
                cursor.execute(sql, service_type)  # execute the sql statement with the variable(s) given here
                fleets = cursor.fetchall()  # since we are using a DictCursor, result should be a tuple of dicts
                cursor.close()
        except Exception:
            print("Failure to select fleets")

        # return the resulting tuple of fleets
        return fleets
