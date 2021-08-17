#!/usr/bin/python3
from resources import dispatch_database
from resources import fleet_database
from fleet import Fleet
import requests


class Dispatch:

    def __init__(self, record_id=None):
        self.record_id = record_id

    # creates a dispatch record in the database
    # sets the record_id for the dispatch instance
    def create_record(self, order_number, destination_address):
        database = dispatch_database.DispatchDatabase()
        record_status = "OPEN"
        # get the destination coordinates through a mapbox request
        destination = self.get_coordinates_of_destination(destination_address)
        # create the dispatch record, setting the status as OPEN
        result = database.dispatch_record(order_number, destination['latitude'], destination['longitude'], record_status)
        # close the database after recording the record
        database.close()
        self.record_id = result

    # creates a dispatch record in the database
    # returns True if the record was updated successfully, False otherwise
    def update_record(self, vehicle_number, record_status):
        database = dispatch_database.DispatchDatabase()
        result = database.update_record(self.record_id, record_status, vehicle_number)
        database.close()

        return result

    @staticmethod
    # Checks through all fleets of a given service type to find a available vehicle
    def get_vehicle(service_type):

        database = fleet_database.FleetDatabase()
        results = database.select_fleets(service_type)
        database.close()

        AvaVeh = None

        # loop through every fleet with a given service type
        for entry in results:

            fleet_id = entry['fleet_id']
            fleet_candidate = Fleet(fleet_id)

            veh = fleet_candidate.get_available_vehicle()
            # if getAvailableVehicle returns a value a vehicle is found
            if veh is not None:
                AvaVeh = veh
            else:
                continue
        # if no vehicle found return None
        return AvaVeh

    @staticmethod
    # grabs dispatch records of the status pending that contain the vehicle_number entered
    def find_pending_record(vehicle_number):
        database = dispatch_database.DispatchDatabase()
        record_status = "PENDING"
        # select a single record that contains the vehicle and is listed as PENDING
        record = database.select_record_by_status(vehicle_number, record_status)
        return record

    @staticmethod
    # returns a dict of the latitude and longitude of the address
    def get_coordinates_of_destination(destination_address):
        token = "pk.eyJ1IjoidGhlY29vbGVyamFtcyIsImEiOiJja2x2N3I0bWcwNm5uMm9xb2YycTRrZmp6In0.HeT7Nh005EmxAxq47waiPw"
        mapbox_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + destination_address + ".json"
        params = {"limit": 1, "access_token": token}

        # combine the above data into a mapbox forward geocoding request
        response = requests.get(mapbox_url, params=params)
        mapbox_geo = response.json()

        # destination is a list of the coordinates
        destination = mapbox_geo['features'][0]['geometry']['coordinates']
        destination_dict = {'latitude': destination[1], 'longitude': destination[0]}

        return destination_dict

    @staticmethod
    # takes in a source dictionary of coordinates and a destination dictionary of coordinates
    # returns an entire mapbox route json from source -> destination
    def get_route(source, destination):
        coordinate_string = f"{source['longitude']},{source['latitude']};" \
                            f"{destination['longitude']},{destination['latitude']}"

        token = "pk.eyJ1IjoidGhlY29vbGVyamFtcyIsImEiOiJja2x2N3I0bWcwNm5uMm9xb2YycTRrZmp6In0.HeT7Nh005EmxAxq47waiPw"
        mapbox_url = "https://api.mapbox.com/directions/v5/mapbox/driving/" + coordinate_string + ".json"
        params = {"geometries": "geojson", "access_token": token}

        # combine the above data into a mapbox route request
        response = requests.get(mapbox_url, params=params)
        mapbox_route = response.json()

        return mapbox_route
