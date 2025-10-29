class Shape: # общий класс
    def area(self):
        pass # абстрактный метод

class Rectangle(Shape): # Класс Прямоугольник, наследуется от Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height # реализация метода поиска площади для прямоугольника

class Circle(Shape): # класс Круг, наследуется от Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius # реализация метода поиска площади для круга

# создаем объекты
my_rectangle = Rectangle(5, 4)
my_circle = Circle(5)
# вызываем методы для поиска площади
print(my_rectangle.area())
print(my_circle.area())