number_paintings = input()
lst = [int(x) for x in number_paintings.split()]
while True:
    instructions = input()
    if instructions == "END":
        break
    elif instructions == "Reverse":
        lst.reverse()
    else:
        instructions = instructions.split()
        if len(instructions) < 3:
            command = instructions[0]
            index_1 = int(instructions[1])

        else:
            command = instructions[0]
            index_1 = int(instructions[1])
            index_2 = int(instructions[2])
        if command == 'Change':
            if index_1 in lst:
                lst = [index_2 if i == index_1 else i for i in lst]
        elif command == 'Hide':
            if index_1 in lst:
                lst.remove(index_1)
        elif command == 'Switch':
            if index_1 in lst and index_2 in lst:
                a, b = lst.index(index_1), lst.index(index_2)
                lst[b], lst[a] = lst[a], lst[b]
        elif command == 'Insert':
            if len(lst) >= index_1 + 1:
                lst.insert(index_1 + 1, index_2)
print(" ".join([str(num) for num in lst]))