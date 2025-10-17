def count_digit(input_str):
    frequency = {}
    for char in input_str:
        digit = int(char)
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    res = dict(sorted_items[:3])
    keys = sorted(res.keys())
    for digit in sorted(res.keys()):
        count = res[digit]
        print(f"Цифра {digit}: встретилась {count} раз(а)")
    return res
count_digit(str(input()))
