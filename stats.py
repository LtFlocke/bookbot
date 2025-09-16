def get_book_text(filepath):
	book_text = ""
	with open(filepath) as f:
		book_text = f.read()
	return book_text

def count_words(filepath):
	book_text = get_book_text(filepath)
	book_words = []
	book_num_words = 0
	book_words = book_text.split()
	book_num_words = len(book_words)
	return book_num_words

def count_characters(filepath):
    book_text = get_book_text(filepath)
    lower_book_text = book_text.lower()
    char_counts = {}
    for char in lower_book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    # Convert to list of dictionaries with "char" and "num" keys
    char_count = [{"char": char, "num": count} for char, count in char_counts.items()]
    return char_count

def sort_dictionaries(filepath):
    def sort_on(items):
        return items["num"]
    char_count = count_characters(filepath)
    char_count.sort(key=sort_on, reverse=True)
    return char_count

    
