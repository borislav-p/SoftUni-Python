string = input()
while True:
    command = input().split(" ")
    if command[0] == "For" and command[1] == "Azeroth":
        break

    elif command[0] == "GladiatorStance":
        string = string.upper()
        print(string)
    elif command[0] == "DefensiveStance":
        string = string.lower()
        print(string)
    elif command[0] == "Dispel":
        index = int(command[1])
        letter = (command[2])
        if len(string) > index >= 0:
            tmp = list(string)
            tmp[index] = letter
            string = "".join(tmp)
            print("Success!")
        else:
            print("Dispel too weak.")

    elif command[0] == "Target" and command[1] == "Change":

        first_string = command[2]
        second_string = command[3]
        if first_string in string:
            string = string.replace(first_string, second_string)
            print(string)
        else:
            print(string)
    elif command[0] == "Target" and command[1] == "Remove":
        substring = command[2]
        if substring in string:
            string = string.replace(substring, "")
            print(string)



    else:
        print("Command doesn't exist!")
