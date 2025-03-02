from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filepath>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        num_words = get_word_count(get_book_text(path))
        num_char = get_char_count(get_book_text(path))
        num_char_sorted = char_count_sort(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")

    for char in num_char_sorted:
        if char.isalpha():
            print(f"{char}: {num_char_sorted[char]}")

    print("============= END ===============")





#############################
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



main()