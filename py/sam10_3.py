def add_two():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two()
    add_two()
    add_two()