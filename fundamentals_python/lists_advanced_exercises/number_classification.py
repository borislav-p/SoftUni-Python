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



#numbers = [int(number) for number in input().split(", ")]
#print(f"Positives: {', '.join(str(number) for number in numbers if number >= 0)}")
#print(f"Negatives: {', '.join(str(number) for number in numbers if number < 0)}")
#print(f"Even: {', '.join(str(number) for number in numbers if number % 2 == 0)}")
#print(f"Odd: {', '.join(str(number) for number in numbers if number % 2 != 0)}")

