#!/usr/bin/python3
from resources import vehicle_database


class Fleet:

    # Fleet constructor
    def __init__(self, fleet_id):
        self.fleet_id = fleet_id

    # add vehicle to fleet
    def add_vehicle(self, vehicle_number, plate_number):
        
        database = vehicle_database.VehicleDatabase()
        successfulVehAdd = database.add_vehicle(vehicle_number, plate_number, self.fleet_id)
        database.close()
        
        return successfulVehAdd
    
    # remove vehicle to fleet
    def remove_vehicle(self, vehicle_number):
        
        database = vehicle_database.VehicleDatabase()
        successfulVehRem = database.remove_vehicle(vehicle_number, self.fleet_id)
        database.close()
        
        return successfulVehRem

    # select vehicles from fleet that have status="available"
    # will return None (null) if nothing is found
    def get_available_vehicle(self):
        status = "AVAILABLE"
        database = vehicle_database.VehicleDatabase()
        successfulGetAvaVeh = database.select_vehicle_by_status(self.fleet_id, status)
        database.close()
        
        return successfulGetAvaVeh

    # select all the vehicles in a fleet from the db and return them in a list
    # will return None (null) if nothing is found
    def get_all_vehicles(self):
        
        database = vehicle_database.VehicleDatabase()
        successfulGetAllVeh = database.select_vehicles(self.fleet_id)
        database.close()
        
        return successfulGetAllVeh
