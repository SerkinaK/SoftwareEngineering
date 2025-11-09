import time
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"\nВремя выполнения: {end_time - start_time:.6f} секунд")

    return wrapper

@timer
def fibonacci():
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()