def sum_of_three_digit_number(number: int):
    result = 0
    for i in range(3):
        current_number = number % 10
        result = result + current_number
        number = number // 10
    return result

test_result = sum_of_three_digit_number(291)
print(test_result)

