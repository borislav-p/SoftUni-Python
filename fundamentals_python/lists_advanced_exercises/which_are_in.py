first_list = input().split(", ")
second_list = input().split(", ")
sub_strings = []
for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_word in sub_strings:
            sub_strings.append(first_word)

print(sub_strings)