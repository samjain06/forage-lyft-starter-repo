import unittest

from tire.octoprime_tire import OctoprimeTire


class TestTire(unittest.TestCase):

    def test_octoprime_service_true(self):
        tire_wear = [1, 1, 1, 0]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_octoprime_service_false(self):
        tire_wear = [0.7, 0.7, 0.7, 0.8]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
