import os

menu = {"Mozzarella": 850, "Greek Salad": 440, "Caesar Salad": 720, "Roasted Chicken": 1200, "Club Sandwich": 870,
        "Fried Prawns": 620, "Grilled Salmon": 1100, "Cup of coffee": 210, "Pot of tea": 250, "Fresh Juice": 330,
        "Mineral Water": 110}

print("MENU\n\n")

for course, price in menu.items():
    print(course + "\t\t" + format(price, ".2f") + " RUR")
print("\n\n")

orders = []
order = input("What you would like to have? (Q for quit)")

while (order.upper() != 'Q'):
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")
    order = input("Anything else? (Q for quit)")

print("You have ordered: ", orders)

total = 0

for order in orders:
    total += menu[order]

print("Your total bill is:", total, " RUR")

os.system("pause")





