from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight: float=10, fuel: float=10, fuel_consumption: float=1):
        """
        Args:
            weight: Weight in pounds.
            fuel: Current fuel value.
            fuel_consumption: Fuel points consumption per distance point.
        """
        super().__init__(weight, fuel, fuel_consumption)

        self.engine = Engine(volume=10, pistons=4)

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine
