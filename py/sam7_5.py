import re

def compare_letters_and_digits(filename):
    with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    russian_letters_count = len(re.findall(r'[а-яА-ЯёЁ]', text))
    digits_count = len(re.findall(r'\d', text))
    if russian_letters_count > digits_count:
        return "В файле больше русских букв."
    elif digits_count > russian_letters_count:
        return "В файле больше цифр."
    else:
        return "Количество русских букв и цифр в файле одинаково."

filename = "new.txt"
result = compare_letters_and_digits(filename)
print(result)