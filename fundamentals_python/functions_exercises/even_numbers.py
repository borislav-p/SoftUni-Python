numbers_as_digits = [int(s) for s in input().split()]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


#def is_even(number):
#    if int(number) % 2 == 0:
#        return True



#numbers = input().split()
#filtered_numbers = []
#for current_number in numbers:
#    if is_even(current_number):
#        filtered_numbers.append(int(current_number))
#print(filtered_numbers)

