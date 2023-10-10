def positive_num(nums):
    return [number for number in nums if int(number) >= 0]


def negative_num(nums):
    return [number for number in nums if int(number) < 0]


def even_num(nums):
    return [number for number in nums if int(number) % 2 == 0]


def odd_num(nums):
    return [number for number in nums if int(number) % 2 != 0]



numbers = input().split(", ")
print(f"Positive: {', '.join(positive_num(numbers))}")
print(f"Negative: {', '.join(negative_num(numbers))}")
print(f"Even: {', '.join(even_num(numbers))}")
print(f"Odd: {', '.join(odd_num(numbers))}")

