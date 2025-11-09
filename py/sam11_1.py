def fib(n):
    a, b = 1, 1
    for num in range(n):
        yield a
        a, b = b, a + b

n = 243
fibonacci_numbers = list(fib(n))

print(fibonacci_numbers[-1])