def get_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main ():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)
main()