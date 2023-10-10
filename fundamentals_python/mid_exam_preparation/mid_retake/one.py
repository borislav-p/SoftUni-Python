side_size = float(input())
number_of_sheets = int(input())
box_area = side_size * side_size * 6
collected_area = 0
sheet_number = 0
for sheets in range(1, number_of_sheets + 1):
    length = float(input())
    width = float(input())
    sheet_number += 1
    if sheet_number % 5 == 0:
        collected_area = collected_area
    elif sheet_number % 3 == 0:
        collected_area += (length * width) * 0.75
    else:
        collected_area += length * width


if collected_area >= box_area:
    percantage = ((collected_area - box_area) / collected_area) * 100
    print(f"You've covered the gift box!")
    print(f"{percantage:.2f}% wrap paper left.")

else:
    percantage_one = 100 - (collected_area / box_area) * 100
    print("You are out of paper!")
    print(f"{percantage_one:.2f}% of the box is not covered.")




