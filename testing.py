import unittest

from parser import *


class TestParser(unittest.TestCase):

    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B', 'CUSTOMER_C']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)


if __name__ == '__main__':
    unittest.main()
