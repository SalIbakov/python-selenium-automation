# Level 1
# Task |

def BinGo(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            print('BinGo')
        elif i % 3 == 0:
            print('Go')
        elif i % 7 == 0:
            print('Bin')
        else:
            print(i)


BinGo(100)


# Task ||

def sum_numbers(n: int):
    final_sum = 0
    for i in range(1, n + 1):
        sum_of_digits = n % 10
        final_sum = final_sum + sum_of_digits
        n = n // 10
    return final_sum


n = 444
test_result = sum_numbers(n)
print(test_result)


# Level 2
# Task |

def find_max(n1: int, n2: int, n3: int):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

n1 = 20
n2 = 86
n3 = 65

max_number = find_max(n1, n2, n3)
print(max_number)

# Task ||
def leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

year = 2023
is_leap_year = leap_year(year)
print(is_leap_year)

# Level 3

def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
        next_fibonacci = fib_sequence[-1] + fib_sequence[-2]
        # Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(next_fibonacci)

    return fib_sequence

print(generate_fibonacci_sequence(n))
