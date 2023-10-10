import re

number_inputs = int(input())
search_pattern = r"([A-Z][a-z]{2,} [A-Z][a-z]{2,})#+((?:\&{0,1}[A-Z][A-Za-z]+){1,3})\d{2}([A-Z][A-Za-z\d]+ (Ltd.|JSC))"
for entry in range(number_inputs):
    entry = input()

    results = re.findall(search_pattern, entry)
    for result in results:
        if len(result) > 1:
            name = result[0]
            possition = result[1].split('&')
            job = result[2]
            possition = " ".join(possition)
            print(f"{name} is {possition} at {job}")


