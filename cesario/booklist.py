from gutenburg import Gutenburg
from book import Book
import numpy as np

class BookList:
    book_list = []
    gutenburg = Gutenburg()
    max_book_size = 65535

    def add_book(self, book: Book):
        self.book_list.append(book)

    def download_books(self):
        for book in self.book_list:
            book = self.gutenburg.download_book(book)

    def get_books_and_classes(self):
        books = []
        classes = []
        for book in self.book_list:
            if book.size() < self.max_book_size:
                books.append(book.content_lines())
                classes.append(book.author.value)
            else:
                while book.size() > self.max_book_size:
                    books.append(book.split(self.max_book_size).content_lines())
                    classes.append(book.author.value)

        return books, np.array(classes, dtype='int')