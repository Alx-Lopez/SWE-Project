#!/usr/bin/python3
from unittest import TestCase, mock
import sys
sys.path.insert(1, '../')
from fleet import Fleet


class TestFleet(TestCase):

    # TODO: include more test cases
    # TODO: improve our use of mock
    # This will build these fleets before every test case
    def setUp(self):
        print('setup')
        self.fleet_one = Fleet('23')
        self.fleet_two = Fleet('19')

    # Called after every test case, assuming setUp() was successful
    def tearDown(self):
        print('tearDown\n')

    # Testing the add_vehicle function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet.Fleet.add_vehicle')
    def test_add_vehicle(self, mock_add_vehicle):
        print('Testing test_add_vehicle')

        # Setting up our mock for our tests
        mock_add_vehicle.return_value = True

        # Trying to add vehicles to a fleet
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_one.add_vehicle('1', 'WGV4706'))
        self.assertTrue(self.fleet_one.add_vehicle('2', 'VGW6074'))
        self.assertTrue(self.fleet_two.add_vehicle('22', 'PWR4053'))
        self.assertTrue(self.fleet_two.add_vehicle('21', 'TRY1465'))

        # Setting up our mock for our tests
        mock_add_vehicle.return_value = False

        # Trying to add invalid vehicles to a fleet
        # Our patch should allow this to be tested
        # assuming it reaches the database call
        self.assertFalse(self.fleet_one.add_vehicle('1', 'WGV4706'))
        self.assertFalse(self.fleet_one.add_vehicle('', ''))
        self.assertFalse(self.fleet_one.add_vehicle('24', None))
        self.assertFalse(self.fleet_one.add_vehicle(None, 'MKX7845'))
        self.assertFalse(self.fleet_one.add_vehicle(None, None))
        self.assertFalse(self.fleet_one.add_vehicle(None, ''))
        self.assertFalse(self.fleet_one.add_vehicle('', None))

    # Testing the remove_vehicle function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet.Fleet.remove_vehicle')
    def test_remove_vehicle(self, mock_remove_vehicle):
        print('Testing test_remove_vehicle')

        # Setting up our mock for our tests
        mock_remove_vehicle.return_value = True

        # Trying to remove vehicles from a fleet
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_one.remove_vehicle('1'))
        self.assertTrue(self.fleet_one.remove_vehicle('2'))
        self.assertTrue(self.fleet_two.remove_vehicle('22'))
        self.assertTrue(self.fleet_two.remove_vehicle('23'))

        # Setting up our mock for our tests
        mock_remove_vehicle.return_value = False

        # Trying to remove invalid vehicles
        # Our patch should allow this to be tested
        # assuming it reaches the database call
        self.assertFalse(self.fleet_one.remove_vehicle('1'))
        self.assertFalse(self.fleet_one.remove_vehicle('22'))
        self.assertFalse(self.fleet_one.remove_vehicle(None))
        self.assertFalse(self.fleet_one.remove_vehicle(''))
        self.assertFalse(self.fleet_one.remove_vehicle('2.2222'))
        self.assertFalse(self.fleet_one.remove_vehicle(2.2222))

    # Testing the get_available_vehicle function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet.Fleet.get_available_vehicle')
    def test_get_available_vehicle(self, mock_get_available_vehicle):
        print('Testing test_get_available_vehicle')

        # Setting up our mock for our tests
        mock_get_available_vehicle.return_value = {'vehicle_number': '1', 'license_plate': 'WGV4706'}

        # Trying to get an available vehicle from a fleet
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_one.get_available_vehicle() is not None)
        self.assertTrue(self.fleet_two.get_available_vehicle() is not None)

        # Setting up our mock for our tests
        mock_get_available_vehicle.return_value = None

        # Trying to get an available vehicle from a fleet with no vehicles
        # Our patch should allow us to test this
        # assuming it reaches the database call
        new_fleet = Fleet('3')
        self.assertTrue(new_fleet.get_available_vehicle() is None)

    # Testing the get_all_vehicles function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet.Fleet.get_all_vehicles')
    def test_get_all_vehicles(self, mock_get_all_vehicles):
        print('Testing test_get_all_vehicles')

        # Setting up our mock for our tests
        mock_get_all_vehicles.return_value = {'vehicle': {'vehicle_number': '1', 'license_plate': 'WGV4706'}}

        # Trying to get all the vehicles in a fleet
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_one.get_all_vehicles() is not None)
        self.assertTrue(self.fleet_two.get_all_vehicles() is not None)

        # Setting up our mock for our tests
        mock_get_all_vehicles.return_value = None

        # Trying to get all the vehicles from a fleet with no vehicles
        # Our patch should allow us to test this
        # assuming it reaches the database call
        new_fleet = Fleet('3')
        self.assertTrue(new_fleet.get_all_vehicles() is None)


if __name__ == '__main__':
    TestCase.main()
