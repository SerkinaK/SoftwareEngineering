class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name(self):
        print(f"Я {self.name}")
    def my_age(self):
        print(f"Мне уже {self.age} год")

my_animal = Animal("кролик", 1)
my_animal.my_name()
my_animal.my_age()
