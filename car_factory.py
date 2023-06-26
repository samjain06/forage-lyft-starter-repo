from car.car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        _engine = CapuletEngine(current_mileage, last_service_mileage)
        _battery = SpindlerBattery(current_date, last_service_date)
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        _engine = WilloughbyEngine(current_mileage, last_service_mileage)
        _battery = SpindlerBattery(current_date, last_service_date)
        return Car(_engine, _battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        _engine = SternmanEngine(warning_light_on)
        _battery = SpindlerBattery(current_date, last_service_date)
        return Car(_engine, _battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        _engine = WilloughbyEngine(current_mileage, last_service_mileage)
        _battery = NubbinBattery(current_date, last_service_date)
        return Car(_engine, _battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        _engine = CapuletEngine(current_mileage, last_service_mileage)
        _battery = NubbinBattery(current_date, last_service_date)
        return Car(_engine, _battery)
