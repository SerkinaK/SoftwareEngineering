def personal_info(name, age, company = 'unnamed'):
    print(f'Имя: {name}, Возраст: {age}, Компания: {company}')
one = ('Григорий',25,'Yandex')
two = ('Григорий',45)
personal_info(*one)
personal_info(*two)