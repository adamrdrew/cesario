from re import M
from book import Book
from booklist import BookList
from author import Author
from classifier import Classifier
import numpy as np

def main():
    
    book_list = BookList()
    
    book_list.add_book(Book("A Modest Proposal", Author.JONATHAN_SWIFT, "http://www.gutenberg.org/files/1080/1080-0.txt"))
    book_list.add_book(Book("Gulliver's Travels", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/cache/epub/17157/pg17157.txt"))
    book_list.add_book(Book("A Tale of a Tub", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/files/4737/4737-0.txt"))
    book_list.add_book(Book("Three Prayers and Sermons", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/files/4738/4738-0.txt"))
    book_list.add_book(Book("The Bickerstaff-Partridge Papers", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/cache/epub/1090/pg1090.txt"))
    book_list.add_book(Book("The Battle of the Books", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/cache/epub/623/pg623.txt"))
    book_list.add_book(Book("The Journal to Stella", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/files/4208/4208-0.txt"))
    book_list.add_book(Book("Prose Works", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/cache/epub/13040/pg13040.txt"))
    book_list.add_book(Book("Polite Conversations", Author.JONATHAN_SWIFT, "https://www.gutenberg.org/files/60186/60186-0.txt"))

    book_list.add_book(Book("Mr. Pickwick's Christmas", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/61193/61193-0.txt"))
    book_list.add_book(Book("Master Humphrey's Clock", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/588/588-0.txt"))
    book_list.add_book(Book("To Ne Read at Dusk", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/924/924-0.txt"))
    book_list.add_book(Book("The Chimes", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/653/653-0.txt"))
    book_list.add_book(Book("Doctor Marigold", Author.CHARLES_DICKENS, "https://www.gutenberg.org/cache/epub/1415/pg1415.txt"))
    book_list.add_book(Book("David Copperfield", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/766/766-0.txt"))
    book_list.add_book(Book("Three Ghost Stories", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/883/883-0.txt"))
    book_list.add_book(Book("Bleakhouse", Author.CHARLES_DICKENS, "https://www.gutenberg.org/cache/epub/1023/pg1023.txt"))
    book_list.add_book(Book("A Christmas Carol", Author.CHARLES_DICKENS, "https://www.gutenberg.org/cache/epub/19337/pg19337.txt"))
    book_list.add_book(Book("American Notes", Author.CHARLES_DICKENS, "https://www.gutenberg.org/files/675/675-0.txt"))

    book_list.add_book(Book("The Legend of Sleepy Hollow", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/cache/epub/41/pg41.txt"))
    book_list.add_book(Book("Rip Van Winkle", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/60976/60976-0.txt"))
    book_list.add_book(Book("The Sketch Book of Geoffrey Crayon", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/2048/2048-0.txt"))
    book_list.add_book(Book("The Alhambra", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/49947/49947-0.txt"))
    book_list.add_book(Book("An Old Fashioned Christmas Day", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/52361/52361-0.txt"))
    book_list.add_book(Book("Bracebridge Hall, or The Humorists", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/cache/epub/13515/pg13515.txt"))
    book_list.add_book(Book("Chronicle of the Conquest of Granada", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/3293/3293-0.txt"))
    book_list.add_book(Book("Astoria", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/1371/1371-0.txt"))
    book_list.add_book(Book("Tales of a Traveller", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/files/13514/13514-0.txt"))
    book_list.add_book(Book("The Life and Voyages of Christopher Columbus", Author.WASHINGTON_IRVING, "https://www.gutenberg.org/cache/epub/8519/pg8519.txt"))

    book_list.add_book(Book("The Adventures of Tom Sawyer", Author.MARK_TWAIN, "https://www.gutenberg.org/files/74/74-0.txt"))
    book_list.add_book(Book("The Adventures of Huckleberry Finn", Author.MARK_TWAIN, "https://www.gutenberg.org/files/76/76-0.txt"))
    book_list.add_book(Book("The Prince and the Pauper", Author.MARK_TWAIN, "https://www.gutenberg.org/files/1837/1837-0.txt"))
    book_list.add_book(Book("A Connecticut Yankee in King Arthur's Court", Author.MARK_TWAIN, "https://www.gutenberg.org/cache/epub/86/pg86.txt"))
    book_list.add_book(Book("The Mysterious Stranger", Author.MARK_TWAIN, "https://www.gutenberg.org/files/3186/3186-0.txt"))
    book_list.add_book(Book("The Innocents Abroad", Author.MARK_TWAIN, "https://www.gutenberg.org/files/3176/3176-0.txt"))
    book_list.add_book(Book("Life On The Mississippi", Author.MARK_TWAIN, "https://www.gutenberg.org/files/245/245-0.txt"))
    book_list.add_book(Book("Roughing It", Author.MARK_TWAIN, "https://www.gutenberg.org/cache/epub/3177/pg3177.txt"))
    book_list.add_book(Book("The Mysterious Stranger and Other Stories", Author.MARK_TWAIN, "https://www.gutenberg.org/files/3186/3186-0.txt"))
    book_list.add_book(Book("The Tragedy of Pudd'nhead Wilson", Author.MARK_TWAIN, "https://www.gutenberg.org/files/102/102-0.txt"))

    book_list.add_book(Book("The Picture of Dorian Gray", Author.OSCAR_WILDE, "https://www.gutenberg.org/cache/epub/174/pg174.txt"))
    book_list.add_book(Book("The Importance of Being Earnest", Author.OSCAR_WILDE, "https://www.gutenberg.org/files/844/844-0.txt"))
    book_list.add_book(Book("The Happy Prince and Other Tales", Author.OSCAR_WILDE, "https://www.gutenberg.org/cache/epub/902/pg902.txt"))
    book_list.add_book(Book("The Canterville Ghost", Author.OSCAR_WILDE, "https://www.gutenberg.org/cache/epub/14522/pg14522.txt"))
    book_list.add_book(Book("An Ideal Husband", Author.OSCAR_WILDE, "https://www.gutenberg.org/files/885/885-0.txt"))
    book_list.add_book(Book("De Profundis", Author.OSCAR_WILDE, "https://www.gutenberg.org/cache/epub/921/pg921.txt"))
    book_list.add_book(Book("Salome", Author.OSCAR_WILDE, "https://www.gutenberg.org/cache/epub/42704/pg42704.txt"))
    book_list.add_book(Book("Lady Windermere’s Fan", Author.OSCAR_WILDE, "https://www.gutenberg.org/files/790/790-0.txt"))
    book_list.add_book(Book("A Woman of No Importance", Author.OSCAR_WILDE, "https://www.gutenberg.org/files/854/854-0.txt"))
    book_list.add_book(Book("A House of Pomegranites", Author.OSCAR_WILDE, "https://www.gutenberg.org/files/873/873-0.txt"))

    book_list.add_book(Book("The Adventures of Sherlock Holmes", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/files/1661/1661-0.txt"))
    book_list.add_book(Book("A Study in Scarlet", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/cache/epub/244/pg244.txt"))
    book_list.add_book(Book("The Lost World", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/cache/epub/139/pg139.txt"))
    book_list.add_book(Book("The Hound of the Baskervilles", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/files/2852/2852-0.txt"))
    book_list.add_book(Book("The Memoirs of Sherlock Holmes", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/cache/epub/834/pg834.txt"))
    book_list.add_book(Book("The Return of Sherlock Holmes", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/cache/epub/108/pg108.txt"))
    book_list.add_book(Book("The Valley of Fear", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/files/3289/3289-0.txt"))
    book_list.add_book(Book("Tales of Terror and Mystery", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/cache/epub/537/pg537.txt"))
    book_list.add_book(Book("The White Company", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/files/903/903-0.txt"))
    book_list.add_book(Book("The Great Boer War", Author.ARTHUR_CONAN_DOYLE, "https://www.gutenberg.org/files/3069/3069-0.txt"))

    book_list.add_book(Book("The Alchemist", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/4081/pg4081.txt"))
    book_list.add_book(Book("Volpone", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/4039/pg4039.txt"))
    book_list.add_book(Book("Every Man in his Humour", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/5333/pg5333.txt"))
    book_list.add_book(Book("Bartholomew Fair", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/49461/pg49461.txt"))
    book_list.add_book(Book("Epiceone", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/4011/pg4011.txt"))
    book_list.add_book(Book("Discoveries made upon men", Author.BEN_JONSON, "https://www.gutenberg.org/files/5134/5134-0.txt"))
    book_list.add_book(Book("Sejanus", Author.BEN_JONSON, "https://www.gutenberg.org/files/5232/5232-0.txt"))
    book_list.add_book(Book("The Devil is an Ass", Author.BEN_JONSON, "https://www.gutenberg.org/files/50150/50150-0.txt"))
    book_list.add_book(Book("Poetaster", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/5166/pg5166.txt"))
    book_list.add_book(Book("Cynthia's Revels", Author.BEN_JONSON, "https://www.gutenberg.org/cache/epub/3771/pg3771.txt"))

    book_list.add_book(Book("Paradise Lost", Author.JOHN_MILTON, "https://www.gutenberg.org/cache/epub/26/pg26.txt"))
    book_list.add_book(Book("Areopagitica", Author.JOHN_MILTON, "https://www.gutenberg.org/cache/epub/608/pg608.txt"))
    book_list.add_book(Book("Poetical Works", Author.JOHN_MILTON, "https://www.gutenberg.org/cache/epub/1745/pg1745.txt"))
    book_list.add_book(Book("Comus", Author.JOHN_MILTON, "https://www.gutenberg.org/files/19819/19819-0.txt"))
    book_list.add_book(Book("Paradise Regained", Author.JOHN_MILTON, "https://www.gutenberg.org/cache/epub/58/pg58.txt"))
    book_list.add_book(Book("Minor Poems", Author.JOHN_MILTON, "https://www.gutenberg.org/cache/epub/31706/pg31706.txt"))

    book_list.add_book(Book("Romeo and Juliet", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"))
    book_list.add_book(Book("Hamlet", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/1524/pg1524.txt"))
    book_list.add_book(Book("Midsummer's Night", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/files/1514/1514-0.txt"))
    book_list.add_book(Book("Merchant of Venice", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/1515/pg1515.txt"))
    book_list.add_book(Book("As you like it", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/1121/pg1121.txt"))
    book_list.add_book(Book("Comedy of Errors", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/files/23046/23046-0.txt"))
    book_list.add_book(Book("Taming of the Shrew", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/1508/pg1508.txt"))
    book_list.add_book(Book("Measure for Measure", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/23045/pg23045.txt"))
    book_list.add_book(Book("Tempest", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/files/23042/23042-0.txt"))
    book_list.add_book(Book("Macbeth", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/2264/pg2264.txt"))
    book_list.add_book(Book("Othello", Author.WILLIAM_SHAKESPEARE, "https://www.gutenberg.org/cache/epub/1531/pg1531.txt"))

    book_list.add_book(Book("Poems vol 1", Author.JOHN_DONNE, "https://www.gutenberg.org/files/48688/48688-0.txt"))
    book_list.add_book(Book("Poems vol 2", Author.JOHN_DONNE, "https://www.gutenberg.org/files/48772/48772-0.txt"))
    book_list.add_book(Book("Paradoxes and Problems", Author.JOHN_DONNE, "https://www.gutenberg.org/files/61783/61783-0.txt"))
    book_list.add_book(Book("Letters", Author.JOHN_DONNE, "https://www.gutenberg.org/cache/epub/37387/pg37387.txt"))



    book_list.download_books()
    documents, classes = book_list.get_books_and_classes()

    classifier = Classifier()
    scores = classifier.get_scores(documents, classes)
    mean_score = np.mean(scores)
    print("Mean score: " + str(mean_score))


if __name__ == '__main__':
    main()