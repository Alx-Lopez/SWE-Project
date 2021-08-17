#!/usr/bin/python3
from order import Order
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append((rootdir + "/common-services-be"))
import user


class Customer(user.User):
    """
    Used to create a customer.

    Functions:
        place_order(dest_address, service_type)
    """

    def place_order(self, dest_address, service_type):
        """
        Attempts to place an order for the customer

        :param dest_address: (String) destination address for the order
        :param service_type: (String) plugin type of the order
        :return: dictionary with keys: (boolean) success, (String) order_number, (Dictionary) vehicle
        """
        success = False
        # get customer's ID for the order
        customer_id = self.get_id()

        # create an order with the customer's ID, destination address, and plugin type
        customer_order = Order(customer_id, dest_address, service_type)

        # attempt to record the address to our system
        customer_order.record_order()

        if customer_order.order_number is not None:
            customer_order.get_vehicle()
            if customer_order.vehicle is not None:
                success = customer_order.update_order()

        order_number = customer_order.order_number
        vehicle = customer_order.vehicle
        order_information = {'success': success, 'order_number': order_number, 'vehicle': vehicle}

        return order_information
