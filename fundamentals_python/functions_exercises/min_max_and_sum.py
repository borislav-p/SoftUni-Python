number = input()
numbers_as_digits = [int(s) for s in number.split()]
min_number = min(numbers_as_digits)
max_number = max(numbers_as_digits)
sum_number = sum(numbers_as_digits)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_number}")

