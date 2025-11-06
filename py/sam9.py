class Tomato:
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зеленый',
        3: 'красный'
    } # Храним все стадии созревания помидоров
    def __init__(self, index):
        self._index = index # хранит индекс помидора
        self._state = 0  # указвает начальную стадию созревания

    def grow(self): #Перводим томат в новую стадию созревания
        if self._state < 3:
            self._state += 1
            print(f"Помидор {self._index} перешел в стадию: {Tomato.states[self._state]}")
        else:
            print(f"Помидор {self._index} уже полностью созрел")

    def is_ripe(self): # проверка созрел ли помидор
        return self._state == 3

class TomatoBush: # куст с помидорами
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)] # список томатов на кусте

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow() # все томаты на кусте растут одновременно

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes) # проверка все ли томаты на кусте созрели

    def give_away_all(self):
        print(f"Собран урожай с {len(self.tomatoes)} томатов!")
        self.tomatoes = []  # очищаем список томатов

class Gardener: # Класс Садовника

    def __init__(self, name, plant):
        self.name = name  # имя садовника - публичное свойство
        self._plant = plant  # растение, за которым ухаживает садовник - защищённое

    @staticmethod
    def knowledge_base(): # справки по садоводству
        print("СПРАВКА ПО САДОВОДСТВУ")
        print("Стадии созревания томата:")
        for stage, description in Tomato.states.items():
            print(f"  {stage}: {description}")


    def work(self):
        print(f"{self.name} ухаживает за растениями...")
        self._plant.grow_all()  # Заставляем все томаты расти

    def harvest(self): # собираем урожай
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
            return True
        else:
            print(f"{self.name}: Томаты еще не созрели! Нужно продолжать ухаживать.")
            return False

if __name__ == "__main__":
    print("1. ВЫЗОВ СПРАВКИ ПО САДОВОДСТВУ:")
    Gardener.knowledge_base()

    print("2. СОЗДАНИЕ ОБЪЕКТОВ:")
    bush = TomatoBush(3)  # Создаем куст с 3 помидорами
    gardener = Gardener("Иван", bush)  # Создаем садовника с именем Иван
    print(f"Создан садовник: {gardener.name}")
    print(f"Создан куст с {len(bush.tomatoes)} помидорами")

    print("\n3. УХОД ЗА РАСТЕНИЯМИ:")
    gardener.work()  # Первый уход
    gardener.work()  # Второй уход

    print("\n4. ПЕРВАЯ ПОПЫТКА СБОРА УРОЖАЯ:")
    harvest_result = gardener.harvest()
    if not harvest_result:
        print("\nПРОДОЛЖАЕМ УХАЖИВАТЬ:")
        gardener.work()  # Третий уход

        print("\nВТОРАЯ ПОПЫТКА СБОРА УРОЖАЯ:")
        harvest_result = gardener.harvest()
    if not harvest_result:
        print("\n5. ФИНАЛЬНЫЙ УХОД И СБОР УРОЖАЯ:")
        gardener.work()  # Финальный уход
        gardener.harvest()  # Финальный сбор урожая
