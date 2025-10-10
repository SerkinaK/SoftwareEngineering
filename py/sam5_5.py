def list_to_set(lst):
    result_set = set()
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)
    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(list_to_set(list_1))
print(list_to_set(list_2))
print(list_to_set(list_3))