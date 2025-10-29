class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name(self):
        print(f"Я {self.name}")

    def my_age(self):
        print(f"Мне уже {self.age} ")

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
my_domestic.my_name()
my_domestic.my_age()
my_domestic.my_owner()