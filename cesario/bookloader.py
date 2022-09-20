from nis import cat
import os
import fnmatch
from book import Book
from booklist import BookList
import codecs

class BookLoader:
    FIRST_LINE = "the project gutenberg ebook of "
    AUTHOR_DELIM = ", by "

    def __init__(self, directory:str):
        self.directory = directory
        self.booklist = BookList()

    def load(self):
        for dirpath, dirnames, filename in os.walk(self.directory):
            if dirpath == "old":
                continue
            for filename in filename:
                txtfile_full_path = os.path.join(dirpath, filename)
                f = codecs.open(txtfile_full_path, 'r', encoding='latin-1')
                self.process(f.read())
                f.close()



    def process(self, text:str):
        try:
            if self.detect_valid_first_line(text) == False:
                return
            title = self.get_book_title(text)
            if len(title) == 0:
                return
            author = self.get_author(text)
            if len(title) == 0:
                return
        except Exception as e:
            print(e)
            return
        book = self.make_book(title, author, text)
        print("Loaded book: " + book.title + " by " + book.author + "\n")
        self.booklist.add_book(book)

    def detect_valid_first_line(self, text:str) -> bool:
        lines = text.splitlines()
        first_line = lines[0].lower()
        if first_line.startswith(self.FIRST_LINE) == False:
            return False
        return True
    
    def get_book_title(self, text:str) -> str:
        idx1 = text.lower().index(self.FIRST_LINE)
        idx2 = text.lower().index(self.AUTHOR_DELIM)
        if idx1 > 100 or idx2 > 100:
            raise Exception("Error getting title")
        return text[idx1+len(self.FIRST_LINE):idx2].lower()

    def get_author(self, text:str) -> str:
        idx1 = text.lower().index(self.AUTHOR_DELIM)
        idx2 = text.lower().index("\n")
        if idx1 > 100 or idx2 > 100:
            raise Exception("Error getting title")
        return text[idx1+len(self.AUTHOR_DELIM):idx2].lower()

    def make_book(self, title:str, author:str, text:str) -> Book:
        no_url = ""
        book = Book(title, author, no_url)
        book.raw_text = text
        return book
