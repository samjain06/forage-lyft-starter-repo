from .interface_tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
