#!/usr/bin/python3
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append((rootdir + "/common-services-be"))
from resources import database_connect


class VehicleDatabase(database_connect.DatabaseConnect):
    """
    Used for interacting with the vehicle table in the database.

    Functions:
        add_vehicle(vehicle_number, license_plate, fleet_id)
        remove_vehicle(vehicle_number, fleet_id)
        update_vehicle(user_id)
        select_fleets(service_type)
    """

    # attempt to add a vehicle
    # returns True if the vehicle was successfully added, False otherwise
    def add_vehicle(self, vehicle_number, license_plate, fleet_id):
        successful_add = False
        try:
            # check if that vehicle already exists
            with self.connection.cursor() as cursor:
                # select the id of any entries that match the vehicle_number to see if the vehicle already exists
                sql = "SELECT `vehicle_number` FROM `vehicle` WHERE `vehicle_number`=%s"
                cursor.execute(sql, vehicle_number)  # execute the sql statement with the variable(s) given here
                result = cursor.fetchone()  # since we are using a DictCursor, result should be a dict

            # ensure the result is None
            if result is None:
                # insert the new vehicle into the database
                with self.connection.cursor() as cursor:
                    # create a new vehicle entry in the database with the information received in the POST
                    sql = "INSERT INTO `vehicle` (`vehicle_number`,`license_plate`,`battery_charge`,`latitude`," \
                          "`longitude`,`status`,`fleet_id`) VALUES (%s, %s, null, null, null, %s, %s)"
                    cursor.execute(sql, (vehicle_number, license_plate, "AVAILABLE", fleet_id))

                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()

                successful_add = True  # if no errors, add was successful
        except Exception:
            print("Failure to add vehicle")

        # return whether the vehicle was successfully added
        return successful_add

    # attempt to update a vehicle
    # returns True if the vehicle was successfully updated, False otherwise
    def update_vehicle(self, vehicle_number, battery_charge, latitude, longitude, status):
        successful_update = False
        try:
            # check that the vehicle exists
            with self.connection.cursor() as cursor:
                # select the id of any entries that match the vehicle_number to see if the vehicle exists
                sql = "SELECT `vehicle_number` FROM `vehicle` WHERE `vehicle_number`=%s"
                cursor.execute(sql, vehicle_number)  # execute the sql statement with the variable(s) given here
                result = cursor.fetchone()  # since we are using a DictCursor, result should be a dict

            # check that the result is not None before continuing
            if result is not None:
                with self.connection.cursor() as cursor:
                    # update the vehicle entry in the database with the information received
                    sql = "UPDATE `vehicle` SET `battery_charge`=%s,`latitude`=%s,`longitude`=%s,`status`=%s " \
                          "WHERE `vehicle_number`=%s"
                    cursor.execute(sql, (battery_charge, latitude, longitude, status, vehicle_number))

                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()

                successful_update = True  # if no errors, update was successful
        except Exception:
            print("Failure to update vehicle")

        # return whether the vehicle was successfully updated
        return successful_update

    # attempt to update a vehicle STATUS
    # returns True if the vehicle was successfully updated, False otherwise
    def update_vehicle_status(self, vehicle_number, status):
        successful_update = False
        try:
            # check that the vehicle exists
            with self.connection.cursor() as cursor:
                # select the id of any entries that match the vehicle_number to see if the vehicle exists
                sql = "SELECT `vehicle_number` FROM `vehicle` WHERE `vehicle_number`=%s"
                cursor.execute(sql, vehicle_number)  # execute the sql statement with the variable(s) given here
                result = cursor.fetchone()  # since we are using a DictCursor, result should be a dict

            # check that the result is not None before continuing
            if result is not None:
                with self.connection.cursor() as cursor:
                    # update the vehicle entry in the database with the information received
                    sql = "UPDATE `vehicle` SET `status`=%s WHERE `vehicle_number`=%s"
                    cursor.execute(sql, (status, vehicle_number))

                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()

                successful_update = True  # if no errors, update was successful
        except Exception:
            print("Failure to update vehicle")

        # return whether the vehicle was successfully updated
        return successful_update

    # attempt to remove a vehicle
    # returns True if the vehicle was successfully removed, False otherwise
    def remove_vehicle(self, vehicle_number, fleet_id):
        successful_remove = False
        try:
            # check if that vehicle exists
            with self.connection.cursor() as cursor:
                # select the id of any entries that match the vehicle_number to see if the vehicle exists
                sql = "SELECT `vehicle_number` FROM `vehicle` WHERE `vehicle_number`=%s AND `fleet_id`=%s"
                cursor.execute(sql, (vehicle_number, fleet_id))  # execute the sql statement
                result = cursor.fetchone()  # since we are using a DictCursor, result should be a dict

            # check that result is not None before continuing
            if result is not None:
                # delete the vehicle from the database
                with self.connection.cursor() as cursor:
                    sql = "DELETE FROM `vehicle` WHERE `vehicle_number`=%s AND `fleet_id`=%s"
                    cursor.execute(sql, (vehicle_number, fleet_id))

                # commit to save changes and close the cursor
                self.connection.commit()
                cursor.close()

                successful_remove = True  # if no errors, remove was successful
        except Exception:
            print("Failure to remove vehicle")

        # return whether the vehicle was successfully removed
        return successful_remove

    # selects the data of all vehicles belonging to this fleet for purposes of displaying them
    # returns a tuple of dicts that represent each vehicle in the fleet
    def select_vehicles(self, fleet_id):
        try:
            # select all vehicles that belong to the given fleet
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `vehicle` WHERE `fleet_id`=%s"
                cursor.execute(sql, fleet_id)  # execute the sql statement with the variable(s) given here
                vehicles = cursor.fetchall()  # since we are using a DictCursor, result should be a tuple of dicts
                cursor.close()
        except Exception:
            print("Failure to select vehicles")

        # return the resulting tuple of vehicles
        return vehicles

    # select all vehicles marked with the entered status that belong to a given fleet
    # returns a tuple that will either contain dicts of vehicle_numbers or be empty if no vehicles were found
    def select_vehicle_by_status(self, fleet_id, status):
        try:
            # select all vehicles marked as available that belong to the given fleet
            with self.connection.cursor() as cursor:
                sql = "SELECT `vehicle_number`,`license_plate` FROM `vehicle` WHERE `fleet_id`=%s AND `status`=%s"
                cursor.execute(sql, (fleet_id, status))  # execute the sql statement with the variable(s) given here
                # take a single vehicle from the selection
                vehicle = cursor.fetchone()  # since we are using a DictCursor, result should be a dict
                cursor.close()
        except Exception:
            print("Failure to select vehicles")

        # return the resulting vehicle
        return vehicle

    # selects the data of a vehicle by its vehicle_number
    # returns a dictionary of the vehicle with the given vehicle_number
    def select_vehicle_by_number(self, vehicle_number):
        try:
            # select the vehicle with the given vehicle_number
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `vehicle` WHERE `vehicle_number`=%s"
                cursor.execute(sql, vehicle_number)  # execute the sql statement with the variable(s) given here
                vehicle = cursor.fetchone()  # since we are using a DictCursor, result should be a tuple of dicts
                cursor.close()
        except Exception:
            print("Failure to select vehicle")

        # return the resulting tuple of vehicles
        return vehicle
