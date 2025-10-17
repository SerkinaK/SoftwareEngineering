def remove_elem(trp,elem):
    tuple_list = list(trp)
    if elem in tuple_list:
        tuple_list.remove(elem)
    return tuple(tuple_list)
print(remove_elem((1, 2, 3), 1))
print(remove_elem((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_elem((2, 4, 6, 6, 4, 2), 9))