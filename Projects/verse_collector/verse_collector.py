filename = 'KJV.txt'

# Suppose I want to copy and paste Genesis 1:1-3.

with open(filename) as f:
	bible_list = f.readlines()

sample_verses = bible_list[0] + bible_list[1] + bible_list[2] + bible_list[3] + bible_list[4] + bible_list[5] + bible_list[6] + bible_list[7]
# print(sample_verses)


# Create a dictionary
# keys are the verse addresses
# values are the verses
bible_dictionary = {}

for i in range(0,  int(len(bible_list)/3)  ):
	bible_dictionary.update( {bible_list[3*i].strip() : bible_list[3*i+1].strip()} )

# print(bible_dictionary)


# Example:
# Print Genesis 1:1-3
verse_address = input("What verses would you like to print? ")




print(verse_address + " (KJV)")

print(bible_dictionary['$$ Genesis 1:1'])

print(bible_dictionary['$$ John 1:1'])

print(bible_dictionary['$$ John 14:12'])
