from random import randint

def throw():
    number = randint(1, 6)
    print(f"Значение кубика: {number}")
    if number == 5 or number == 6:
        print("Вы победили")
    elif number == 3 or number == 4:
        throw()
    elif number == 1 or number == 2:
        print("Вы проиграли")

if __name__ == '__main__':
    throw()