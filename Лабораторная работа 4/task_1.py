# TODO: описать базовый класс для транспортных средств
class Vehicle:
    def __init__(self, name: str, vehicle_type: str):
        self._name = name
        self._vehicle_type = vehicle_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def vehicle_type(self) -> str:
        return self._vehicle_type

    def sound(self) -> str:
        return "Гул двигателя"

    def __str__(self) -> str:
        return f"Транспортное средство {self.name}, тип {self.vehicle_type}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, vehicle_type={self.vehicle_type!r})"

# TODO: описать дочерний класс для автомобилей
class Car(Vehicle):
    def __init__(self, name: str, vehicle_type: str, engine_capacity: float):
        super().__init__(name, vehicle_type)
        self._engine_capacity = engine_capacity

    @property
    def engine_capacity(self) -> float:
        return self._engine_capacity

    def sound(self) -> str:
        return "Рев мотора"

    def __str__(self) -> str:
        return f"Автомобиль {self.name}, тип {self.vehicle_type}, объем двигателя {self.engine_capacity} л"

# TODO: описать дочерний класс для самолетов
class Airplane(Vehicle):
    def __init__(self, name: str, vehicle_type: str, wing_span: float):
        super().__init__(name, vehicle_type)
        self._wing_span = wing_span

    @property
    def wing_span(self) -> float:
        return self._wing_span

    def sound(self) -> str:
        return "Шум турбин"

    def __str__(self) -> str:
        return f"Самолет {self.name}, тип {self.vehicle_type}, размах крыльев {self.wing_span} м"
