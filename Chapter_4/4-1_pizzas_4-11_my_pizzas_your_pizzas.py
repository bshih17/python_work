# 4-1 Pizzas
pizzas = ['pepperoni', "pineapple", "anchovy", "mushroom", "sausage"]
for pizza in pizzas:
	print(f"I would like to order a {pizza} pizza now.")

print("I liked the pineapple pizza, the mushroom pizza, and the anchovy pizza. They were delicious.")

# 4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append('cheese')
friend_pizzas.append('Hawaiian')

print("\nMy favorite pizzas are:")
for pizza in pizzas: print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas: print(pizza.title())

