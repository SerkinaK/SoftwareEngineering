class InputNumberDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        if number > 0:
            print("Введено положительное число")
        elif number < 0:
            print("Введено отрицательное число")
        else:
            print("Введен ноль")

        result = self.func(number)

        return result


class OutputResultDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        result = self.func(number)
        if result > 0:
            print("Результат положительный")
        elif result < 0:
            print("Результат отрицательный")
        else:
            print("Результат ноль")

        return result


@OutputResultDecorator
@InputNumberDecorator
def calculate_square(number):
    result = number ** 2
    print(f" Квадрат {number} = {result}")
    return result

@OutputResultDecorator
@InputNumberDecorator
def double_number(number):
    result = number * 2
    print(f"Удвоенное число {number}  = {result}")
    return result

@OutputResultDecorator
@InputNumberDecorator
def invert_number(number):
    result = -number
    print(f" Инвертированное число {number} = {result}")
    return result

if __name__ == '__main__':
    result1 = calculate_square(4)
    result2 = calculate_square(-3)
    result3 = double_number(5)
    result4 = double_number(-7)
    result5 = invert_number(10)
    result6 = calculate_square(0)