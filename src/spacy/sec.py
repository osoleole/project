import os
import sys
import codecs
import spacy
import pandas as pd
import itertools as it

HOME = os.getenv("HOME")
DB_ROOT = 'db'
DATA_DIR = 'lamedoc/raw/books/txt'
DATA_PATH = os.path.join(HOME,DB_ROOT,DATA_DIR)
INPUT_FILE_NAME = 'clean_book1.txt'
INPUT_FILE_PATH = os.path.join(DATA_PATH,INPUT_FILE_NAME)

nlp = spacy.load('en')

with codecs.open(INPUT_FILE_PATH, encoding='utf_8') as f:
    raw_text = f.read()

print(raw_text)




if __name__ == "__main__":
    print(INPUT_FILE_PATH)

