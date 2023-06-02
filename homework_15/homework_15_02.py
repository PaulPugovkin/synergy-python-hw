# Создайте класс Autobus, который наследуется от класса Transport.
#
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
#
# Используйте переопределение метода.
#
# Используйте следующий код для родительского класса транспортного средства:

# class Transport:
#
#     def __init__(self, name, max_speed, mileage):
#
#
# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
#
#
# def seating_capacity(self, capacity):
#     return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"


# Ожидаемый результат вывода:
#
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, seatCapacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.seatCapacity = seatCapacity
    def setCapacity(self, seatCapacity):
        self.seatCapacity = seatCapacity
    def seatingCapacity(self):
        return f"Вместимость одного автобуса {self.name}  {self.seatCapacity} пассажиров"

autobus = Autobus('Renault Logan', 80, 1000, 50)

print(autobus.seatingCapacity())
autobus.setCapacity(100)
print(autobus.seatingCapacity())