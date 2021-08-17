from resources import order_database
import requests
import json


class Order:
    """
    Used to create an order for a customer.

    Functions:
        record_order()
        update_order()
        get_vehicle()
        get_address_id()
    """

    VEHICLE_REQUEST_URL = 'https://supply.team21.sweispring21.tk/api/vehicle-request'

    def __init__(self, customer_id, dest_address, service_type):
        # TODO: validate constructor inputs
        # Once inputs are validated, update functions that check these inputs
        self.customer_id = customer_id
        self.address = dest_address
        self.service_type = service_type

        # Hardcoded to None when initialized
        self.order_number = None
        self.vehicle = None

    def record_order(self):
        address_id = Order.get_address_id(self)

        # We require a valid address_ID to record our order
        if address_id is not None:
            # create a database connection
            database = order_database.OrderDatabase()

            # attempt to record an order
            order_result = database.record_order(self.customer_id, address_id)

            # close the database connection
            database.close()

            # if we received an orderNumber, the order was recorded successfully
            # if we received None (null), the order failed to be recorded
            if order_result is not None:
                self.order_number = order_result

    def update_order(self):
        success = False

        # Ensure that there is a vehicle to now update the specified order with
        if (self.order_number is not None) and (self.vehicle is not None):
            vehicle_number = self.vehicle['vehicle_number']

            # create a database connection
            database = order_database.OrderDatabase()

            # attempt to update the order
            result = database.update_order(self.order_number, vehicle_number)

            # close the database connection
            database.close()

            if result:
                success = True

        return success

    def get_vehicle(self):
        # if the order was placed (not None), we can request a vehicle for it
        if self.order_number is not None:
            dest_address = Order.format_address(self)

            # setting up the data that our api needs to receive
            data = {
                'order_number': self.order_number,
                'service_type': self.service_type,
                'dest_address': dest_address
            }

            # create the request and take in a response
            response = requests.post(Order.VEHICLE_REQUEST_URL, json.dumps(data))
            # TODO: check that we received a 200 status before setting vehicle
            # set vehicle to our response (JSON format)
            vehicle_json = response.json()

            self.vehicle = vehicle_json['vehicle']

    # TODO: potentially make address its own class to handle things like this and format_address()
    def get_address_id(self):
        # create a database connection
        database = order_database.OrderDatabase()

        # separately pull every element of the address
        street_address = self.address['street_address']
        city = self.address['city']
        state = self.address['state']
        zip_code = self.address['zip_code']

        # attempt to record/access the address and receive its ID
        address_id = database.record_address(street_address, city, state, zip_code)

        # close the database connection
        database.close()

        # return the received order ID
        return address_id

    # TODO: potentially make address its own class to handle things like this and get_address_id()
    def format_address(self):
        # Formatting the address into one string
        # Example formatting for the following values:
        # streetAddress = '1234 Main St'
        # city = 'Austin'
        # state = 'TX'
        # zip_code = '78704'
        # dest_address = '1234 Main St Austin TX 78704'
        address_string = f"{self.address['street_address']} {self.address['city']} "
        address_string += f"{self.address['state']} {self.address['zip_code']}"

        return address_string

    # string representation of an Order
    def __str__(self):
        # Handling when order_number and or vehicle is None
        if self.order_number is None:
            order_number_string = "Order does not have an associated number"
        else:
            order_number_string = f"Order Number: {self.order_number}"

        if self.vehicle is None:
            vehicle_number_string = "Order does not have an associated vehicle"
        else:
            vehicle_number_string = f"Vehicle Number: {self.vehicle['vehicle_number']}"

        # Setting up String filled with all Order information
        order_str = f"{order_number_string}, Customer ID: {self.customer_id}, Address: {self.format_address()}, "
        order_str += f"{vehicle_number_string}, Service Type: {self.service_type}"
        return order_str

    # overwrite the display of internal representation for list use
    __repr__ = __str__

    # Orders are equal if their IDs are equal
    # We are ignoring implementing this for now as a result

