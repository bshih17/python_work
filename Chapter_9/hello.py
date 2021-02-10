class Parent:
	def __init__(self, name):
		print(f"Parent __init__ {name.title()}")

class Child(Parent):
	def __init__(self):
		print('Child__init__ AAAAAAAAAAAAAAAAAAA')
		super().__init__('max')

child = Child()
