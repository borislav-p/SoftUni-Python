list_of_numbers = input().split(" ")
list_of_numbers_digits = [int(i) for i in list_of_numbers]
number_to_remove = int(input())
for i in range(number_to_remove):
    min_number = min(list_of_numbers_digits)
    list_of_numbers_digits.remove(min_number)
print(*list_of_numbers_digits, sep=', ')
