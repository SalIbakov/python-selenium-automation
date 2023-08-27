def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    print(f"The factorial of {n} is {result}")

factorial(6)