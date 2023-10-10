distributors = {}
clients = {}
total_money = 0
while True:
    input_line = input()
    if input_line == "End":
        break
    command = input_line.split(" ")
    if command[0] == "Deliver":
        distributor_name = command[1]
        money_spend = float(command[2])
        if distributor_name not in distributors:
            distributors[distributor_name] = money_spend
        else:
            distributors[distributor_name] += money_spend

    elif command[0] == "Return":
        distributor_name = command[1]
        money_spend = float(command[2])
        if distributor_name in distributors:
            if distributors[distributor_name] == money_spend:
                del distributors[distributor_name]
            elif distributors[distributor_name] > money_spend:
                distributors[distributor_name] -= money_spend

    elif command[0] == "Sell":
        client_name = command[1]
        money_earned = float(command[2])
        if client_name not in clients:
            clients[client_name] = money_earned
            total_money += money_earned
        else:
            clients[client_name] += money_earned
            total_money += money_earned

for key, value in clients.items():
    print(f"{key}: {value:.2f}")
print("-----------")
for key, value in distributors.items():
    print(f"{key}: {value:.2f}")
print("-----------")
print(f"Total Income: {total_money:.2f}")
