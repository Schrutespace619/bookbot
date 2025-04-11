def get_book_text(books):
    with open(books) as f:
        book_content = f.read()
    return book_content

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)

main()

