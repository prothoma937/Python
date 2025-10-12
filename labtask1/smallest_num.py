numbers = [12, 5, 7, 2, 19, 3]

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)