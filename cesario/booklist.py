from gutenburg import Gutenburg
from book import Book

class BookList:
    book_list = []
    gutenburg = Gutenburg()

    def add_book(self, book: Book):
        self.book_list.append(book)

    def download_books(self):
        for book in self.book_list:
            book = self.gutenburg.download_book(book)