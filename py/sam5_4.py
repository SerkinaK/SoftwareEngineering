first = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
second = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
third = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
def new(grades):
    result = []
    for grade in grades:
        if grade == 2:
            continue
        if grade == 3:
            result.append(4)
        else:
            result.append(grade)
    return result
print(new(first))
print(new(second))
print(new(third))