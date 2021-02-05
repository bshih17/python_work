first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

full_name = "{} {}".format(last_name, first_name)
print(full_name)




print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")



favorite_language = ' python '
print(f"{favorite_language} 2 spaces")
print(f"{favorite_language.rstrip()} 1 space")

favorite_language = '         python     '
print(f"Hi {favorite_language} spaces")
print(f"Hi {favorite_language.strip()} 1 space")

