import unittest

from tire.carrigan_tire import CarriganTire


class TestTire(unittest.TestCase):

    def test_carrigan_service_true(self):
        tire_wear = [0.8, 0.7, 0.9, 0.3]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_carrigan_service_false(self):
        tire_wear = [0.8, 0.7, 0.7, 0.8]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
