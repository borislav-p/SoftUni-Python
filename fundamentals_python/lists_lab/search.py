number = int(input())
word = input()
first_list = []

for _ in range(number):
    current_string = input()
    first_list.append(current_string)

print(first_list)
for i in range(len(first_list) - 1, -1, -1):
    element = first_list[i]
    if word not in element:
        first_list.remove(element)
print(first_list)