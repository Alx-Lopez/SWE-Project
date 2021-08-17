#!/usr/bin/python3
from unittest import TestCase, mock
import sys
sys.path.insert(1, '../')
from dispatch import Dispatch


class TestDispatch(TestCase):

    # TODO: include more test cases
    # TODO: improve our use of mock
    # This will build these fleets before every test case
    def setUp(self):
        print('setup')
        self.dispatch_record_one = Dispatch('1')
        self.dispatch_record_two = Dispatch('2')

    # Called after every test case, assuming setUp() was successful
    def tearDown(self):
        print('tearDown\n')

    # Testing create_record as well as get_coordinates_of_destination since it's necessary for create_record
    # This patch will allow us to manage the function/database responses
    @mock.patch('dispatch.Dispatch.create_record')
    @mock.patch('dispatch.Dispatch.get_coordinates_of_destination')
    def test_create_record(self, mock_coordinates, mock_create_record):
        print('Testing test_create_record')

        # Setting up mocks for our test
        coordinates = {'latitude': 30.2672, 'longitude': -97.7431}
        mock_coordinates.return_value = coordinates
        # Initializing a valid instance of dispatch
        valid_dispatch = Dispatch()
        # need to directly set instance variable until mock knowledge is improved
        valid_dispatch.record_id = '3'
        address = "1234 Main St Austin TX 78704"

        # Trying to create a dispatch record
        # Our patch should allow this to work
        # assuming it reaches the database call
        valid_dispatch.create_record('23', address)
        self.assertEqual('3', valid_dispatch.record_id)
        self.assertEqual(coordinates, valid_dispatch.get_coordinates_of_destination(address))

        # Setting up mocks for our test
        mock_coordinates.return_value = None
        # Initializing an instance of dispatch
        invalid_dispatch = Dispatch()

        # Trying to record an invalid dispatch record
        # Our patch should allow this to be tested
        # assuming it reaches the database call
        invalid_dispatch.create_record(None, None)
        self.assertTrue(invalid_dispatch.record_id is None)
        self.assertTrue(invalid_dispatch.get_coordinates_of_destination(None) is None)

    # Testing update_record function
    # This patch will allow us to manage the function/database responses
    @mock.patch('dispatch.Dispatch.update_record')
    def test_update_record(self, mock_update_record):
        print('Testing test_update_record')

        # Setting up mocks for our test
        mock_update_record.return_value = True
        dispatch_status = 'PENDING'
        vehicle_number = '1'

        # Trying to update a valid dispatch record
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.dispatch_record_one.update_record(vehicle_number, dispatch_status))
        self.assertTrue(self.dispatch_record_two.update_record(vehicle_number, dispatch_status))

        # Setting up mocks for our test
        mock_update_record.return_value = False

        # Trying to update invalid dispatch records
        # Our patch should allow this to be tested
        # assuming it reaches the database call
        self.assertFalse(self.dispatch_record_one.update_record(None, None))
        self.assertFalse(self.dispatch_record_one.update_record(vehicle_number, None))
        self.assertFalse(self.dispatch_record_one.update_record(None, dispatch_status))
        self.assertFalse(self.dispatch_record_one.update_record('', ''))
        self.assertFalse(self.dispatch_record_one.update_record(dispatch_status, vehicle_number))
        self.assertFalse(self.dispatch_record_one.update_record(1, 1))
        self.assertFalse(self.dispatch_record_one.update_record(1.1, 1.1))

    # Testing get_vehicle function
    # This patch will allow us to manage the function/database responses
    @mock.patch('dispatch.Dispatch.get_vehicle')
    def test_get_vehicle(self, mock_get_vehicle):
        print('Testing test_get_vehicle')

        # Setting up mock for our test
        mock_get_vehicle.return_value = {'vehicle_number': '1'}
        service_type = 'rideShare'

        # Trying to get a vehicle for our dispatch record
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.dispatch_record_one.get_vehicle(service_type) is not None)
        self.assertTrue(self.dispatch_record_two.get_vehicle(service_type) is not None)

        # Setting up mock for our test
        mock_get_vehicle.return_value = None

        # Trying to get a vehicle for an invalid service_type
        # Our patch should allow us to test this
        # asssuming it reaches the database call
        self.assertTrue(self.dispatch_record_one.get_vehicle('baking') is None)
        self.assertTrue(self.dispatch_record_one.get_vehicle(2) is None)
        self.assertTrue(self.dispatch_record_one.get_vehicle('1') is None)
        self.assertTrue(self.dispatch_record_one.get_vehicle(None) is None)
        self.assertTrue(self.dispatch_record_one.get_vehicle('') is None)
        self.assertTrue(self.dispatch_record_one.get_vehicle(2.222) is None)

    # Testing get_route function
    # This patch will allow us to manage the function/database responses
    @mock.patch('dispatch.Dispatch.get_route')
    def test_get_route(self, mock_get_route):
        print('Testing test_get_route')

        # Setting up mocks for our tests
        source_coordinates = {'latitude': 30.2672, 'longitude': -97.7431}
        dest_coordinates = {'latitude': 30.2651, 'longitude': -97.7471}
        mock_get_route.return_value = 'mapbox_route'

        # Trying to get a mapbox route
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.dispatch_record_one.get_route(source_coordinates, dest_coordinates) is not None)
        self.assertTrue(self.dispatch_record_two.get_route(dest_coordinates, source_coordinates) is not None)

        # TODO: Ask maps how mapbox returns "invalid" requests


if __name__ == '__main__':
    TestCase.main()
