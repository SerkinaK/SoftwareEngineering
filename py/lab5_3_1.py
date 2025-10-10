def replace(input_list):
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list

print(replace([1, 2, 3, 4, 5]))