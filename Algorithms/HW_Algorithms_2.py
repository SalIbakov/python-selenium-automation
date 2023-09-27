# Task 1. Reverse a negative integer and keep the negative sign at the beginning.
# Example: -189 -> -981
def reverse_integer(n: int):
    # Convert the integer to a string
    num_str = str(n)

    # Check if the number is negative
    if n < 0:
        # Reverse the string excluding the negative sign
        reversed_str = '-' + num_str[:0:-1]
    else:
        # Reverse the entire string
        reversed_str = num_str[::-1]

    # Convert the reversed string back to an integer
    return int(reversed_str)


result = reverse_integer(-189)
print(result)  # Output: -981

    