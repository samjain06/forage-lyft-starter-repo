from .interface_tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        for wear in self.tire_wear:
            if wear >= 0.9:
                return True