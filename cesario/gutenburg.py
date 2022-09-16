import urllib.request

import numpy as np

from book import Book
from log import Log

class Gutenburg:
    LOG = "log/gutenberg.log"
    def __init__(self):
        self.log = Log(self.LOG)
    
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








