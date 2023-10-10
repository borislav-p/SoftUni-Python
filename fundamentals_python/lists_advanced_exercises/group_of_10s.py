numbers = list(map(int, input().split(", ")))
# max_number = max(numbers) // 10
boundary = 0
while len(numbers) > 0:
    group = []
    boundary += 10
    for num in numbers:
        if num <= boundary:
            group.append(num)
    print(f"Group of {boundary}'s: {group}")
    for copy in group:
        if copy in numbers:
            numbers.remove(copy)
