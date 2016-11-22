import os

HOME = os.getenv("HOME")
DB_ROOT = os.path.join(HOME,'db')

# Raw data path
RAW_DATA_DIR = 'lamedoc/raw/sec'
RAW_DATA_PATH = os.path.join(HOME,DB_ROOT,RAW_DATA_DIR)

# Processwd data path
PROCESSED_DATA_DIR = 'lamedoc/processed/sec'
PROCESSED_DATA_PATH = os.path.join(HOME,DB_ROOT,PROCESSED_DATA_DIR)

# N-grams data path
NGRAMS_DATA_PATH = os.path.join(PROCESSED_DATA_PATH,'ngrams')

# Normailezed data path
NORMALIZED_DATA_PATH = os.path.join(PROCESSED_DATA_PATH,'normalized')

#INPUT_FILE_NAME = 'clean_book1.txt'
#INPUT_FILE_PATH = os.path.join(DATA_PATH,INPUT_FILE_NAME)


