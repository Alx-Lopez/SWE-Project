import unittest
import vehiclesim


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self):
        self.test_Vehicle_1 = vehiclesim.Vehicle("123", 123.00, 123.00 ,"Available")
        self.test_Vehicle_2 = vehiclesim.Vehicle("123", 123.00, 123.00, "Available")
        self.test_Vehicle_3 = vehiclesim.Vehicle("123", 123.00, 123.00, "Available")
        self.test_Vehicle_4 = vehiclesim.Vehicle("123", 123.00, 123.00, "Available")

    def tearDown(self):
        pass

    def test_vin(self):
        self.assertEqual(self.test_Vehicle_1.vehicle_id,'123',"DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_2.vehicle_id, '123', "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_3.vehicle_id, '123', "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_4.vehicle_id, '123', "DOES NOT EQUAL")

    def test_lat(self):
        self.assertEqual(self.test_Vehicle_1.lat, 123.00, "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_2.lat, 123.00, "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_3.lat, 123.00, "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_4.lat, 123.00, "DOES NOT EQUAL")

    def test_long(self):
        self.assertEqual(self.test_Vehicle_1.long,123.00,"DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_2.long, 123.00, "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_3.long, 123.00, "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_4.long, 123.00, "DOES NOT EQUAL")

    def test_status(self):
        self.assertEqual(self.test_Vehicle_1.status,"Available","DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_2.status, "Available", "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_3.status, "Available", "DOES NOT EQUAL")
        self.assertEqual(self.test_Vehicle_4.status, "Available", "DOES NOT EQUAL")

    def test_heartbeat(self):
        pass
    def test_route(self):
        pass


if __name__ == '__main__':
    unittest.main()
