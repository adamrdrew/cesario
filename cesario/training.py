from book import Book
from booklist import BookList

TRAINING_DATA = {
    #These are the documents that train for shakespeare's style
    "shakespeare": [
        "training/shakespeare/pg1112.txt",
        "training/shakespeare/pg1112.txt",
        "training/shakespeare/pg1515.txt",
        "training/shakespeare/pg1531.txt",
        "training/shakespeare/pg1532.txt",
        "training/shakespeare/pg1519.txt",
        "training/shakespeare/pg1526.txt",
        "training/shakespeare/pg1522.txt",
        "training/shakespeare/pg23045.txt",
        "training/shakespeare/pg1508.txt",
        "training/shakespeare/23046-0.txt",
        "training/shakespeare/pg1523.txt",
        "training/shakespeare/pg1103.txt",
        "training/shakespeare/pg1534.txt",
        "training/shakespeare/pg1521.txt",
        "training/shakespeare/pg1529.txt",
        "training/shakespeare/pg1539.txt",
        "training/shakespeare/pg1110.txt",
        "training/shakespeare/pg1106.txt",
        "training/shakespeare/1045-0.txt",
        "training/shakespeare/pg1795.txt",
        "training/shakespeare/pg1041.txt",
    ],
    #This is a large collection of documents that train for non-shakespeare style
    "other": [
        #Jane Austen
        "training/other/1342-0.txt",
        "training/other/pg105.txt",
        "training/other/pg158.txt",
        "training/other/161-0.txt",
        "training/other/pg121.txt",
        "training/other/pg141.txt",
        "training/other/pg42078.txt",
        #John Locke
        "training/other/pg7370.txt",
        "training/other/pg10615.txt",
        "training/other/pg10616.txt",
        #William Wordsworth
        "training/other/9622-0.txt",
        "training/other/pg10219.txt",
        "training/other/pg59813.txt",
        "training/other/56361-0.txt",
        "training/other/pg12145.txt",
        #William Blake
        "training/other/pg1934.txt",
        "training/other/pg45315.txt",
        "training/other/pg574.txt",
        #Jonathan Swift
        "training/other/1080-0.txt",
        "training/other/829-0.txt",
        "training/other/pg623.txt",
        "training/other/4737-0.txt",
        "training/other/4208-0.txt",
        "training/other/4738-0.txt",
        #Mary Shelly Wollstonecraft
        "training/other/84-0.txt",
        "training/other/pg18247.txt",
        "training/other/pg15238.txt",
        "training/other/pg6447.txt",
        #Samuel Johnson
        "training/other/652-0.txt",
        "training/other/pg2064.txt",
        "training/other/57837-0.txt",
        "training/other/5098-0.txt",
        #John Milton
        "training/other/pg26.txt",
        "training/other/pg608.txt",
        "training/other/pg1745.txt",
        "training/other/pg58.txt",
        #Samuel Coleridge
        "training/other/9622-0.txt",
        "training/other/pg151.txt",
        "training/other/29090-0.txt",
        "training/other/44795-0.txt",
        "training/other/pg6787.txt",
        #Daniel Defoe
        "training/other/521-0.txt",
        "training/other/376-0.txt",
        "training/other/pg40580.txt",
        "training/other/370-0.txt",
        "training/other/pg30344.txt",
        "training/other/pg31053.txt",
        #Alexander Pope
        "training/other/pg9800.txt",
        "training/other/pg2428.txt",
        "training/other/pg7409.txt",
        "training/other/pg9601.txt",
        "training/other/pg9413.txt",
        #Walter Scott
        "training/other/82-0.txt",
        "training/other/pg3011.txt",
        #Joseph Addison
        "training/other/pg31592.txt",
        #Samuel Foote
        "training/other/pg49602.txt",
        #John Vanbrugh
        "training/other/51113-0.txt",
        #William Congreve
        "training/other/1292-0.txt",
        "training/other/1244-0.txt",
        "training/other/1192-0.txt",
        "training/other/pg1191.txt",
        "training/other/2363-0.txt",
        #Thomas d'Urfey
        "training/other/pg33404.txt",
        "training/other/pg16335.txt",
        #Susanna Centivre
        "training/other/pg16740.txt",
        "training/other/36234-0.txt",
        "training/other/pg38931.txt",
    ],
}

SUSPECTS= []

class Training:
    def get_training_data(split_docs:bool):
        book_list = BookList()  
        for file in TRAINING_DATA["shakespeare"]:
            book_list.add_book(Book({"file": file, "is_shakespeare": True}))
        for file in TRAINING_DATA["other"]:
            book_list.add_book(Book({"file": file, "is_shakespeare": False}))
        book_list.load()
        books, classes = book_list.get_books_and_classes(split_docs)
        return books, classes
