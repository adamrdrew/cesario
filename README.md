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

### Training Document Splitting
We offer two different training data ingestion methods. One method processes and indexes the training documents in whole. The other method splits the training data into sub documents of 65k characters or less. 

## Validation
We offer two validation systems - test train split with manual validation and cross validation. Test train split is disabled by default because cross validation always produces roughly the same results, but you are free to enable it by uncommenting it from the `validate` method.



## Results


## Sources
* The poems of Edward de Vere were found on https://sourcetext.com/oxfords-poems/ and corroberated with http://www.oxford-shakespeare.com/oxfordspoems.html