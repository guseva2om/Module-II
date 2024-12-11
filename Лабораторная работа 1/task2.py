from task_1 import Laptop, Car, Bicycle # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # Инстанцируем все описанные классы
    bike = Bicycle("Giant", "Escape 3", 21)
    car = Car("Toyota", "Camry", 2015)
    laptop = Laptop("Dell", "XPS 13", 8)
    # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        print(bike.ride(-510)) # TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        print(car.drive(-120)) # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        print(laptop.upgrade_ram(-4)) # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')
