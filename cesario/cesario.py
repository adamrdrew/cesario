from book import Book
from booklist import BookList
from classifier import CharNGramClassifier, FunctionWordClassifier, KMeansClusteringClassifier
import click

TRAINING_DATA = {
    #These are the documents that train for shakespeare's style
    "shakespeare": [
        "https://www.gutenberg.org/cache/epub/1513/pg1513.txt",
        "https://www.gutenberg.org/cache/epub/1524/pg1524.txt",
        "https://www.gutenberg.org/files/23042/23042-0.txt",
        "https://www.gutenberg.org/files/1533/1533-0.txt",
        "https://www.gutenberg.org/files/1514/1514-0.txt",
        "https://www.gutenberg.org/cache/epub/1112/pg1112.txt",
        "https://www.gutenberg.org/cache/epub/1112/pg1112.txt",
        "https://www.gutenberg.org/cache/epub/1515/pg1515.txt",
        "https://www.gutenberg.org/cache/epub/1531/pg1531.txt",
        "https://www.gutenberg.org/cache/epub/1532/pg1532.txt",
        "https://www.gutenberg.org/cache/epub/1519/pg1519.txt",
        "https://www.gutenberg.org/cache/epub/1526/pg1526.txt",
        "https://www.gutenberg.org/cache/epub/1522/pg1522.txt",
        "https://www.gutenberg.org/cache/epub/23045/pg23045.txt",
        "https://www.gutenberg.org/cache/epub/1508/pg1508.txt",
        "https://www.gutenberg.org/files/23046/23046-0.txt",
        "https://www.gutenberg.org/cache/epub/1523/pg1523.txt",
        "https://www.gutenberg.org/cache/epub/1103/pg1103.txt",
        "https://www.gutenberg.org/cache/epub/1534/pg1534.txt",
        "https://www.gutenberg.org/cache/epub/1521/pg1521.txt",
        "https://www.gutenberg.org/cache/epub/1529/pg1529.txt",
        "https://www.gutenberg.org/cache/epub/1539/pg1539.txt",
        "https://www.gutenberg.org/cache/epub/1110/pg1110.txt",
        "https://www.gutenberg.org/cache/epub/1106/pg1106.txt",
        "https://www.gutenberg.org/files/1045/1045-0.txt",
        "https://www.gutenberg.org/cache/epub/1795/pg1795.txt",
    ],
    #This is a large collection of documents that train for non-shakespeare style
    "other": [
        #Jane Austen
        "https://www.gutenberg.org/files/1342/1342-0.txt",
        "https://www.gutenberg.org/cache/epub/105/pg105.txt",
        "https://www.gutenberg.org/cache/epub/158/pg158.txt",
        "https://www.gutenberg.org/files/161/161-0.txt",
        "https://www.gutenberg.org/cache/epub/121/pg121.txt",
        "https://www.gutenberg.org/cache/epub/141/pg141.txt",
        "https://www.gutenberg.org/cache/epub/42078/pg42078.txt",
        #John Locke
        "https://www.gutenberg.org/cache/epub/7370/pg7370.txt",
        "https://www.gutenberg.org/cache/epub/10615/pg10615.txt",
        "https://www.gutenberg.org/cache/epub/10616/pg10616.txt",
        #William Wordsworth
        "https://www.gutenberg.org/files/9622/9622-0.txt",
        "https://www.gutenberg.org/cache/epub/10219/pg10219.txt",
        "https://www.gutenberg.org/cache/epub/59813/pg59813.txt",
        "https://www.gutenberg.org/files/56361/56361-0.txt",
        "https://www.gutenberg.org/cache/epub/12145/pg12145.txt",
        #William Blake
        "https://www.gutenberg.org/cache/epub/1934/pg1934.txt",
        "https://www.gutenberg.org/cache/epub/45315/pg45315.txt",
        "https://www.gutenberg.org/cache/epub/574/pg574.txt",
        #Jonathan Swift
        "https://www.gutenberg.org/files/1080/1080-0.txt",
        "https://www.gutenberg.org/files/829/829-0.txt",
        "https://www.gutenberg.org/cache/epub/623/pg623.txt",
        "https://www.gutenberg.org/files/4737/4737-0.txt",
        "https://www.gutenberg.org/files/4208/4208-0.txt",
        "https://www.gutenberg.org/files/4738/4738-0.txt",
        #Mary Shelly Wollstonecraft
        "https://www.gutenberg.org/files/84/84-0.txt",
        "https://www.gutenberg.org/cache/epub/18247/pg18247.txt",
        "https://www.gutenberg.org/cache/epub/15238/pg15238.txt",
        "https://www.gutenberg.org/cache/epub/6447/pg6447.txt",
        #Samuel Johnson
        "https://www.gutenberg.org/files/652/652-0.txt",
        "https://www.gutenberg.org/cache/epub/2064/pg2064.txt",
        "https://www.gutenberg.org/files/57837/57837-0.txt",
        "https://www.gutenberg.org/files/5098/5098-0.txt",
        #John Milton
        "https://www.gutenberg.org/cache/epub/26/pg26.txt",
        "https://www.gutenberg.org/cache/epub/608/pg608.txt",
        "https://www.gutenberg.org/cache/epub/1745/pg1745.txt",
        "https://www.gutenberg.org/cache/epub/58/pg58.txt",
        #Samuel Coleridge
        "https://www.gutenberg.org/files/9622/9622-0.txt",
        "https://www.gutenberg.org/cache/epub/151/pg151.txt",
        "https://www.gutenberg.org/files/29090/29090-0.txt",
        "https://www.gutenberg.org/files/44795/44795-0.txt",
        "https://www.gutenberg.org/cache/epub/6787/pg6787.txt",
        #Daniel Defoe
        "https://www.gutenberg.org/files/521/521-0.txt",
        "https://www.gutenberg.org/files/376/376-0.txt",
        "https://www.gutenberg.org/cache/epub/40580/pg40580.txt",
        "https://www.gutenberg.org/files/370/370-0.txt",
        "https://www.gutenberg.org/cache/epub/30344/pg30344.txt",
        "https://www.gutenberg.org/cache/epub/31053/pg31053.txt",
        #Alexander Pope
        "https://www.gutenberg.org/cache/epub/9800/pg9800.txt",
        "https://www.gutenberg.org/cache/epub/2428/pg2428.txt",
        "https://www.gutenberg.org/cache/epub/7409/pg7409.txt",
        "https://www.gutenberg.org/cache/epub/9601/pg9601.txt",
        "https://www.gutenberg.org/cache/epub/9413/pg9413.txt",
        #Walter Scott
        "https://www.gutenberg.org/files/82/82-0.txt",
        "https://www.gutenberg.org/cache/epub/3011/pg3011.txt",
        #Joseph Addison
        "https://www.gutenberg.org/cache/epub/31592/pg31592.txt",
        #Samuel Foote
        "https://www.gutenberg.org/cache/epub/49602/pg49602.txt",
        #John Vanbrugh
        "https://www.gutenberg.org/files/51113/51113-0.txt",
        #William Congreve
        "https://www.gutenberg.org/files/1292/1292-0.txt",
        "https://www.gutenberg.org/files/1244/1244-0.txt",
        "https://www.gutenberg.org/files/1192/1192-0.txt",
        "https://www.gutenberg.org/cache/epub/1191/pg1191.txt",
        "https://www.gutenberg.org/files/2363/2363-0.txt",
        #Thomas d'Urfey
        "https://www.gutenberg.org/cache/epub/33404/pg33404.txt",
        "https://www.gutenberg.org/cache/epub/16335/pg16335.txt",
        #Susanna Centivre
        "https://www.gutenberg.org/cache/epub/16740/pg16740.txt",
        "https://www.gutenberg.org/files/36234/36234-0.txt",
        "https://www.gutenberg.org/cache/epub/38931/pg38931.txt",
    ],
}

