from datetime import datetime
from interface_battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, current_date: datetime, last_service_date: datetime):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date > self.last_service_date.replace(year=self.last_service_date.year + 2)
