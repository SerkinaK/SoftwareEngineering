class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car): # Наследование от Car
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model) # вызываем конструктор родительского класса
        self.battery_capacity = battery_capacity # добавляем новый атрибут

    def charge(self): #создаем уникальный метод для класса ElectricCar
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive() # используем унаследованный метод
my_electric_car.charge() # используем собственный метод