import doctest
class Laptop:
    def __init__(self, brand: str, model: str, ram: int):
        """
        Инициализация ноутбука.

        :param brand: Бренд ноутбука.
        :param model: Модель ноутбука.
        :param ram: Объем оперативной памяти в гигабайтах (больше 0).
        :raises ValueError: Если объем оперативной памяти меньше 0.
        """
        if ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом.")

        self.brand = brand
        self.model = model
        self.ram = ram

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличение объема оперативной памяти.

        :param additional_ram: Дополнительный объем оперативной памяти в гигабайтах (больше 0).
        :raises ValueError: Если дополнительный объем оперативной памяти не положительный.

        >>> laptop = Laptop("Dell", "XPS 13", 8)
        >>> laptop.upgrade_ram(4)
        >>> laptop.ram
        12
        """
        if additional_ram <= 0:
            raise ValueError("Дополнительный объем оперативной памяти должен быть положительным.")

        self.ram += additional_ram

    def get_info(self) -> str:
        """
        Получение информации о ноутбуке.

        :return: Строка с информацией о ноутбуке.

        >>> laptop = Laptop("Dell", "XPS 13", 8)
        >>> laptop.get_info()
        'Ноутбук Dell XPS 13 с 8 ГБ оперативной памяти.'
        """
        return f'Ноутбук {self.brand} {self.model} с {self.ram} ГБ оперативной памяти.'


class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация автомобиля.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля (должен быть не меньше 1886).
        :raises ValueError: Если год выпуска меньше 1886.
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")

        self.make = make
        self.model = model
        self.year = year

    def get_age(self) -> int:
        """
        Получение возраста автомобиля.

        :return: Возраст автомобиля в годах.

        >>> car = Car("Toyota", "Camry", 2015)
        >>> car.get_age()
        8
        """
        current_year = 2023  # Можно заменить на datetime.datetime.now().year
        return current_year - self.year

    def drive(self, distance: float) -> str:
        """
        Поездка на автомобиле на определенное расстояние.

        :param distance: Расстояние в километрах (больше 0).
        :raises ValueError: Если расстояние меньше 0.
        :return: Строка с сообщением о поездке.

        >>> car = Car("Toyota", "Camry", 2015)
        >>> car.drive(100)
        'Вы проехали 100 км на Toyota Camry.'
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным.")

        return f'Вы проехали {distance} км на {self.make} {self.model}.'


class Bicycle:
    def __init__(self, brand: str, model: str, gear_count: int):
        """
        Инициализация велосипеда.

        :param brand: Бренд велосипеда.
        :param model: Модель велосипеда.
        :param gear_count: Количество передач (больше 0).
        :raises ValueError: Если количество передач меньше нуля.
        """
        if gear_count <= 0:
            raise ValueError("Количество передач должно быть положительным.")

        self.brand = brand
        self.model = model
        self.gear_count = gear_count

    def ride(self, distance: float) -> str:
        """
        Поездка на велосипеде на определенное расстояние.

        :param distance: Расстояние в километрах (больше 0).
        :raises ValueError: Если расстояние меньше 0.
        :return: Строка с сообщением о поездке.

        >>> bike = Bicycle("Giant", "Escape 3", 21)
        >>> bike.ride(10)
        'Вы проехали 10 км на велосипеде Giant Escape 3.'
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным.")

        return f'Вы проехали {distance} км на велосипеде {self.brand} {self.model}.'

    def get_info(self) -> str:
        """
        Получение информации о велосипеде.

        :return: Строка с информацией о велосипеде.

        >>> bike = Bicycle("Giant", "Escape 3", 21)
        >>> bike.get_info()
        'Велосипед Giant Escape 3 с 21 передачей.'
        """
        return f'Велосипед {self.brand} {self.model} с {self.gear_count} передачей.'


if __name__ == "__main__":
    doctest.testmod()