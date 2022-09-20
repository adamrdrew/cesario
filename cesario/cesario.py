
from classifier import CharNGramClassifier, FunctionWordClassifier, KMeansClusteringClassifier
import click
from training import Training

def cross_validate_classifier(classifier_class, title):
    books, classes = Training.get_training_data()
    classifier = classifier_class(books, classes)
    scores = classifier.cross_validate()
    print("-----")
    print(" Cross Validation for: " + title)
    print(" Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def test_train_split_validate_cluster(classifier_class, title):
    books, classes = Training.get_training_data()
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