def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    print(f"There are {word_count} words in this book\n")
    letter_counts = get_letter_counts(text)
    print_report(letter_counts)

def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def get_word_count(text):
    return len(text.split())

def get_letter_counts(text):
    letter_dict = {}
    for letter in text.lower():
        if(letter in letter_dict):
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def print_report(letter_dict):
    list_of_dicts = []
    for letter in letter_dict:
        if(letter.isalpha()):
            list_of_dicts.append({"letter": letter, "num" :letter_dict[letter]})

    list_of_dicts.sort(reverse=True, key=sort_on)

    for dict in list_of_dicts:
        print(f"The '{dict["letter"]}' character was found {dict["num"]} times")



main()