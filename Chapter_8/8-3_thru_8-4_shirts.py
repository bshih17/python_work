# 8-3 T-Shirt
def make_shirt(size, text):
	"""Display shirt size and text on shirt."""
	print(f"The shirt size is {size}, and it will say '{text}'.")

make_shirt('large', "You don't learn anything until you do it")

make_shirt(text = "Just do it", size = 'medium')

# 8-3 Large Shirts
def make_shirt(size = 'large', text = 'I love Python.'):
	print(f"The shirt size is {size}, and it will say '{text}'.")

make_shirt()
make_shirt('medium')
make_shirt(text = 'Write code.')
