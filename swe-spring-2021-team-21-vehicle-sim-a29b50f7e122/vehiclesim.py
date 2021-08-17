
import json
import requests
import time

class Vehicle:

    def __init__(self, vehicle_id,lat,long,status):
        self.speed = 0
        self.odometer = 0
        self.tripTime = 0
        self.vehicle_id = vehicle_id
        self.status = status
        self.pulse = False
        self.lat = lat
        self.long = long
        self.route = []

    def __str__(self):
        vehicle = "Current Vehicle {}" .format(self.vehicle_id)
        return vehicle

    #pre:true
    #post:none
    #function description: starts vehicle and heartbeat
    def start_vehicle(self):
        self.start_heartbeat()
        self.status = "OOS"

    #pre:true
    #post:none
    #function description: returns the vehicle class as a JSON OBJ
    def toJSON(self):
        return json.dumps(self, default=lambda a: a.__dict__)

    #pre:true
    #post:None
    #function description:starts heartbeat
    def start_heartbeat(self):
        self.pulse = True
        self.status = "AVAILABLE"
        self.heartbeat()

    # pre:none
    # post: true
    # function description: stops heartbeat
    def stop_heartbeat(self):
        self.pulse = False
        self.status = "OOS"
        print("The status of vehicle {} has changed to  {}".format(self.vehicle_id, self.status))

    #pre:true
    #post: none
    #function description: sends heartbeat(location,status,vehicle_id) to supply cloud
    def heartbeat(self):
        count = 0
        while self.pulse:
            prev_location = (self.lat, self.long)
            vehicle_heartbeat = self.toJSON()
            try:
                vehicle_heartbeat_response = requests.post("https://supply.team21.sweispring21.tk/api/heartbeat",vehicle_heartbeat)
            except:
                print("Error in Connection")
                self.stop_heartbeat()
            response = vehicle_heartbeat_response.json()
            response_received = True if response != {} else False
            if response_received == True and count == 0:
                self.route = receive_route(response['route'])
                self.status = "BUSY"
                count = 1
            if len(self.route) != 0:
                self.move_thru_route()
            else:
                self.status = "AVAILABLE"
                break
            time.sleep(5)
            print("The vehicle moved to {} ".format(prev_location))
            print(vehicle_heartbeat_response)

        self.stop_heartbeat()

    # pre:true
    # post:none
    # function description:jumps through each coord_pair and pops a coord_pair each time its called
    def move_thru_route(self):
        for coor_pair in self.route:
            lat,long = coor_pair
            self.lat = lat
            self.long = long
            self.route.pop(0)
            break


    #pre: json response from mapbox
    #post: returns ->[[lat,long],[lat,long],[lat,long],[lat,long]]
    #function description:#converts the json response into a 2d array
def receive_route(json_response):
    vehicle_route=json.dumps(json_response.get("routes")[0].get("geometry").get("coordinates"))
    return json.loads(vehicle_route)



def main():
    myVehicle = Vehicle("12345",-97.7333 ,30.2053 , status="REQUESTED")
    print("*" * 8, "I'm an autonomous vehicle!")
    while True:
        action = input("What should I do? [S]tartHearbeat, [Q]uit\t ---> ").upper()
        if action not in "SQ" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'S':
            print(myVehicle.__str__() + " is starting route")
            myVehicle.start_vehicle()
        elif action == 'Q':
            break

    print('\n****** bye-bye'.upper())

main()
