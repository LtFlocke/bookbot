import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def main(filepath=sys.argv[1]):
	from stats import count_words
	from stats import count_characters
	from stats import sort_dictionaries
	filepath = filepath
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
