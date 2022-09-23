
from enum import Flag
from classifiers import get_classifier_config
import click
from training import Training
from book import Book
from joblib import dump, load
import statistics

class LibCesario:

    #The codes for the ensemble models
    ENSEMBLE = ["svm_fw_cv", 
    "svm_fw_tfidf", 
    "rf_fw_cv", 
    "rf_fw_tfidf", 
    "svm_cng_cv", 
    "svm_cng_tfidf", 
    "rf_cng_cv", 
    "rf_cng_tfidf"]

    #Load the ensemble models
    def load_models(self) -> list:
        try:
            loaded_classifiers = []
            for classifier_code in self.ENSEMBLE:
                classifier_dict = get_classifier_config(classifier_code)
                model = load(classifier_dict["file"])
                loaded_classifiers.append(model)
            return loaded_classifiers
        except:
            print("Models not found. Please run 'cesario train' first.")
            exit(1)


    #Run cross validation on the ensemble models
    def validate(self, split_docs):
        print("Validating classifiers. This will take a while...")
        for classifier_code in self.ENSEMBLE:
            classifier_dict = get_classifier_config(classifier_code)
            self.cross_validate_classifier(classifier_dict["class"], split_docs)

    #Runs cross validation on a sinlge classifier
    def cross_validate_classifier(self, classifier_class, split_docs:bool=False):
        books, classes = Training.get_training_data(split_docs)
        classifier = classifier_class(books, classes)
        scores = classifier.cross_validate()
        print("-----")
        print(" Cross Validation for: " + classifier.name)
        print(" Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    #For a given doc get the prediction results for each classifier in the ensemble
    def get_ensemble_prediction_results(self, doc:str) -> list:
        loaded_classifiers = self.load_models()
        results = []
        for classifier in loaded_classifiers:
            prediction = {"is_shakespeare": False, "probability": 0}
            prediction["is_shakespeare"] = bool(classifier.predict(doc)[0])
            prediction["probability"] = classifier.predict_with_probability(doc)[0][classifier.predict(doc)[0]]
            results.append(prediction)
        return results

    #Process and aggregate the results from the ensemble
    def process_ensemble_prediction_results(self, results:list) -> dict:
        is_shakespeare_count = 0
        result_count = 0
        probabilities = []
        for result in results:
            result_count += 1 
            if result["is_shakespeare"] == True: 
                is_shakespeare_count += 1
            probabilities.append(result["probability"])
        is_shakespeare = is_shakespeare_count > result_count / 2
        probability = statistics.mean(probabilities)
        concordance = 100 - (is_shakespeare_count / result_count)
        return {"is_shakespeare": is_shakespeare, "probability": probability, "concordance": concordance}

    #Gets an ensemble prediction for the given doc and processes it
    def ensemble_predict_simple(self, doc:str) -> dict:
        results = self.get_ensemble_prediction_results(doc)
        return self.process_ensemble_prediction_results(results)

    #Prints the ensemble results
    def print_ensemble_results(self, result):
        print("Ensemble Results:")
        print("-----------------------------")
        print("     * Is Shakespeare: " + str(result["is_shakespeare"]))
        print("     * Mean Probability: %0.2f" % result["probability"])
        print("     * Concordance: " + str(result["concordance"]))
        print(" ")

    #Get a prediction from the ensemble for a given file or URL
    def predict(self, file:str, url:str):
        if file == "" and url == "":
            print("Please specify a file or URL.")
            exit(1)
        if file != "" and url != "":
            print("Please specify only one file or URL.")
            exit(1)
        if file != "":
            self.predict_file(file)
            exit(0)
        if url != "":
            self.predict_url(url)
            exit(0)

    #Get the prediction for the remote URL
    def predict_url(self, url:str):
        classifiers = self.load_models()
        book = Book({"url":url, "is_shakespeare": False})
        book.load()
        result = self.ensemble_predict_simple(book.content_lines())
        self.print_ensemble_results(result)

    #Get the prediction for the local file
    def predict_file(self, file:str):
        classifiers = self.load_models()
        f = open(file,'r')
        text = f.read()
        print(text.split("\n")[0])
        result = self.ensemble_predict_simple(text)
        self.print_ensemble_results(result)

    #Train the ensemble
    def train(self, split_docs:bool):
        print("Training ensemble. This will take a while...")
        print(" * Getting training data...")
        books, classes = Training.get_training_data(split_docs)
        print(" * Training individual classifiers...")
        for classifier_code in self.ENSEMBLE:
            classifier_dict = get_classifier_config(classifier_code)
            classifier = classifier_dict["class"](books, classes)
            print("     * Training " + classifier.name + "...")
            classifier.train()
            print("     * Saving " + classifier.name + "...")
            dump(classifier, classifier_dict["file"])
        print("Done!")