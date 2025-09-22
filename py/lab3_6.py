string = "Привет всем изучающим Pyton!"
value = input("Введите букву: ")
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква {value} есть в строке под индексом {index}")
        break
else:
    print(f"Буквы {value} нет в строке")