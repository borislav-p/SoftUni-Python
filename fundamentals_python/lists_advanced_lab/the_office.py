employees_happiness = input().split()
happiness_factor = int(input())

happiness_by_the_factor = list(map(lambda x: int(x) * happiness_factor, employees_happiness))
filtered = list(filter(lambda x: x >= sum(happiness_by_the_factor)/len(employees_happiness), happiness_by_the_factor))


if len(filtered) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are not happy!")
