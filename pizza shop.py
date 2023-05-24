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

# Empty lists created for storing selected pizza and toppings
pizza_selected = []
topping_selected = []

print("Welcome to our Pizza Shop")
print("Pizzas Available in our shop:")

for pizza, price in pizza_shop.items():
    print(f"{pizza} - Rs{price}")

while True:
    choice = input("Select a pizza or 'No' to proceed to checkout: ")

    if choice.upper() == "NO":
        break

    if choice in pizza_shop:
        pizza_selected.append(choice)

print("Toppings available:")
for topping, price in topping_shop.items():
    print(f"{topping} - Rs{price}")

topping_choice = input("Do you want to add toppings? (Yes/No): ")

if topping_choice.lower() == "yes":
    while True:
        topping = input("Select a topping or 'No' to proceed: ")
        if topping.upper() == "NO":
            break
        if topping in topping_shop:
            topping_selected.append(topping)

total = 0
for pizza in pizza_selected:
    subtotal = pizza_shop[pizza] + sum(topping_shop[topping] for topping in topping_selected)
    print(f"{pizza} with {', '.join(topping_selected)} - Subtotal: Rs{subtotal}")
    total += subtotal

print("Total: Rs" + str(total))