SUSPECTS= []

def get_training_data():
    book_list = BookList()  
    for url in TRAINING_DATA["shakespeare"]:
        book_list.add_book(Book({"url": url, "is_shakespeare": True}))
    for url in TRAINING_DATA["other"]:
        book_list.add_book(Book({"url": url, "is_shakespeare": False}))
    book_list.load()
    books, classes = book_list.get_books_and_classes()
    return books, classes

def cross_validate_classifier(classifier_class, title):
    books, classes = get_training_data()
    classifier = classifier_class(books, classes)
    scores = classifier.cross_validate()
    print("-----")
    print(" Cross Validation for: " + title)
    print(" Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def test_train_split_validate_cluster(classifier_class, title):
    books, classes = get_training_data()
    classifier = classifier_class(books, classes)
    accuracy = classifier.train_and_validate()
    print("-----")
    print(" Test Train Split Validation for: " + title)
    print(" Accuracy: %0.2f" % (accuracy))

@click.group()
def cli():
    pass

@cli.command("validate")
def validate():
    print("Validating classifiers. This will take a while...")
    cross_validate_classifier(FunctionWordClassifier, "Function Word Classifier")
    cross_validate_classifier(CharNGramClassifier, "Char NGram Classifier")
    cross_validate_classifier(KMeansClusteringClassifier, "KMeans Clustering Classifier")
    test_train_split_validate_cluster(FunctionWordClassifier, "Function Word Classifier")
    test_train_split_validate_cluster(CharNGramClassifier, "Char NGram Classifier")
    test_train_split_validate_cluster(KMeansClusteringClassifier, "KMeans Clustering Classifier")

if __name__ == '__main__':
    cli()