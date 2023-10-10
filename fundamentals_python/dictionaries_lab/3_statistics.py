products_inventory = {}
while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in products_inventory:
        products_inventory[product] = quantity
    else:
        products_inventory[product] += quantity


print("Products in stock:")
product_representations = [f"- {item}: {str(products_inventory[item])}" for item in products_inventory]
print("\n".join(product_representations))

print(f"Total Products: {len(products_inventory)}")
print(f"Total Quantity: {sum(products_inventory.values())}")
