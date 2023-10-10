import re


def emoji_detectors():
    data = input()
    pattern = r"[0-9]|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})"
    result = re.finditer(pattern, data)
    words = {}
    cool_threshold = 1

    for res in result:
        word = res.group()
        if word.isdigit():
            cool_threshold *= int(word)
        else:
            words[word] = 0
            for ch in word:
                if ch != ":" or ch != "*":
                    words[word] += ord(ch)

    print(f"4 emojis found in the text. The cool ones are:")


emoji_detectors()