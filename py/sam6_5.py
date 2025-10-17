def sieve(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    unique_list.reverse()
    result = tuple(unique_list)
    return result

print(sieve([1, 2, 3, 2, 1, 4, 5]))
print(sieve([3, 3, 3, 3]))
print(sieve([1, 2, 3, 4, 5]))