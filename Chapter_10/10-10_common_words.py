def count_word(filename, word):
	"""Count the approximate number of times a word appears in the file."""
	with open(filename, encoding='utf-8') as f:
		content = f.read()

		number = content.lower().count(word)
		print(f"'{word}' appears {number} times in {filename}.")


filenames = 'frankenstein.txt', 'arsene_lupin.txt', 'dr_jekyll_and_mr_hyde.txt', 'the_king_james_bible.txt'

print("The number of appearances of 'the':")
for filename in filenames:
	count_word(filename, 'the')

print("\nThe number of appearances of 'the ':")
for filename in filenames:
	count_word(filename, 'the ')


print("\nFrankenstein; or, The Modern Prometheus:")
count_word('frankenstein.txt', 'frankenstein')
count_word('frankenstein.txt', 'monster')
count_word('frankenstein.txt', 'creature')
count_word('frankenstein.txt', 'created')
count_word('frankenstein.txt', 'life')

print("\nThe Extraordinary Adventures of Arsène Lupin, Gentleman-Burglar:")
count_word('arsene_lupin.txt', 'arsène lupin')
count_word('arsene_lupin.txt', 'arsène')
count_word('arsene_lupin.txt', 'lupin')

print("\nThe Strange Case of Dr. Jekyll and Mr. Hyde:")
count_word('dr_jekyll_and_mr_hyde.txt', 'henry')
count_word('dr_jekyll_and_mr_hyde.txt', 'jekyll')
count_word('dr_jekyll_and_mr_hyde.txt', 'edward')
count_word('dr_jekyll_and_mr_hyde.txt', 'hyde')
count_word('dr_jekyll_and_mr_hyde.txt', 'mad')
count_word('dr_jekyll_and_mr_hyde.txt', 'potion')

print("\nThe King James Bible:")
count_word('the_king_james_bible.txt', 'god')
count_word('the_king_james_bible.txt', 'lord')
count_word('the_king_james_bible.txt', 'jesus')
count_word('the_king_james_bible.txt', 'christ')
count_word('the_king_james_bible.txt', 'saviour')
count_word('the_king_james_bible.txt', 'said')
count_word('the_king_james_bible.txt', 'faith ')