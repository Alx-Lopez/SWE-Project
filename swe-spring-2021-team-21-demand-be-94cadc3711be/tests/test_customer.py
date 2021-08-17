from unittest import TestCase, mock
import sys
sys.path.insert(1, '../')
from customer import Customer


class TestCustomer(TestCase):

    # TODO: include more test cases
    # This will build these customers before every test case
    def setUp(self):
        print('setup')

        # Customers we regularly use within our test cases
        self.customer = Customer('larryboy@vt.com')

    # Called after every test case, assuming setUp() was successful
    def tearDown(self):
        print('tearDown\n')

    # Testing placeOrder function
    # This patch will allow us to manage the database response
    # TODO: improve our use of mock
    @mock.patch('customer.Customer.place_order')
    def test_place_order(self, mock_place_order):
        print('Testing test_placeOrder')

        # Setting up the rest of the patch
        mock_place_order.return_value = {'success': True, 'order_number': '1', 'vehicle': {'vehicle_number': '12WE56'}}

        # Trying to place an order
        # We get three return values when placing an order,
        # so we need to test all three
        response = self.customer.place_order('test_addr', 'plugin')
        response_success = response['success']
        response_order_number = response['order_number']
        response_vehicle = response['vehicle']
        self.assertTrue(response_success)
        self.assertTrue(response_order_number is not None)
        self.assertTrue(response_vehicle is not None)

        # Setting up the patch for our next test
        mock_place_order.return_value = {'success': False, 'order_number': None, 'vehicle': None}

        # Trying to place an invalid order
        response = self.customer.place_order('invalid', 'invalid')
        response_success = response['success']
        response_order_number = response['order_number']
        response_vehicle = response['vehicle']
        self.assertFalse(response_success)
        self.assertTrue(response_order_number is None)
        self.assertTrue(response_vehicle is None)


if __name__ == '__main__':
    TestCase.main()
