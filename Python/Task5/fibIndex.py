def fib(n: int):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


def fib_index(n: int):
    i = 0
    fibo = fib(0)
    while fibo < n:
        i += 1
        fibo = fib(i)
        if fibo == n:
            break
        if fibo > n:
            i = -1
            break
    return i


# Tests
print(fib(6))  # 8
print(fib_index(8))  # 6
