numbers = [10, 25, 8, 45, 30, 45, 12]

numbers = list(set(numbers))

numbers.sort(reverse=True)

print("Second highest number is:", numbers[1])