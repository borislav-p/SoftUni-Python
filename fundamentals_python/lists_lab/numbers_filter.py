number = int(input())
numbers_list = []
filtered_numbers = []
for i in range(number):
    current_number = int(input())
    numbers_list.append(current_number)
command = input()
if command == "even":
    for number in numbers_list:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == "odd":
    for number in numbers_list:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == "negative":
    for number in numbers_list:
        if number < 0:
            filtered_numbers.append(number)
elif command == "positive":
    for number in numbers_list:
        if number >= 0:
            filtered_numbers.append(number)
print(filtered_numbers)