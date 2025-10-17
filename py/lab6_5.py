def tuple_sort(trp):
    for elm in trp:
        if not isinstance(elm, int):
            return trp
    return tuple(sorted(trp))
if __name__ == '__main__':
    print(tuple_sort((7,9,10,2,6,1,4)))
    print(tuple_sort((7,9.2,10,2,2,1.5,4)))