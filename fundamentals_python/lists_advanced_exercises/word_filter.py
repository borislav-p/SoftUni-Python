words = input().split()
filtered_words = [word for word in words if 0 == len(word) % 2 == 0]
print("\n".join(filtered_words))