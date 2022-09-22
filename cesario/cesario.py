
from enum import Flag
from classifiers import get_classifier_config
import click
from training import Training
from book import Book
from joblib import dump, load
import statistics

#The codes for the ensemble models
ENSEMBLE = ["svm_fw_cv", 
"svm_fw_tfidf", 
"rf_fw_cv", 
"rf_fw_tfidf", 
"svm_cng_cv", 
"svm_cng_tfidf", 
"rf_cng_cv", 
"rf_cng_tfidf"]

#This is the dummy group method used for Click
@click.group()
def cli():
    pass

#Load the ensemble models
def load_models() -> list:
    try:
        loaded_classifiers = []
        for classifier_code in ENSEMBLE:
            classifier_dict = get_classifier_config(classifier_code)
            model = load(classifier_dict["file"])
            loaded_classifiers.append(model)
        return loaded_classifiers
    except:
        print("Models not found. Please run 'cesario train' first.")
        exit(1)


#Run cross validation on the ensemble models
@cli.command("validate")
@click.option('--split-docs', is_flag=True, help='On ingest, split docs to 65k character chunks.')
def validate(split_docs):
    print("Validating classifiers. This will take a while...")
    for classifier_code in ENSEMBLE:
        classifier_dict = get_classifier_config(classifier_code)
        cross_validate_classifier(classifier_dict["class"], split_docs)

#Runs cross validation on a sinlge classifier
def cross_validate_classifier(classifier_class, split_docs:bool=False):
    books, classes = Training.get_training_data(split_docs)
    classifier = classifier_class(books, classes)
    scores = classifier.cross_validate()
    print("-----")
    print(" Cross Validation for: " + classifier.name)
    print(" Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

#For a given doc get the prediction results for each classifier in the ensemble
def get_ensemble_prediction_results(doc:str) -> list:
    loaded_classifiers = load_models()
    results = []
    for classifier in loaded_classifiers:
        prediction = {"is_shakespeare": False, "probability": 0}
        prediction["is_shakespeare"] = bool(classifier.predict(doc)[0])
        prediction["probability"] = classifier.predict_with_probability(doc)[0][classifier.predict(doc)[0]]
        results.append(prediction)
    return results

#Process and aggregate the results from the ensemble
def process_ensemble_prediction_results(results:list) -> dict:
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
def ensemble_predict_simple(doc:str) -> dict:
    results = get_ensemble_prediction_results(doc)
    return process_ensemble_prediction_results(results)

#Prints the ensemble results
def print_ensemble_results(result):
    print("Ensemble Results:")
    print("-----------------------------")
    print("     * Is Shakespeare: " + str(result["is_shakespeare"]))
    print("     * Mean Probability: %0.2f" % result["probability"])
    print("     * Concordance: " + str(result["concordance"]))
    print(" ")

#Get a prediction from the ensemble for a given file or URL
@cli.command("predict")
@click.option('--file', default="",  help='Predict the authorship of a local file.')
@click.option('--url', default="",  help='Predict the authorship of a file on a web server.')
def predict(file:str, url:str):
    if file == "" and url == "":
        print("Please specify a file or URL.")
        exit(1)
    if file != "" and url != "":
        print("Please specify only one file or URL.")
        exit(1)
    if file != "":
        predict_file(file)
        exit(0)
    if url != "":
        predict_url(url)
        exit(0)

#Get the prediction for the remote URL
def predict_url(url:str):
    classifiers = load_models()
    book = Book({"url":url, "is_shakespeare": False})
    book.load()
    result = ensemble_predict_simple(book.content_lines())
    print_ensemble_results(result)

#Get the prediction for the local file
def predict_file(file:str):
    classifiers = load_models()
    f = open(file,'r')
    text = f.read()
    print(text.split("\n")[0])
    result = ensemble_predict_simple(text)
    print_ensemble_results(result)

#Train the ensemble
@cli.command("train")
@click.option('--split-docs', is_flag=True, help='On ingest, split docs to 65k character chunks.')
def train(split_docs:bool):
    print("Training ensemble. This will take a while...")
    print(" * Getting training data...")
    books, classes = Training.get_training_data(split_docs)
    print(" * Training individual classifiers...")
    for classifier_code in ENSEMBLE:
        classifier_dict = get_classifier_config(classifier_code)
        classifier = classifier_dict["class"](books, classes)
        print("     * Training " + classifier.name + "...")
        classifier.train()
        print("     * Saving " + classifier.name + "...")
        dump(classifier, classifier_dict["file"])
    print("Done!")

#Entrypoint
if __name__ == '__main__':
    print("Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'")
    print("--------------------------------------------------------")
    cli()