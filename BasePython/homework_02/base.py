from dataclasses import dataclass

from .exceptions import LowFuelError, NotEnoughFuel


@dataclass
class Vehicle:

    weight: float
    fuel: float
    fuel_consumption: float
    started: bool = False

    def start(self) -> None:
        if self.started:
            return
        if self.fuel <= 0:
            raise LowFuelError
        self.started = True

    def move(self, distance: float) -> None:
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed > self.fuel:
            raise NotEnoughFuel
        self.fuel -= fuel_needed
