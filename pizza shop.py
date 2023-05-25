import csv
import random

def select_items(items, item_type):
    selected_items = []

    print(f"{item_type.capitalize()}s available:")
    for item, price in items.items():
        print(f"{item} - Rs{price}")

    while True:
        choice = input(f"Select a pizza or 'No' to proceed to checkout: ")

        if choice.upper() == "NO":
            break

        if choice in items:
            selected_items.append(choice)

    return selected_items

name = input("Enter your name: ")
order_id = random.randint(0, 99999)

pizza_shop = {
    "cheese": 500,
    "veg": 600,
    "chicken": 700
}

topping_shop = {
    "olive": 50,
    "extracheese": 100,
    "mushroom": 150
}

# Select pizzas
pizza_selected = select_items(pizza_shop, "pizza")

# Select toppings
topping_selected = select_items(topping_shop, "topping")

total = 0
for pizza in pizza_selected:
    subtotal = pizza_shop[pizza] + sum(topping_shop[topping] for topping in topping_selected)
    print(f"{pizza} with {', '.join(topping_selected)} - Subtotal: Rs{subtotal}")
    total += subtotal

print("Total: Rs" + str(total))

# Writing order details to a CSV file
with open("order_details.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Pizza", "Toppings", "Order ID", "Total"])
    writer.writerow([name, ", ".join(pizza_selected), ", ".join(topping_selected), order_id, total])

print("Thank you for your order,Pls visit again")
print("Order details saved to order_details.csv")
