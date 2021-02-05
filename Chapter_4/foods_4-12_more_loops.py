# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_foods = my_foods doesn't make a copy of the list
# It makes the 2 lists the SAME list.
# Both variables, friend_foods and my_foods, would point to the same list.

my_foods.append('cannoli')
friend_foods.append('ice cream')
sorted(my_foods)

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 4-12 More Loops
print("\nMy favorite foods are:")
for food in my_foods: print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods: print(food)