import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery

class TestBattery(unittest.TestCase):
    def test_nubbin_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
