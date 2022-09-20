from gutenburg import Gutenburg
from book import Book
import numpy as np

class BookList:
    MAX_BOOK_SIZE = 65535
    book_list = []

    def add_book(self, book: Book):
        self.book_list.append(book)

    def load(self):
        for book in self.book_list:
            book.load()

    def get_books_and_classes(self):
        classes = []
        books = []
        classes = []
        for book in self.book_list:
            if book.size() < self.MAX_BOOK_SIZE:
                books.append(book.content_lines())
                classes.append(int(book.is_shakespeare))
            else:
                while book.size() > self.MAX_BOOK_SIZE:
                    books.append(book.split(self.MAX_BOOK_SIZE).content_lines())
                    classes.append(int(book.is_shakespeare))
        return books, np.array(classes, dtype='int')