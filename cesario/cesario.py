from book import Book
from booklist import BookList
from author import Author

def main():
    a_modest_proposal = Book("A Modest Proposal", Author.JONATHAN_SWIFT, "http://www.gutenberg.org/files/1080/1080-0.txt")
    gullivers_travels = Book("Gulliver's Travels", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/cache/epub/17157/pg17157.txt")

    book_list = BookList()
    book_list.add_book(a_modest_proposal)
    book_list.add_book(gullivers_travels)
    book_list.download_books()


if __name__ == '__main__':
    main()