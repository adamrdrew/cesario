# Cesario
An experiment in machine learning authorship attribution as it pertains to the Shakespeare authorship question.

## Background
A small but persistent minority of Shakespeare scholars and enthusiasts mantain that the man William Shakespeare from Stratford-upon-Avon was not the author of the works attributed to William Shakespeare. This view is nowhere near the majority view in the field of Shakespeare scholarship, but has existed since at least Victorian times and persists to this day.

Many alternative authors are put forward, for many reasons, all of which is beyond the scope of this project. The goal of this project is to use machine learning based authorship attribution to weigh in on the issue in a neutral data scientific way. The author of this project has no hard opinion on the matter except for the slight bias in favor of the consensus schorlarly view that any layman has when approaching a subject outside their expertise.

## Training Data
We start with a large corpus of training data drawn from the amazing and wonderful Project Gutenberg. We divide our training set into two classes: Shakespeare and Not Shakespeare. The Shakespeare class is comprised of 26 source documents that includes most of Shakespeare's major plays, as well as the sonnets. The Not Shakespeare class contains 67 writings of various genres (plays, books, and poetry) from contemporary or near contemporary authors. This set is largely drawn from authors in the generation or two after Shakespeare so as to be close in language and subject matter but far enough in time to not include any candidates for alternative authorship.

The training data can be found in the `training` data and consists of the raw text files pulled from Project Gutenberg. The shakespeare set is in `training/shakespeare` and the rest in `training/other`. 

*Note: I consulted the Project Gutenberg License before including the documents in this repo and as I understand it this usage is within the scope of the license. If I am in error this is a good faith mistake and I am happy to remove them. Note that I originally tried getting the files on demand at run time but that does appear to be against the terms of service so I felt this was the better option.*

## Classifiers
We use the training data to train an ensemble of machine learning models with various feature extractors. These are constructed into easy to use plugin classes called Classifiers that abstract away the details of the models and present a consistent API. Our models are combinations of:

* Classifiers:
    * SVC - Support Vector Classifier
    * Random Forest
* Feature Selectors:
    * Custom funciton word extractor
    * Character n-gram extractor
* Vectorizers:
    * Count Vectorizer
    * TF/IDF Vectorizer

The classifiers are deployed an an ensemble which represents a model for each combination of the above. 

## Training
You can train the models via the cli:

```bash
$ python cesario/cesario.py train
```

The ensemble models are all trained with the training data set described above in the Training Data section.


## Validation
We offer two validation systems - test train split with manual validation and cross validation. Test train split is disabled by default because cross validation always produces roughly the same results, but you are free to enable it by uncommenting it from the `validate` method.

```
$ python cesario/cesario.py train ; python cesario/cesario.py validate
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
Training ensemble. This will take a while...
 * Getting training data...
 * Training individual classifiers...
     * Training SVM with Function Words and Count Vectorizer...
     * Saving SVM with Function Words and Count Vectorizer...
     * Training SVM with Function Words and TFIDF Vectorizer...
     * Saving SVM with Function Words and TFIDF Vectorizer...
     * Training Random Forest with Function Words and Count Vectorizer...
     * Saving Random Forest with Function Words and Count Vectorizer...
     * Training Random Forest with Function Words and TFIDF Vectorizer...
     * Saving Random Forest with Function Words and TFIDF Vectorizer...
     * Training SVM with Char NGram and Count Vectorizer...
     * Saving SVM with Char NGram and Count Vectorizer...
     * Training SVM with Char NGram and TFIDF Vectorizer...
     * Saving SVM with Char NGram and TFIDF Vectorizer...
     * Training Random Forest with Char NGram and Count Vectorizer...
     * Saving Random Forest with Char NGram and Count Vectorizer...
     * Training Random Forest with Char NGram and TFIDF Vectorizer...
     * Saving Random Forest with Char NGram and TFIDF Vectorizer...
Done!
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
Validating classifiers. This will take a while...
-----
 Cross Validation for: SVM with Function Words and Count Vectorizer
 Accuracy: 0.88 (+/- 0.26)
-----
 Cross Validation for: SVM with Function Words and TFIDF Vectorizer
 Accuracy: 0.92 (+/- 0.27)
-----
 Cross Validation for: Random Forest with Function Words and Count Vectorizer
 Accuracy: 0.95 (+/- 0.08)
-----
 Cross Validation for: Random Forest with Function Words and TFIDF Vectorizer
 Accuracy: 0.95 (+/- 0.06)
-----
 Cross Validation for: SVM with Char NGram and Count Vectorizer
 Accuracy: 0.95 (+/- 0.09)
-----
 Cross Validation for: SVM with Char NGram and TFIDF Vectorizer
 Accuracy: 0.95 (+/- 0.04)
-----
 Cross Validation for: Random Forest with Char NGram and Count Vectorizer
 Accuracy: 0.96 (+/- 0.03)
-----
 Cross Validation for: Random Forest with Char NGram and TFIDF Vectorizer
 Accuracy: 0.96 (+/- 0.02)
```

