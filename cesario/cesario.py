
from enum import Flag
from classifiers import get_classifier_config
import click
from training import Training
from book import Book
from joblib import dump, load
import statistics
from libcesario import LibCesario

lib_cesario = LibCesario()

#This is the dummy group method used for Click
@click.group()
def cli():
    pass

#Run cross validation on the ensemble models
@cli.command("validate")
@click.option('--split-docs', is_flag=True, help='On ingest, split docs to 65k character chunks.')
def validate(split_docs):
    lib_cesario.validate(split_docs)


#Get a prediction from the ensemble for a given file or URL
@cli.command("predict")
@click.option('--file', default="",  help='Predict the authorship of a local file.')
@click.option('--url', default="",  help='Predict the authorship of a file on a web server.')
def predict(file:str, url:str):
    lib_cesario.predict(file, url)


#Train the ensemble
@cli.command("train")
@click.option('--split-docs', is_flag=True, help='On ingest, split docs to 65k character chunks.')
def train(split_docs:bool):
    lib_cesario.train(split_docs)

#Entrypoint
if __name__ == '__main__':
    print("Cesario v0.1.0 - 'Disguise, I see thou art a wickedness'")
    print("--------------------------------------------------------")
    cli()