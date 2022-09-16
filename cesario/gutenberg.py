import urllib.request
import logging
import numpy as np
from enum import Enum
from sklearn.feature_extraction.text import CountVectorizer

class Author(Enum):
    JONATHAN_SWIFT = 0
    WASHINGTON_IRVING = 1


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
        return "\n".join(out)

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




a_modest_proposal = Book("A Modest Proposal", Author.JONATHAN_SWIFT, "http://www.gutenberg.org/files/1080/1080-0.txt")
gullivers_travels = Book("Gulliver's Travels", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/cache/epub/17157/pg17157.txt")

book_list = BookList()
book_list.add_book(a_modest_proposal)
book_list.add_book(gullivers_travels)
book_list.download_books()

FUNCTION_WORDS = ["a", "able", "aboard", "about", "above", "absent",
"according" , "accordingly", "across", "after", "against",
"ahead", "albeit", "all", "along", "alongside", "although",
"am", "amid", "amidst", "among", "amongst", "amount", "an",
"and", "another", "anti", "any", "anybody", "anyone",
"anything", "are", "around", "as", "aside", "astraddle",
"astride", "at", "away", "bar", "barring", "be", "because",
"been", "before", "behind", "being", "below", "beneath",
"beside", "besides", "better", "between", "beyond", "bit",
"both", "but", "by", "can", "certain", "circa", "close",
"concerning", "consequently", "considering", "could",
"couple", "dare", "deal", "despite", "down", "due", "during",
"each", "eight", "eighth", "either", "enough", "every",
"everybody", "everyone", "everything", "except", "excepting",
"excluding", "failing", "few", "fewer", "fifth", "first",
"five", "following", "for", "four", "fourth", "from", "front",
"given", "good", "great", "had", "half", "have", "he",
"heaps", "hence", "her", "hers", "herself", "him", "himself",
"his", "however", "i", "if", "in", "including", "inside",
"instead", "into", "is", "it", "its", "itself", "keeping",
"lack", "less", "like", "little", "loads", "lots", "majority",
"many", "masses", "may", "me", "might", "mine", "minority",
"minus", "more", "most", "much", "must", "my", "myself",
"near", "need", "neither", "nevertheless", "next", "nine",
"ninth", "no", "nobody", "none", "nor", "nothing",
"notwithstanding", "number", "numbers", "of", "off", "on",
"once", "one", "onto", "opposite", "or", "other", "ought",
"our", "ours", "ourselves", "out", "outside", "over", "part",
"past", "pending", "per", "pertaining", "place", "plenty",
"plethora", "plus", "quantities", "quantity", "quarter",
"regarding", "remainder", "respecting", "rest", "round",
"save", "saving", "second", "seven", "seventh", "several",
"shall", "she", "should", "similar", "since", "six", "sixth",
"so", "some", "somebody", "someone", "something", "spite",
"such", "ten", "tenth", "than", "thanks", "that", "the",
"their", "theirs", "them", "themselves", "then", "thence",
"therefore", "these", "they", "third", "this", "those",
"though", "three", "through", "throughout", "thru", "thus",
"till", "time", "to", "tons", "top", "toward", "towards",
"two", "under", "underneath", "unless", "unlike", "until",
"unto", "up", "upon", "us", "used", "various", "versus",
"via", "view", "wanting", "was", "we", "were", "what",
"whatever", "when", "whenever", "where", "whereas",
"wherever", "whether", "which", "whichever", "while",
"whilst", "who", "whoever", "whole", "whom", "whomever",
"whose", "will", "with", "within", "without", "would", "yet",
"you", "your", "yours", "yourself", "yourselves"]

extractor = CountVectorizer(vocabulary=FUNCTION_WORDS)