## Manual Testing
We provide a set of test data that is not derived from the training set that you can test manually. These include plays by Shakespeare along with works by near contempories.

```bash
$ for i in testing/shakespeare/*.txt; do python cesario/cesario.py predict --file $i; done 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook of A Midsummer Night’s Dream, by William Shakespeare
Ensemble Results:
-----------------------------
     * Is Shakespeare: True
     * Mean Probability: 0.61
     * Concordance: 99.375
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook of Macbeth, by William Shakespeare
Ensemble Results:
-----------------------------
     * Is Shakespeare: True
     * Mean Probability: 0.58
     * Concordance: 99.25
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg EBook of The Tempest, by William Shakespeare
Ensemble Results:
-----------------------------
     * Is Shakespeare: True
     * Mean Probability: 0.61
     * Concordance: 99.25
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook of Romeo and Juliet, by William Shakespeare
Ensemble Results:
-----------------------------
     * Is Shakespeare: True
     * Mean Probability: 0.74
     * Concordance: 99.0
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook of Hamlet, by William Shakespeare
Ensemble Results:
-----------------------------
     * Is Shakespeare: True
     * Mean Probability: 0.65
     * Concordance: 99.375
 
(cesario) [13:31] adamdrew @ adamwork: ~/Development/cesario [master]: Up-to-date
$ for i in testing/other/*.txt; do python cesario/cesario.py predict --file $i; done 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook, The Beggars Opera, by John Gay
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.77
     * Concordance: 100.0
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg EBook of The Works of Aphra Behn, by Aphra Behn
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.96
     * Concordance: 99.75
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg EBook of The Quiet Life, by Various
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.91
     * Concordance: 100.0
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook of The Pilgrim’s Progress, by John Bunyan
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.88
     * Concordance: 100.0
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg EBook of The Discovery of Guiana, by Sir Walter Raleigh
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.94
     * Concordance: 100.0
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg EBook of Diary of Samuel Pepys, August/September 1666
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.92
     * Concordance: 100.0
 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg EBook of No Cross, No Crown, by William Penn
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.97
     * Concordance: 100.0
 
(cesario) [13:32] adamdrew @ adamwork: ~/Development/cesario [master]: Up-to-date
$ 
```

## Predictions
You can get predictions either from a local file or a URL that houses a plain text file

```
$ python cesario/cesario.py predict --file testing/shakespeare/1514-0.txt 
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
The Project Gutenberg eBook of A Midsummer Night’s Dream, by William Shakespeare
Ensemble Results:
-----------------------------
     * Is Shakespeare: True
     * Mean Probability: 0.61
     * Concordance: 99.375
 
(cesario) [13:34] adamdrew @ adamwork: ~/Development/cesario [master]: Modified
$ python cesario/cesario.py predict --url https://www.gutenberg.org/cache/epub/25063/pg25063.txt
Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'
--------------------------------------------------------
Ensemble Results:
-----------------------------
     * Is Shakespeare: False
     * Mean Probability: 0.78
     * Concordance: 100.0
```

## Results 
Will be added after this project is publicly presented.

## Sources and Resources Consulted
* The poems of Edward de Vere were found on https://sourcetext.com/oxfords-poems/ and corroberated with http://www.oxford-shakespeare.com/oxfordspoems.html
* Savoy, Jacques. (2013). Feature selections for authorship attribution. 939-941. 10.1145/2480362.2480541.
* Stylistic Features Based on Sequential Rule Mining for Authorship Attribution - Mohamed Amine Boukhaled, Jean-Gabriel Ganascia, in Cognitive Approach to Natural Language Processing, 2017
* Learning Data Mining with Python by Robert Layton 