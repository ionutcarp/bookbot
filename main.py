def get_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def count_words(lotta_text):
    words = lotta_text.split()
    # count_words=0
    # for item in words:
    #     count_words+=1
    # return count_words
    return len(words)


def count_char(text):
    char_dict = {}
    for i in text:
        j = i.lower()
        if j in char_dict:
            char_dict[j] += 1
        else:
            char_dict[j] = 1
    return char_dict


def gen_report(book_path, number_words, char_dict):
    """
    Purpose: aggregate all the word and character data into a nice report that we can print to the console
    """
    print(f"--- Begin report of {book_path} ---")
    print(number_words, " words found in the document")
    print("")
    list_dict = []
    for item in char_dict:
        if item.isalpha():
            entry={
                "name": item,
                "num": char_dict[item]
            }
            list_dict.append(entry)
    list_dict.sort(reverse=True, key=sort_on)
    for item in list_dict:
        print(f"The '{item["name"]}' character was found {item["num"]} times")
    # end for
    print("--- End report ---")
    return


def sort_on(dict):
    return dict["num"]


def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    number_words = count_words(text)
    char_dict=count_char(text)
    # print(text)
    # print("")
    # print(number_words)
    # print("")
    # print(char_dict)
    # print("")
    gen_report(book_path, number_words, char_dict)


main()
