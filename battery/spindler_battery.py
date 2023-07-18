from .interface_battery import Battery
from datetime import date


class SpindlerBattery(Battery):

    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date > self.last_service_date.replace(year=self.last_service_date.year + 3)
