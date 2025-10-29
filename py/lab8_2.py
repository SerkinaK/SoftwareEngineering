class Car: #объявляем класс
    def __init__(self, make, model): #конструктор класса, который принимает 2 параметра
        self.make = make
        self.model = model

    def drive(self): #добавляем метод класса
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создаем экземпляр класса
my_car.drive() #вызываем метод для созданного объекта