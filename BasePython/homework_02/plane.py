"""
создайте класс `Plane`, наследник `Vehicle`
"""
from dataclasses import dataclass
from base import Vehicle
from engine import Engine
import exceptions


class Plane(Vehicle):
    def __init__(self, weight: float=100, fuel: float=10, fuel_consumption: float=1,
                 max_cargo: float=50):
        """
        Args:
            weight: Weight in pounds.
            fuel: Current fuel value.
            fuel_consumption: Fuel points consumption per distance point.
            max_cargo: Maximum allowed cargo.
        """
        super().__init__(weight, fuel, fuel_consumption)

        self.engine = Engine(volume=10, pistons=4)
        self.cargo = 0
        self.max_cargo = max_cargo

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine

    def load_cargo(self, cargo: float) -> None:
        new_cargo = cargo + self.cargo
        if new_cargo > self.max_cargo:
            raise exceptions.CargoOverload
        self.cargo = new_cargo

    def remove_all_cargo(self) -> float:
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo
