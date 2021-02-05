# terms = list(range(1,6))
# print(terms)

# monomial
degree = 5
coefficient = 3

der_degree = degree-1
der_coefficient = degree*coefficient

print(f"if f(x)= {coefficient}x^{degree},")
print(f"then f'(x)= {der_coefficient}x^{der_degree}")

# polynomial
# term = [coefficient, degree]

# eventually, I need to write my code in such a way...
# that the only necessary code to change is the input for the term
# everything else should be automated
term1 = [4,5]
term2 = [3,2]
term3 = [2,1]
all_terms = [term1, term2, term3]


term = [1,1]
der_coefficient = term[1]*term[0]
der_degree = term[1]-1
der_term = [der_coefficient, der_degree]

# the for loop makes a new line for every iteration
# can I make them all the same line?
for value in range(0,3):
    all_terms[value] = (f"{all_terms[value][0]}x^{all_terms[value][1]}")



print (f"\nf(x)= {all_terms[0]} + {all_terms[1]} + {all_terms[2]}")
