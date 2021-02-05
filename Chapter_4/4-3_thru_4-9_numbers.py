# 4.3 Counting to Twenty
print([value for value in range(1,21)])

numbers = [value for value in range(1,21)]
print(numbers)

# 4.4 One Million
# print([value for value in range(1,1000001)])
numbers = [value for value in range(1,1000001)]
# for number in numbers: print(number)

# 4.5 Summing a Million
print(min(numbers))
print(max(numbers))
print(f"The sum of all the numbers from 1 to 1,000,000 is {sum(numbers)}.")

# 4.6 Odd Numbers
numbers = [value for value in range(1,20,2)]
print(f"A list of all the odd numbers from 1 to 20: {numbers}")

# 4.7 Threes
numbers = list(range(3,31,3))
print("\nThe following is a list of multiples of 3 from 3 to 30:")
for number in numbers: print(number)

# 4.8 Cubes
cubes = [integer**3 for integer in range(1,11)]
print("\nThe folowing is a list of cubes of the integers from 1 to 10:")
print(cubes)

# 4.9 Cube Comprehension
for cube in cubes: print(cube)