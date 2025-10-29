class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.__health_status = "здоров"


    def my_name(self):
        print(f"Я {self._name}")

    def my_age(self):
        print(f"Мне уже {self._age} ")

    def get_health_status(self):
        return self.__health_status

    def set_health_status(self, status):
        allowed_statuses = ["здоров", "болен", "на лечении"]
        if status in allowed_statuses:
            self.__health_status = status
            print(f"Статус здоровья изменен на: {status}")
        else:
            print("Недопустимый статус здоровья")

class DomesticAnimal(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner

    def my_owner(self):
        print(f"Мой хозяин - {self.owner}")


my_animal = Animal("кролик", 1)
my_domestic = DomesticAnimal("собака", 3, "Иван")
my_animal.my_name()
my_animal.my_age()
print(f"Статус здоровья: {my_animal.get_health_status()}")
my_animal.set_health_status("на лечении")
my_domestic.my_name()
my_domestic.my_age()
my_domestic.my_owner()
print(f"Статус здоровья: {my_domestic.get_health_status()}")
