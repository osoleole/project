import os


HOME = os.getenv("HOME")
DB_ROOT = 'db'
DATA_DIR = 'lamedoc/raw/books/txt'
DATA_PATH = os.path.join(HOME,DB_ROOT,DATA_DIR)
INPUT_FILE_NAME = 'clean_book1.txt'
INPUT_FILE_PATH = os.path.join(DATA_PATH,INPUT_FILE_NAME)


