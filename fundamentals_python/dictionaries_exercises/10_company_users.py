companies = {}
command = input().split(" -> ")
while command[0] != "End":
    company, id = command
    if company in companies.keys():
        if id not in companies[company]:
            companies[company].append(id)
    else:
        companies[company] = []
        companies[company].append(id)



    command = input().split(" -> ")

for company in companies.keys():
    print(f"{company}")
    for employee in companies[company]:
        print(f"-- {employee}")