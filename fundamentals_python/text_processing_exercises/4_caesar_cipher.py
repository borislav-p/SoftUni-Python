text = input()
new_ord = ""
for ch in text:
    ch = (ord(ch) + 3)
    ch = chr(ch)
    new_ord += ch

print(new_ord)
