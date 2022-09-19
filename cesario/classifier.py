from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from functionwords import FunctionWords

class Classifier:
    def __init__(self):
        self.parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
        self.svr = SVC()
        self.grid = GridSearchCV(self.svr, self.parameters)
        self.function_words = FunctionWords()
        self.pipeline  = Pipeline([('feature_extraction', self.function_words.extractor), ('clf', self.grid)])
        

    def get_scores(self, documents, classes):
        return cross_val_score(self.pipeline, documents, classes, scoring='f1_weighted', cv=16)