from dataclasses import dataclass
import exceptions


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
            raise exceptions.LowFuelError
        self.started = True

    def move(self, distance: float) -> None:
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed > self.fuel:
            raise exceptions.NotEnoughFuel
        self.fuel -= fuel_needed
