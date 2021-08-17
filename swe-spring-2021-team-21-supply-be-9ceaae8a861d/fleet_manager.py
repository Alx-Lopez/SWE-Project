#!/usr/bin/python3
from resources import fleet_database
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append((rootdir + "/common-services-be"))
import user  # PyCharm does not recognize this import but it is correct


# inherits User class
class FleetManager(user.User):
   
    # adds a fleet
    def add_fleet(self, service_type):
        
        database = fleet_database.FleetDatabase()
        successfulFleetAdd = database.add_fleet(self.get_id(), service_type)
        database.close()
        
        return successfulFleetAdd
    
    # removes a fleet
    def remove_fleet(self, fleet_id):
                
        database = fleet_database.FleetDatabase()
        successfulFleetDel = database.remove_fleet(self.get_id(), fleet_id)
        database.close()
        
        return successfulFleetDel
    
    # selects all the fleets belonging to a certain manager
    def select_fleets(self):
                
        database = fleet_database.FleetDatabase()
        successfulSelManFleet = database.select_manager_fleets(self.get_id())
        database.close()
        
        return successfulSelManFleet
