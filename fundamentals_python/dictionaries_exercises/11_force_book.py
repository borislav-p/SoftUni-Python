force_side_dict = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        forced_side, forced_user = splitted_command
        present = False
        for value in force_side_dict.values():
            if forced_user in value:
                present = True
                break
        if not present:
            if forced_side not in force_side_dict.keys():
                force_side_dict[forced_side] = [forced_user]
            else:
                force_side_dict[forced_side].append(forced_user)

    else:
        splitted_command = command.split(" -> ")
        forced_user, forced_side = splitted_command
        for key, value in force_side_dict.items():
            if forced_user in value:
                force_side_dict[key].pop(value.index(forced_user))
                break
        if forced_side not in force_side_dict.keys():
            force_side_dict[forced_side] = [forced_user]
        else:
            force_side_dict[forced_side].append(forced_user)
        print(f"{forced_user} joins the {forced_side} side!")

    command = input()

for forced_side in force_side_dict.keys():
    if len(force_side_dict[forced_side]) > 0:
        print(f"Side: {forced_side}, Members: {len(force_side_dict[forced_side])}")
        [print(f"! {user}") for user in force_side_dict[forced_side]]