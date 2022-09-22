from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from functionwords import FunctionWords, FunctionWordsTFIDF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

#This is the superclass for all the classifiers
class Classifier:
    pipeline = None
    name = "Classifier"

    def __init__(self, documents:list[str], classes:list[int]):
        self.documents = documents
        self.classes = classes
        self.init_pipeline()

    #def predict_probability_string(self, doc:str):
    #    class_prediction = self.predict(doc)[0]
    #    result = self.predict_with_probability(doc)
    #    prediction_probablity = result[0][class_prediction]
    #    print("     * " + self.name + ": is by Shakespeare: "+ str(bool(class_prediction == 1)) +", with probability: %0.2f" % prediction_probablity)
    #    return result[0][1]

    def init_pipeline(self):
        raise NotImplementedError

    def train(self):
        self.pipeline.fit(self.documents, self.classes)

    def predict(self, doc:str) -> list[int]:
        return self.pipeline.predict([doc])
    
    def predict_with_probability(self, doc:str) -> list[float]:
        return self.pipeline.predict_proba([doc])

    #Cross validation. Cuts the data set up into sections and trains and tests the sections against eachother
    def cross_validate(self) -> list[float]:
        return cross_val_score(self.pipeline, self.documents, self.classes, cv=10, scoring='accuracy')

####################################################################################
#Feature Words Classifiers
class Classifier_SVM_FeatureWordsExtractor_CountVectorizer(Classifier):
    name = "SVM with Function Words and Count Vectorizer"
    def init_pipeline(self):
        parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'probability':[True], 'class_weight':['balanced', None]}
        svr = SVC()
        grid = GridSearchCV(svr, parameters)
        function_words = FunctionWords()
        self.pipeline  = Pipeline([('feature_extraction', function_words.extractor), ('clf', grid)])

class Classifier_SVM_FeatureWordsExtractor_TfidfVectorizer(Classifier):
    name = "SVM with Function Words and TFIDF Vectorizer"
    def init_pipeline(self):
        parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'probability':[True], 'class_weight':['balanced', None]}
        svr = SVC()
        grid = GridSearchCV(svr, parameters)
        function_words_tfidf = FunctionWordsTFIDF()
        self.pipeline  = Pipeline([('feature_extraction', function_words_tfidf.extractor), ('clf', grid)])

class Classifier_RandomForest_FeatureWordsExtractor_CountVectorizer(Classifier):
    name = "Random Forest with Function Words and Count Vectorizer"
    def init_pipeline(self):
        parameters = {'criterion':('gini', 'entropy'), 'n_estimators':[100, 1000], 'class_weight':['balanced', 'balanced_subsample', None]}
        rfc = RandomForestClassifier()
        grid = GridSearchCV(rfc, parameters)
        function_words = FunctionWords()
        self.pipeline  = Pipeline([('feature_extraction', function_words.extractor), ('clf', grid)])


class Classifier_RandomForest_FeatureWordsExtractor_TfidfVectorizer(Classifier):
    name = "Random Forest with Function Words and TFIDF Vectorizer"
    def init_pipeline(self):
        parameters = {'criterion':('gini', 'entropy'), 'n_estimators':[100, 1000], 'class_weight':['balanced', 'balanced_subsample', None]}
        rfc = RandomForestClassifier()
        grid = GridSearchCV(rfc, parameters)
        function_words_tfidf = FunctionWordsTFIDF()
        self.pipeline  = Pipeline([('feature_extraction', function_words_tfidf.extractor), ('clf', grid)])

####################################################################################
#Char NGram Words Classifiers
class Classifier_SVM_CharNGRamExtractor_CountVectorizer(Classifier):
    name = "SVM with Char NGram and Count Vectorizer"
    def init_pipeline(self):
        parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'probability':[True], 'class_weight':['balanced', None]}
        svr = SVC()
        grid = GridSearchCV(svr, parameters)
        ngram_extractor = CountVectorizer(analyzer='char', ngram_range=(3,3))
        self.pipeline  = Pipeline([('feature_extraction', ngram_extractor), ('clf', grid)])


class Classifier_SVM_CharNGRamExtractor_TfidfVectorizer(Classifier):
    name = "SVM with Char NGram and TFIDF Vectorizer"
    def init_pipeline(self):
        parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'probability':[True], 'class_weight':['balanced', None]}
        svr = SVC()
        grid = GridSearchCV(svr, parameters)
        ngram_extractor = CountVectorizer(analyzer='char', ngram_range=(3,3))
        self.pipeline  = Pipeline([('feature_extraction', ngram_extractor), ('clf', grid)])

class Classifier_RandomForest_CharNGRamExtractor_CountVectorizer(Classifier):
    name = "Random Forest with Char NGram and Count Vectorizer"
    def init_pipeline(self):
        parameters = {'criterion':('gini', 'entropy'), 'n_estimators':[100, 1000], 'class_weight':['balanced', 'balanced_subsample', None]}
        rfc = RandomForestClassifier()
        grid = GridSearchCV(rfc, parameters)
        ngram_extractor = CountVectorizer(analyzer='char', ngram_range=(3,3))
        self.pipeline  = Pipeline([('feature_extraction', ngram_extractor), ('clf', grid)])

class Classifier_RandomForest_CharNGRamExtractor_TfidfVectorizer(Classifier):
    name = "Random Forest with Char NGram and TFIDF Vectorizer"
    def init_pipeline(self):
        parameters = {'criterion':('gini', 'entropy'), 'n_estimators':[100, 1000], 'class_weight':['balanced', 'balanced_subsample', None]}
        rfc = RandomForestClassifier()
        grid = GridSearchCV(rfc, parameters)
        ngram_extractor = CountVectorizer(analyzer='char', ngram_range=(3,3))
        self.pipeline  = Pipeline([('feature_extraction', ngram_extractor), ('clf', grid)])

def get_classifier_config(classifier_code:str)->dict:
    REGISTRY = {
        "svm_fw_cv": {"class": Classifier_SVM_FeatureWordsExtractor_CountVectorizer, "file": "models/svm_fw_cv.joblib"},
        "svm_fw_tfidf": {"class": Classifier_SVM_FeatureWordsExtractor_TfidfVectorizer, "file": "models/svm_fw_tfidf.joblib"},
        "rf_fw_cv": {"class": Classifier_RandomForest_FeatureWordsExtractor_CountVectorizer, "file": "models/rf_fw_cv.joblib"},
        "rf_fw_tfidf": {"class": Classifier_RandomForest_FeatureWordsExtractor_TfidfVectorizer, "file": "models/rf_fw_tfidf.joblib"},
        "svm_cng_cv": {"class": Classifier_SVM_CharNGRamExtractor_CountVectorizer, "file": "models/svm_cng_cv.joblib"},
        "svm_cng_tfidf": {"class": Classifier_SVM_CharNGRamExtractor_TfidfVectorizer, "file": "models/svm_cng_tfidf.joblib"},
        "rf_cng_cv": {"class": Classifier_RandomForest_CharNGRamExtractor_CountVectorizer, "file": "models/rf_cng_cv.joblib"},
        "rf_cng_tfidf": {"class": Classifier_RandomForest_CharNGRamExtractor_TfidfVectorizer, "file": "models/rf_cng_tfidf.joblib"},
    }
    return REGISTRY[classifier_code]








