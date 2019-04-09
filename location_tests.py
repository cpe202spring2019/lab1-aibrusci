import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        # test repr for loc
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        # test repr for loc2
        loc2 = Location("Italy", 10, 100.5)
        self.assertEqual(repr(loc2),"Location('Italy', 10, 100.5)")
        # test that repr for loc does not equal repr for loc2
        self.assertFalse(repr(loc) == "Location('Italy', 10, 100.5)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("Italy", 10, 100.5)
        # test loc1 does not equal loc3
        self.assertFalse(loc1 == loc3)
        # test loc1 equals loc2
        self.assertEqual(loc1, loc2)

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        # test name attribute
        self.assertEqual(loc.name, "SLO")
        # test latitude attribute
        self.assertEqual(loc.lat, 35.3)
        # test longitude attribute
        self.assertEqual(loc.lon, -120.7)


if __name__ == "__main__":
        unittest.main()

