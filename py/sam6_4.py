def extract_subtuple(tup, element):
    if element not in tup:
        return ()
    first_index = tup.index(element)
    try:
        second_index = tup.index(element, first_index + 1)
        return tup[first_index:second_index + 1]
    except ValueError:
        return tup[first_index:]
print(extract_subtuple((1, 2, 3), 8))
print(extract_subtuple((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(extract_subtuple((1, 2, 8, 5, 1, 2, 9), 8))