from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from functionwords import FunctionWords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
from author import Authors
from sklearn.cluster import KMeans

COLORS = {
    0: "#ff0000",
    1: "#00ff00",
    2: "#0000ff",
    3: "#ffff00",
    4: "#ff8000",
    5: "#8000ff",
    6: "#ff0080",
    7: "#00ffff",
    8: "#804000",
    9: "#000000",
    10: "#ffffff",
    11: "#808080",
    12: "#c0c0c0",
    13: "#404040",
    14: "#ff8080",
    15: "#80ff80",
}

class Classifier:
    pipeline = None

    def __init__(self, documents:list[str], classes:list[int]):
        self.documents = documents
        self.classes = classes
        self.init_pipeline()

    def init_pipeline(self):
        raise NotImplementedError

    def train(self):
        self.pipeline.fit(self.documents, self.classes)

    def predict(self, doc:str):
        return self.pipeline.predict([doc])
    
    def predict_with_probability(self, doc:str):
        return self.pipeline.predict_proba([doc])

    #Cross validation. Cuts the data set up into sections and trains and tests the sections against eachother
    def cross_validate(self):
        return cross_val_score(self.pipeline, self.documents, self.classes, scoring='f1_weighted', cv=16)

    #Splits the data into a training set and a test set and trains the classifier on the training set and tests it on the test set
    def test_train_split(self):
        return train_test_split(self.documents, self.classes, random_state=14)

    #Trains the classifier on a split 
    def train_and_validate(self):
        train_docs, self.validate_docs, train_classes, self.validate_classes = self.test_train_split()
        self.pipeline.fit(train_docs, train_classes)
        return self.validate()

    def validate(self):
        self.predicted_classes = self.pipeline.predict(self.validate_docs)
        count = len(self.predicted_classes)
        correct_count = 0
        for i in range(count):
            correct = self.predicted_classes[i] == self.validate_classes[i]
            if correct:
                correct_count += 1
        return (correct_count / count) * 100

    def graph_validate(self):
        colors = []
        for prediction in self.predicted_classes:
            colors.append(COLORS[prediction])
        plt.scatter(self.validate_classes, self.predicted_classes, c=colors)
        plt.show()


class FunctionWordClassifier(Classifier):
    def init_pipeline(self):
        parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'probability':[True]}
        svr = SVC()
        grid = GridSearchCV(svr, parameters)
        function_words = FunctionWords()
        self.pipeline  = Pipeline([('feature_extraction', function_words.extractor), ('clf', grid)])


class CharNGramClassifier(Classifier):
    def init_pipeline(self):
        parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'probability':[True]}
        svr = SVC()
        grid = GridSearchCV(svr, parameters)
        ngram_extractor = CountVectorizer(analyzer='char', ngram_range=(3,3))
        self.pipeline  = Pipeline([('feature_extraction', ngram_extractor), ('clf', grid)])

class KMeansClusteringClassifier(Classifier):
    def init_pipeline(self):
        function_words = FunctionWords()
        self.pipeline = Pipeline([('feature_extraction', function_words.extractor), ('clusterer', KMeans(n_clusters=2))])