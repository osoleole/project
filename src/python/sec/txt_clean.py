import os
import sys

HOME = os.getenv("HOME")
DB_ROOT = 'db'
DATA_DIR = 'lamedoc/raw/books/txt'
DATA_PATH = os.path.join(HOME,DB_ROOT,DATA_DIR)
INPUT_FILE_NAME = 'raw_book1.txt'
INPUT_FILE_PATH = os.path.join(DATA_PATH,INPUT_FILE_NAME)
OUTPUT_FILE_NAME = 'clean_book1.txt'
OUTPUT_FILE_PATH = os.path.join(DATA_PATH,OUTPUT_FILE_NAME)

def remove_char(text, char):
    ''' Removes none ASCII symbols from the text.
    Returns text with ASCII symbols only. Untested with all cases and
    languges'''
    return ''.join([i if (ord(i) != char and ord(i) < 127) else '' for i in str(text)])


with open(INPUT_FILE_PATH, 'r') as f:
    ar = []
    for s in f:
        sc = remove_char(s, 10)
        ar.append(sc)
    txt = ' '.join(ar)
    print(txt)
    with open(OUTPUT_FILE_PATH, 'w') as fo:
        fo.write(txt)



if __name__ == "__main__":
    print("I am script")


