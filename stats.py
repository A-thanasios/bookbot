def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def char_count_sort(char_count):
    return dict(sorted(char_count.items(), reverse=True, key= lambda x: x[1]))