# 3-4 Guest List
guests = ['Paul', 'Barnabas', 'Stephen', 'Antipas']

print(f"Dear {guests[0]}, you are invited to my dinner.")
print(f"Dear {guests[1]}, I am inviting you to my supper celebration.")
print(f"Dearly beloved {guests[2]}, you have been invited to my banquet. It would be an honor for you to join us.")
print(f"Faithful {guests[3]}, it is my pleasure and honor to invite you to this celebration and fellowship.")

# 3-5 Changing Guest List
print(f"\"Dear Brother, I can't make it bro. Sincerely, your friend {guests[3]}.\"")

guests[3] = 'Bob'
print(f"Dear {guests[0]}, you are invited to my dinner.")
print(f"Dear {guests[1]}, I am inviting you to my supper celebration.")
print(f"Dearly beloved {guests[2]}, you have been invited to my banquet. It would be an honor for you to join us.")
print(f"hi {guests[3]} whats up, come have dinner with us")

# 3-6 More Guests
print("Dear guests, I have great news! I just found an awesome new place with a bigger dinner table. The new location for the dinner will be at Such-and-Such Place. Sorry for any inconvenience this may cause, but I'm sure you guys will have a great time at our new location. See you all there!")

guests.insert(0, 'Bill')
guests.insert(2, 'John')
guests.append('Chris')

print(f"Dear {guests[0]}, you are invited to my dinner.")
print(f"Dear {guests[1]}, I am inviting you to my supper celebration.")
print(f"Dearly beloved {guests[2]}, you have been invited to my banquet. It would be an honor for you to join us.")
print(f"hi {guests[3]} whats up, come have dinner with us")
print(f"hi {guests[4]} whats up, come have dinner with us")
print(f"hi {guests[5]} whats up, come have dinner with us")
print(f"hi {guests[6]} whats up, come have dinner with us")

# Shrinking Guest List
print("Ok guys, this is terrible. The new dinner table won't arrive in time for the dinner! It's like this whole dinner plan is being orchestrated by a textbook of exercises. Anyways, there's only space for 2 of you guys.")
print(f"Hey {guests.pop(3)}, sorry to do this to you, but you're uninvited.")
print(guests)

print(f"Hey {guests.pop(4)}, you know what? I thought about you and realized I don't really like you anyway. You're uninvited.")
print(guests)

print(f"Hey {guests.pop(4)}, sorry sometimes you're kinda boring, so don't come.")
print(guests)

print(f"Hey {guests.pop(0)}, stay home.")
print(guests)

print(f"Hey {guests.pop(1)}, stay home.")
print(guests)

print(f"You're still invited {guests[0]}.")
print(f"You're still invited {guests[1]}.")

del guests[0]
del guests[0]

print(guests)


# 3-9 Dinner Guests
print(f"There will be {len(guests)} guests joining us because you deleted all of them.")
