#!/usr/bin/python3
import logging
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs

from resources import vehicle_database
from dispatch import Dispatch
from fleet_manager import FleetManager
from fleet import Fleet

# Class Logger we can use for debugging our Python service. You can add an additional parameter here for
# specifying a log file if you want to see a stream of log data in one file.
logging.basicConfig(level=logging.DEBUG)


# BaseHTTPRequestHandler is a class from the http.server python module. http.server is a simple
# module used for creating application servers. BaseHTTPRequestHandler will help us respond to requests that arrive
# at our server, matching a specified hostname and port. For additional documentation on this module,
# you can read: https://docs.python.org/3/library/http.server.html
class Supply(BaseHTTPRequestHandler):

    # HTTP Response code dictionary constant we can reuse inside our responses back to the client. Typically this
    # would be in a configuration file where you store constants you repeatedly use throughout your services.
    HTTP_STATUS_RESPONSE_CODES = {
        'OK': HTTPStatus.OK,
        'MOVED_PERMANENTLY': HTTPStatus.MOVED_PERMANENTLY,
        'PERMANENT_REDIRECT': HTTPStatus.PERMANENT_REDIRECT,
        'FORBIDDEN': HTTPStatus.FORBIDDEN,
        'NOT_FOUND': HTTPStatus.NOT_FOUND,
    }

    # Here's how you extract GET parameters from a URL entered by a client.
    def extract_GET_parameters(self):
        path = self.path
        parsedPath = urlparse(path)
        paramsDict = parse_qs(parsedPath.query)
        logging.info('GET parameters received: ' + json.dumps(paramsDict, indent=4, sort_keys=True))
        return paramsDict

    # Here's how we extract the POST body of data attached to the request by the client.
    def extract_POST_Body(self):
        # The content-length HTTP header is where our POST data will be in the request. So we'll need to
        # read the data using an IO input buffer stream built into the http.server module.
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        postBodyDict = json.loads(postBodyString)
        logging.info('POST Body received: ' + json.dumps(postBodyDict, indent=4, sort_keys=True))
        return postBodyDict

    ########## GET ENDPOINTS ##########

    def do_GET(self):
        path = self.path
        paramsDict = self.extract_GET_parameters()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND']
        responseBody = {}

        if '/get-vehicles' in path:
            fleet_id = paramsDict['fleet_id']
            # create a fleet object and use it to select all the vehicles from the fleet
            vehicles = None  # TODO: call get_all_vehicles

            if vehicles is not None:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']

            responseBody['vehicles'] = vehicles

        elif '/get-fleets' in path:
            email = paramsDict['email']  # sent from localStorage
            # create a FleetManager object and use it to select all the fleets that belong to them
            fleets = None  # TODO: call select_manager_fleets

            if fleets is not None:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']
                responseBody['fleets'] = fleets

        # get a single vehicle

        elif '/get-vehicle-by-id' in path:
            vehicle_number = paramsDict['vehicle_number']
            # create a vehicle database
            database = vehicle_database.VehicleDatabase()
            # select a vehicle from the database with the vehicle_number
            vehicle = database.select_vehicle_by_number(vehicle_number)
            database.close()

            if vehicle is not None:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']
                responseBody['vehicle'] = vehicle

        # RESPONSE

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = json.dumps(responseBody)
        logging.info('Response: ' + response)
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)

    ########## POST ENDPOINTS ##########

    # The do_POST(self) function is how we respond to POST requests from clients.
    # we should only need POST for Register/Login
    def do_POST(self):
        path = self.path
        # Extract the POST body data from the HTTP request, and store it into a Python
        # dictionary we can utilize inside of any of our POST endpoints.
        postBody = self.extract_POST_Body()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND']

        # initialize the response body
        responseBody = {}

        # Vehicle Add PATH

        # FULL PATH: {supply domain}/supply/add-vehicle
        if '/add-vehicle' in path:
            # the request needs to send in a vehicle_number, plate_number, and fleet_id
            vehicle_number = postBody['vehicle_number']
            license_plate = postBody['license_plate']
            fleet_id = postBody['fleet_id']

            fleet = Fleet(fleet_id)

            # attempt to add a new vehicle to a fleet
            successful = fleet.add_vehicle(vehicle_number, license_plate)

            # if it is successful, send back a 200 OK response
            if successful:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        # Vehicle Remove PATH

        # FULL PATH: {supply domain}/supply/remove-vehicle
        if '/remove-vehicle' in path:
            vehicle_number = postBody['vehicle_number']
            fleet_id = postBody['fleet_id']

            fleet = Fleet(fleet_id)

            # attempt to remove a vehicle from a fleet
            successful = fleet.remove_vehicle(vehicle_number)

            # if it is successful, send back a 200 OK response
            if successful:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        # Fleet Add PATH

        # FULL PATH: {supply domain}/supply/add-fleet
        if '/add-fleet' in path:
            service_type = postBody['service_type']
            email = postBody['email']  # email needs to be sent in from localStorage

            fleet = FleetManager(email)

            # attempt to add a fleet
            successful = fleet.add_fleet(service_type)

            # if it is successful, send back a 200 OK response
            if successful:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        # Fleet Remove PATH

        # FULL PATH: {supply domain}/supply/remove-fleet
        elif '/remove-fleet' in path:
            fleet_id = postBody['fleet_id']
            email = postBody['email']  # email needs to be sent in from localStorage

            fleet_manager = FleetManager(email)

            # attempt to add a fleet
            successful = fleet_manager.remove_fleet(fleet_id)

            # if it is successful, send back a 200 OK response
            if successful:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        # heartbeat API PATH

        elif '/api/heartbeat' in path:
            vehicle_number = postBody['vehicle_id']
            vlatitude = postBody['lat']
            vlongitude = postBody['long']
            vstatus = postBody['status']

            # create a database connection
            database = vehicle_database.VehicleDatabase()
            # select the vehicle by the vehicle_number, and check the status
            vehicle = database.select_vehicle_by_number(vehicle_number)

            if vehicle['status'] == "REQUESTED":
                dispatch = Dispatch()
                pending_record = dispatch.find_pending_record(vehicle_number)
                if pending_record is not None:
                    # set the destination to the location in record and the source to the vehicle location
                    destination = {'latitude': pending_record['latitude'], 'longitude': pending_record['longitude']}
                    source = {'latitude': vlatitude, 'longitude': vlongitude}
                    # get a route to send the vehicle
                    route = dispatch.get_route(source, destination)
                    # now update the vehicle with it's own information and prepare to send a route as a response
                    success = database.update_vehicle(vehicle_number, 100, vlatitude, vlongitude, "BUSY")
                    if success:
                        status = self.HTTP_STATUS_RESPONSE_CODES['OK']
                        dispatch.update_record(vehicle_number, "FILLED")
                        responseBody['route'] = route
            else:
                success = database.update_vehicle(vehicle_number, 100, vlatitude, vlongitude, vstatus)
                # if it is successful, send back a 200 OK response
                if success:
                    status = self.HTTP_STATUS_RESPONSE_CODES['OK']

            # finally, close the connection to the database when finished
            database.close()

        # vehicle request API PATH

        elif '/api/vehicle-request' in path:
            order_number = postBody['order_number']
            service_type = postBody['service_type']
            dest_address = postBody['dest_address']
            # product_info = json.load(postBody['product_info'])
            # initialize dispatch and create a record
            dispatch = Dispatch()
            dispatch.create_record(order_number, dest_address)
            # get an available vehicle to fill the record
            vehicle = dispatch.get_vehicle(service_type)

            # if the vehicle exists, fill the record and prepare a response
            if vehicle is not None:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']
                vehicle_number = vehicle['vehicle_number']

                # fill dispatch record
                dispatch.update_record(vehicle_number, "PENDING")

                # update the vehicle's status
                database = vehicle_database.VehicleDatabase()
                vehicle_status = "REQUESTED"
                database.update_vehicle_status(vehicle_number, vehicle_status)

                responseBody['vehicle'] = vehicle

        # RESPONSE

        # sending the HTTP response
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = json.dumps(responseBody)
        logging.info('Response: ' + response)
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)


# Turn the application server on at port 8082 on localhost and fork the process.
if __name__ == '__main__':
    hostName = "localhost"
    # Ports are part of a socket connection made between a server and a client. Ports 0-1023 are
    # reserved for common TCP/IP applications and shouldn't be used here. Communicate with your
    # DevOps member to find out which port you should be running your application off of.
    serverPort = 8083
    appServer = HTTPServer((hostName, serverPort), Supply)
    logging.info('Server started http://%s:%s' % (hostName, serverPort))

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    logging.info('Server stopped')
