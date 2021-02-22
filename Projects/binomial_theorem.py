# Binomial Theorem: using Pascal's Triangle

def get_pascal(n):
	"""Get Pascal's Triangle with n rows"""
	if n == 0:
		pascal = {0: [1]}

	else:
		pascal = {
			0: [1],
			1: [1,1],
			}

		current_row = []
		number = 0

		for current_row in range (2, n+1):
			
			numbers_in_row = []
		
			numbers_in_row.append(1)
	
			for i in range(0, current_row-1):
				number = pascal[current_row-1][i] + pascal[current_row-1][i+1]
				numbers_in_row.append(number)

			numbers_in_row.append(1)

			pascal[current_row]=numbers_in_row

	return pascal


def get_nth_pascal_row(n):
	"""Get nth pascal row starting from n=2"""

	pascal = get_pascal(n)
	
	nth_pascal_row = pascal[n]

	return nth_pascal_row


def get_binomial_expansion(n):
	"""
	Get the binomial expansion for n using Pascal's Triangle
	(x+y)^n =
	"""

	coefficients = get_nth_pascal_row(n)

	binomial_expansion = ''

	for i in range(0, n+1):
		binomial_expansion += f"{coefficients[i]}x^{n-i}y^{i} + "

	binomial_expansion = binomial_expansion[0:len(binomial_expansion)-3]

	return binomial_expansion

pascal = get_pascal(1)
print(pascal)

pascal = get_pascal(3)
print(pascal)

pascal = get_pascal(5)
print(pascal)

row9 = get_nth_pascal_row(8)
print(row9)


print(get_binomial_expansion(0))
print(get_binomial_expansion(1))
print(get_binomial_expansion(2))
print(get_binomial_expansion(3))
print(get_binomial_expansion(4))
print(get_binomial_expansion(9))


# Binomial Theorem: using n choose k

def n_factorial(n):
	"""
	n! = n(n-1)(n-2)*...*3*2*1
	"""

	# if n=3, 3*2*1
	
	# i = 1,2
	# for i = 1, number = 3*(3-1)
	# for i = 2, number = 3*(3-1)*(3-2)
	number = n

	for i in range(1, n):
		number *= n-i

	return number


def n_choose_k(n, k):
	"""n choose k"""

	try:
		if n>=k:
			number = n_factorial(n) / n_factorial(k) / n_factorial(n-k)
			return int(number)

		else:
			bad_input = "n must be greater than or equal to k!"
			return bad_input

	except:
		return 1


def get_binomial_expansion_2(n):
	"""Get the binomial expansion for n using n choose k"""

	binomial_expansion = ''

	for i in range(0, n+1):
		binomial_expansion += f"{n_choose_k(n, i)}x^{n-i}y^{i} + "

	binomial_expansion = binomial_expansion[:len(binomial_expansion)-3]

	return binomial_expansion


print(n_factorial(4))

print(n_choose_k(6, 3))
print(n_choose_k(8, 4))
print(n_choose_k(0, 0))
print(n_choose_k(1, 0))

print(get_binomial_expansion_2(0))
print(get_binomial_expansion_2(1))
print(get_binomial_expansion_2(2))
print(get_binomial_expansion_2(3))
print(get_binomial_expansion_2(4))
