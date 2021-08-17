#!/usr/bin/python3
from unittest import TestCase, mock
import sys
sys.path.insert(1, '../')
from fleet_manager import FleetManager


class TestFleetManager(TestCase):

    # TODO: include more test cases
    # TODO: improve our use of mock
    # This will build these fleet managers before every test case
    def setUp(self):
        print('setup')
        self.fleet_manager_bob = FleetManager('bobtom@vt.com')
        self.fleet_manager_carl = FleetManager('cgrimes@twd.net')

    # Called after every test case, assuming setUp() was successful
    def tearDown(self):
        print('tearDown\n')

    # Testing the add_fleet function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet_manager.FleetManager.add_fleet')
    def test_add_fleet(self, mock_add_fleet):
        print('Testing test_add_fleet')

        # Setting up our mock for our test cases
        mock_add_fleet.return_value = True

        # Trying to add a new fleet
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_manager_bob.add_fleet('rideShare'))
        self.assertTrue(self.fleet_manager_carl.add_fleet('rideShare'))

        # Setting up our mock for our test cases
        mock_add_fleet.return_value = False

        # Trying to add invalid fleets
        # Our patch should allow these to be tested
        # assuming it reaches the database call
        self.assertFalse(self.fleet_manager_bob.add_fleet('baking'))
        self.assertFalse(self.fleet_manager_bob.add_fleet(2319))
        self.assertFalse(self.fleet_manager_bob.add_fleet(3.14))
        self.assertFalse(self.fleet_manager_bob.add_fleet(None))
        self.assertFalse(self.fleet_manager_bob.add_fleet(''))

    # Testing the delete_fleet function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet_manager.FleetManager.delete_fleet')
    def test_delete_fleet(self, mock_delete_fleet):
        print('Testing test_delete_fleet')

        # Setting up our mock for our test cases
        mock_delete_fleet.return_value = True

        # Trying to remove a fleet
        # We are assuming these FM's own these appropriate fleets
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_manager_bob.delete_fleet('1'))
        self.assertTrue(self.fleet_manager_carl.delete_fleet('2'))

        # Setting up our mock for our test cases
        mock_delete_fleet.return_value = False

        # Trying to remove nonexistent fleets
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertFalse(self.fleet_manager_bob.delete_fleet('1'))
        self.assertFalse(self.fleet_manager_carl.delete_fleet('2'))
        self.assertFalse(self.fleet_manager_bob.delete_fleet('2.222'))
        self.assertFalse(self.fleet_manager_bob.delete_fleet(''))
        self.assertFalse(self.fleet_manager_bob.delete_fleet(None))

    # Testing the select_fleets function
    # This patch will allow us to manage the function/database response
    @mock.patch('fleet_manager.FleetManager.select_fleets')
    def test_select_fleets(self, mock_select_fleets):
        print('Testing test_select_fleets')

        # Setting up our mock for our test cases
        mock_select_fleets.return_value = ({'fleet_id': '12'})

        # Trying to select all the fleets of one FM
        # We are assuming these FM's independently owned the fleet
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_manager_bob.select_fleets() is not None)
        self.assertTrue(self.fleet_manager_carl.select_fleets() is not None)

        # Setting up our mock for our test cases
        mock_select_fleets.return_value = None

        # Trying to select all the fleets of an FM that has no fleets
        # We are assuming this FM is retiring and has decommissioned all their fleets
        # Be sure to wish Bob a happy retirement
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.fleet_manager_bob.select_fleets() is None)


if __name__ == '__main__':
    TestCase.main()
