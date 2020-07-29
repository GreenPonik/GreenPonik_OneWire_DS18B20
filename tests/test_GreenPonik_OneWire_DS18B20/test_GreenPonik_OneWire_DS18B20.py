# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from GreenPonik_OneWire_DS18B20.GreenPonik_OneWire_DS18B20 import read_temps


class TestGreenPonik_OneWire_DS18B20(unittest.TestCase):

    def test_read_temps(self):
        self.assertTrue(self, type(read_temps()).__name__ == "list")


if __name__ == '__main__':
    unittest.main()
