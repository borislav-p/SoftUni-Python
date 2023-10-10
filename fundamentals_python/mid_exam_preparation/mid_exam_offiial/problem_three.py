price_ratings = input().split(", ")
#price_ratings_digits = list(map(int, input().split(", ")))



entry_point = int(input())
type_of_item = input()
final_left = []
final_right = []
left_part = price_ratings[0:entry_point]
right_part = price_ratings[(entry_point + 1)::]
left_part_int = [int(x) for x in left_part]
right_part_int = [int(x) for x in right_part]
entry_value = int(price_ratings[entry_point])
if type_of_item == "cheap":
    left_part_int[:] = [x for x in left_part_int if x < entry_value]
    right_part_int[:] = [x for x in right_part_int if x < entry_value]
    sum_left = sum(left_part_int)
    sum_right = sum(right_part_int)
    if sum_left >= sum_right:
        print(f"Left - {sum_left}")
    else:
        print(f"Right - {sum_right}")
else:
    if type_of_item == "expensive":
        left_part_int[:] = [x for x in left_part_int if x >= entry_value]
        right_part_int[:] = [x for x in right_part_int if x >= entry_value]
        sum_left = sum(left_part_int)
        sum_right = sum(right_part_int)
        if sum_left >= sum_right:
            print(f"Left - {sum_left}")
        else:
            print(f"Right - {sum_right}")









