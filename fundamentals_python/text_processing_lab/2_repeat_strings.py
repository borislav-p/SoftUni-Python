words = input().split(" ")
result = [word * len(word) for word in words]
print(f"".join(result))