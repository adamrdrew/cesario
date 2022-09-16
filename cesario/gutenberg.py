import urllib.request
import logging

class Book:
    title = ""
    author = ""
    url = ""
    raw_text = ""

    CONTENT_START = "*** START OF THE PROJECT GUTENBERG EBOOK"
    CONTENT_END = "*** END OF THE PROJECT GUTENBERG EBOOK"

    def __init__(self, title:str, author: str, url:str):
        self.title = title
        self.author = author
        self.url = url

    #Gets the lines of the text exactly as they are in the file
    def raw_lines(self) -> list[str]:
        return self.raw_text.split("\n")
    
    #Gets the lines of the text without the header and footer
    def content_lines(self) -> list[str]:
        out = []
        found_content = False
        for line in self.raw_lines():
            if self.CONTENT_START in line:
                found_content = True
                continue
            if self.CONTENT_END in line:
                break
            if found_content:
                out.append(line)
        return out 

class Gutenburg:
    LOG = "log/gutenberg.log"
    def __init__(self):
        self.log = Log(LOG)
    
    def download_book(self, book: Book) -> Book:
        book.raw_text = self.download(book.url)
        return book

    def download(self, url) -> str:
        try:
            with urllib.request.urlopen(url) as f:
                self.log.info("Donwloaded book " + url)
                return f.read().decode("utf-8")
        except urllib.error.URLError as e:
            self.log.error("Failed to download book " + url + " with error " + e.reason)

class Log:
    def __init__(self, file_name):
        logging.basicConfig(filename=file_name, level=logging.DEBUG)

    def warning(self, message):
        logging.warning(message)
    
    def error(self, message):
        logging.error(message)
    
    def info(self, message):
        logging.info(message)

class BookList:
    book_list = []
    gutenburg = Gutenburg()

    def add_book(self, book: Book):
        self.book_list.append(book)

    def download_books(self):
        for book in self.book_list:
            logging.info("Downloading book: %s", book.title)
            book = self.gutenburg.download_book(book)



a_modest_proposal = Book("A Modest Proposal", "Jonathan Swift", "http://www.gutenberg.org/files/1080/1080-0.txt")
gullivers_travels = Book("Gulliver's Travels", "Jonathan Swift", "https://www.gutenberg.org/cache/epub/17157/pg17157.txt")

book_list = BookList()
book_list.add_book(a_modest_proposal)
book_list.add_book(gullivers_travels)
book_list.download_books()

