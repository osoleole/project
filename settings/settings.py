import sys
import os
from datetime import datetime

#PROJECT_ROOT = os.path.dirname(os.getcwd())
#sys.path.append(os.path.dirname(PROJECT_ROOT))

UNIGRAM = 'unigram'
BIGRAM = 'bigram'
TRIGRAM = 'trigram'
NORMALIZED = 'normalized'
MODEL = 'model'
W2V = 'w2v'
FILE_NAME = 'wiki'

HOME = os.getenv("HOME")
DB_ROOT = os.path.join(HOME,'db')
# Raw data path
RAW_DATA_DIR = 'processed_text/clean'
RAW_DATA_PATH = os.path.join(HOME,DB_ROOT,RAW_DATA_DIR)
# Processed data path
PROCESSED_DATA_DIR = 'processed_text'
PROCESSED_DATA_PATH = os.path.join(HOME,DB_ROOT,PROCESSED_DATA_DIR)
# N-grams data path
NGRAMS_DATA_PATH = os.path.join(PROCESSED_DATA_PATH,'ngrams')
# Normailezed data path
NORMALIZED_DATA_PATH = os.path.join(PROCESSED_DATA_PATH,'normalized')
# Models data path
MODELS_DATA_DIR = 'models'
MODELS_DATA_PATH = os.path.join(HOME,DB_ROOT, MODELS_DATA_DIR) 