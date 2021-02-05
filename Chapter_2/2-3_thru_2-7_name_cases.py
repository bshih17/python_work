name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name = "JoHn SmItH"
print(name.lower())
print(name.upper())
print(name.title())

print('\nSmith Wigglesworth said, "There are four principles we need to maintain: First, read the Word of God. Second, consume the Word of God until it consumes you. Third, believe the Word of God. Fourth, act on the Word."')

person = "John G. Lake"
quote = '"We cannot exercise our faith beyond what we believe to be possible."'
print(f"\n{person.title()} said, {quote}")



name = "\n\t    T.L. Osborn           "
print(name)
# .lstrip() removes new line and tab before T.L. Osborn.
print(name.lstrip())
print(name.rstrip())
print(name.strip())
# Adding \" at the beginning of the quote and at the end of the quote inserts actually quotations when printed.
quote = "\"You should never ask God to do what he has said He's already done, and you should never ask God to do what He has told you to do.\""
print(f"{name.strip()} said, {quote}")