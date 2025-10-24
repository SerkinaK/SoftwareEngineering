def add_expense(filename):
    while True:
        expense = input("Введите описание расхода и сумму: ")
        if expense.lower() == 'выйти':
            break
        if expense.strip():
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(expense + "\n")
def show_expenses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        expenses = file.readlines()
        if expenses:
            print("Ваши расходы:")
            for expense in expenses:
                print(expense.strip())
        else:
            print("Расходов нет.")

filename = "expenses.txt"
add_expense(filename)
show_expenses(filename)