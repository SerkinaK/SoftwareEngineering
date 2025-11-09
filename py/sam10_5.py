class NegativeNumberError(Exception):

    def __init__(self, value, message="Отрицательные числа не допускаются"):
        self.value = value
        self.message = f"{message}: {value}"
        super().__init__(self.message)

def calculate_square_root(number):
    try:
        if number < 0:
            raise NegativeNumberError(number, "Невозможно вычислить корень из отрицательного числа")
        result = number ** 0.5
        print(f"Квадратный корень из {number} = {result:.2f}")
        return result
    except NegativeNumberError as e:
        print(e)
        return None

if __name__ == '__main__':
    calculate_square_root(16)
    calculate_square_root(-9)
    calculate_square_root(0)