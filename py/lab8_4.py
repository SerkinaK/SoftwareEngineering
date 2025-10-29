class Car:
    def __init__(self, make, model):
        self._make = make # защищенный атрибут
        self.__model = model # приватный атрибут

    def drive(self):
        print(f"Driving the {self._make} {self.__model}") # метод имеет доступ ко всем атрибутам

my_car = Car("Toyota", "Corolla")
print(my_car._make) # вызова защищенного атрибута
my_car.drive() # вызов метода