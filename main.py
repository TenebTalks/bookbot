def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count_of_words = count_words(book_text)
    print(f"{count_of_words} words found in {book_path}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_string):
    words_list = book_string.split()
    word_count = len(words_list)
    
    return word_count




main()