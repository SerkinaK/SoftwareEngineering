array = [2, 4, 6, 8, 9]
flag = False;
for value in array:
    if value % 2 != 0:
        flag = True
if flag:
    print("В массиве есть нечётное число")
else:
    print("В массиве все числа чётные")
