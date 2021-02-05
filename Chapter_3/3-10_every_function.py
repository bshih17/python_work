apostles = ['Simon Peter', 'Andrew', 'James of Zebedee', 'John of Zebedee', 'Philip', 'Bartholomew', 'Matthew the tax collector aka Levi of Alphaeus', 'Thomas called the Twin/Didymus', 'James of Alphaeus', 'Lebbaeus Thaddeus aka Judas of James', 'Simon the Cananite and Zealot', 'Judas Iscariot of Simon']

print(apostles)
print(f"\nJesus chose {len(apostles)} apostles.")

print(f"The first disciple Jesus said 'Follow Me' to was {apostles[4]}.")

print(f"\n{apostles[11]} betrayed Jesus and his office was replaced.")
apostles[11] = 'Matthias'
print(f"He was replaced by {apostles[11]}.")

print(f"\nThere were several other people noted to be apostles that were not from the original 12.")
apostles.append('Saul of Tarsus aka Paul')
apostles.append('Joses aka Barnabas, a Levite of Cyprus')
apostles.append('Andronicus')
apostles.append('Junia')
apostles.append('The brethren of the Lord?')
apostles.append("James the Lord's brother")
apostles.append("Ephaphroditus")

print(f"Also, Jesus is the first apostle. He's the Apostle and High Priest of our confession.")
apostles.insert(0, 'Christ Jesus')

print("\nSo, here's the list so far:")
print(apostles)
print(f"That is at least {len(apostles)} apostles.")

brethren_of_the_Lord = ["James the Lord's brother aka James the less", 'Joses', 'Simon', 'Judas']
del apostles[17]
apostles.pop(17)

apostles.append('Joseph called Barsabas surnamed Justus')
print(f"\n{apostles[18]} was also considered as a possible apostle.")
apostles.remove('Joseph called Barsabas surnamed Justus')
print(f"Never mind, the lot fell on {apostles[12]}.")

apostles.append(brethren_of_the_Lord[0])
apostles.append(brethren_of_the_Lord[1])
apostles.append(brethren_of_the_Lord[2])
apostles.append(brethren_of_the_Lord[3])

print(f"\nSo here's the finalized list, assuming that the 4 brothers of Jesus mentioned in Scripture are all apostles:")
print(apostles)

apostles.sort()
print(apostles)

apostles.sort(reverse=True)
print(apostles)

print(sorted(apostles))
print(sorted(apostles, reverse=True))

apostles.reverse()
print(apostles)

print(f"There are {len(apostles)} apostles in this list.")

