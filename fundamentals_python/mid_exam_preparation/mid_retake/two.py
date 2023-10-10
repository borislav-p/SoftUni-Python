targets = list(map(int, input().split("|")))
total_points = 0
while True:
    command = input()
    if command == "Game over":
        break
    elif command == "Reverse":
        targets.reverse()
    else:
        command = command.split("@")
        current_command = (command[0])
        start_index = int(command[1])
        length = int(command[2])
        if current_command == "Shoot Left":
            if start_index < len(targets):
                difference = length - start_index
                while difference > len(targets):
                    difference -= len(targets)
                current_index = len(targets) - difference
                if targets[current_index] >= 5:
                    targets[current_index] -= 5
                    total_points += 5
                else:
                    total_points += targets[current_index]
                    targets[current_index] = 0
        elif current_command == "Shoot Right":
            if start_index < len(targets):
                difference = length - start_index
                while difference > len(targets):
                    difference -= len(targets)
                current_index = len(targets) - difference
                if targets[current_index] >= 5:
                    targets[current_index] -= 5
                    total_points += 5

print("-".join([str(num) for num in targets]))
print(f"John finished the archery tournament with {total_points} points!")













