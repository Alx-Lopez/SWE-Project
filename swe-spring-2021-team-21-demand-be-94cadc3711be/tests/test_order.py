from unittest import TestCase, mock
import sys
sys.path.insert(1, '../')
from order import Order


class TestOrder(TestCase):

    # TODO: include more test cases
    # This will build this customer and address before every test case
    def setUp(self):
        print('setup')
        address = {
            'street_address': '1234 Main St',
            'city': 'Austin',
            'state': 'TX',
            'zip_code': '78704'
        }
        self.order = Order('12345', address, 'rideShare')
        self.invalid_order = Order(None, None, None)

    # Called after every test case, assuming setUp() was successful
    def tearDown(self):
        print('tearDown\n')

    # Testing record_order function as well as get_address_id since it's necessary for record_order
    # This patch will allow us to manage the database response
    # TODO: improve our use of mock
    @mock.patch('order.Order.record_order')
    @mock.patch('order.Order.get_address_id')
    def test_record_order(self, mock_address, mock_record_order):
        print('Testing test_record_order')

        # Setting up mocks for our test
        mock_address.return_value = '2'
        # initializing an order
        valid_order = Order('12345', 'test_addr', 'plugin')
        # need to directly set instance variables until mock knowledge is improved
        valid_order.order_number = '1'

        # Trying to record an order
        # We are assuming the order is properly constructed
        # Our patch should allow this to work
        # assuming it reaches the database call
        valid_order.record_order()
        self.assertEqual('1', valid_order.order_number)
        self.assertEqual('2', valid_order.get_address_id())

        # Setting up for our next test
        mock_address.return_value = None

        # Trying to record an invalid order
        # Our patch should allow this to be tested
        # assuming it reaches the database call
        self.invalid_order.record_order()
        self.assertEqual(None, self.invalid_order.order_number)
        self.assertEqual(None, self.invalid_order.get_address_id())

    # Testing update_order function
    # This patch will allow us to manage the database response
    # TODO: improve our use of mock
    @mock.patch('order.Order.update_order')
    def test_update_order(self, mock_update_order):
        print('Testing test_update_order')

        # Setting up mock for our test
        mock_update_order.return_value = True

        # Trying to update an order
        # We are assuming the order is properly constructed
        # Our patch should allow this to work
        # assuming it reaches the database call
        self.assertTrue(self.order.update_order())

        # Setting up mock for our test
        mock_update_order.return_value = False

        # Trying to update an invalid order
        # Our patch should allow this to be tested
        # assuming it reaches the database call
        self.assertFalse(self.invalid_order.update_order())


if __name__ == '__main__':
    TestCase.main()
