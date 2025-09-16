import sys
import os.path

def main():
	from stats import count_words
	from stats import count_characters
	from stats import sort_dictionaries
	print("Welcome to BookBot!")
	print("Please enter the name of the book file to analyze:")
	book_name = input()
	print(f"Trying to find Book: {book_name}")
	book_name = book_name.strip()
	book_name = book_name.lower()
	filepath ="books/" + book_name.replace(" ","") +".txt"
	if os.path.isfile(filepath) == False:
		print(f"Error: Could not find file {filepath}")
		sys.exit()
	char_count = count_characters(filepath)
	num_words = count_words(filepath)
	char_sort = sort_dictionaries(filepath)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in char_sort:
		if item['char'].isalpha():  # Only print alphabetic characters
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")
main()
