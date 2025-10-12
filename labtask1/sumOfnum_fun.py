def sum_of_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum =", sum_of_numbers(5, 10, 15, 20))