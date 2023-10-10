first_index = int(input())
last_index = int(input())
final_string = ""
for character in range(first_index, last_index + 1):
    final_string += chr(character) + " "
    #print(chr(character), end = " ")
print(final_string)