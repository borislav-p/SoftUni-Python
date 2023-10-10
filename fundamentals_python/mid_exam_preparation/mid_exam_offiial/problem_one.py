experience_needed = float(input())
number_of_battles = int(input())
experience_gained = 0
current_battle = 0
for battles in range(1, number_of_battles + 1):
    current_experience = float(input())
    current_battle += 1
    if current_battle % 3 == 0:
        experience_gained += current_experience * 1.15

    elif current_battle % 5 == 0:
        experience_gained += current_experience * 0.9
    elif current_battle % 15 == 0:
        experience_gained += current_experience * 1.05
    else:
        experience_gained += current_experience

    if experience_gained >= experience_needed:
        break

unsufficient_experience = experience_needed - experience_gained
if experience_gained >= experience_needed:
    print(f"Player successfully collected his needed experience for {current_battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {unsufficient_experience:.2f} more needed.")


