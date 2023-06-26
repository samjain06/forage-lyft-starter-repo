from car.car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from datetime import date


class CarFactory:

    @staticmethod
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        _engine = CapuletEngine(current_mileage, last_service_mileage)
        _battery = SpindlerBattery(current_date, last_service_date)
        _car = Car(_engine, _battery)
        return _car

    @staticmethod
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        _engine = WilloughbyEngine(current_mileage, last_service_mileage)
        _battery = SpindlerBattery(current_date, last_service_date)
        _car = Car(_engine, _battery)
        return _car

    @staticmethod
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        _engine = SternmanEngine(warning_light_on)
        _battery = SpindlerBattery(current_date, last_service_date)
        _car = Car(_engine, _battery)
        return _car

    @staticmethod
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        _engine = WilloughbyEngine(current_mileage, last_service_mileage)
        _battery = NubbinBattery(current_date, last_service_date)
        _car = Car(_engine, _battery)
        return _car

    @staticmethod
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        _engine = CapuletEngine(current_mileage, last_service_mileage)
        _battery = NubbinBattery(current_date, last_service_date)
        _car = Car(_engine, _battery)
        return _car
