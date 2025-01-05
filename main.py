def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count_of_words = count_words(book_text)
    print(f"--- Book report for {book_path} ---")
    print(f"{count_of_words} words found in {book_path}")
    count_each_letter = count_lower_letters(book_text)
    letter_report = character_report(count_each_letter)
    for i in range(0,len(letter_report)):
        print(letter_report[i])
    #print(letter_report)





def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_string):
    words_list = book_string.split()
    word_count = len(words_list)
    
    return word_count

def count_lower_letters(book_to_analyze):
    lowercase_string = book_to_analyze.lower()
    chars_dict = {}
    for char in lowercase_string:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1





    #print(letters_dict)
    return chars_dict


def sort_by_count(dict):
    return dict["count"]


def character_report(dict_of_chars):
    alpha_list = []
    junk_list = []
    printable_list = []
    for char in dict_of_chars:
        count = dict_of_chars[char]
        if char.isalpha():
            char_dict = {
                "name": char,
                "count": count
            }
            alpha_list.append(char_dict)
        else:
            char_dict = {
                "name": char,
                "count": count
            }
            junk_list.append(char_dict)
        alpha_list.sort(reverse=True, key=sort_by_count)
        
    for alpha_dict in alpha_list:
        printable_list.append(f"The {alpha_dict["name"]} character was found {alpha_dict["count"]} times")


    #print(junk_list)
    #print(printable_list)
    return printable_list


main()