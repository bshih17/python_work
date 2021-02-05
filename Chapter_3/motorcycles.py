motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# replacing
motorcycles[0] = 'ducati'
print(motorcycles)

# append
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# starting with an empty list allows users to input data for the list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert
motorcycles.insert(0, 'ducati')
print(motorcycles)

# delete
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles [0]
print(motorcycles)

# pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned.title()}.")

# remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too too_expensive for me.")

