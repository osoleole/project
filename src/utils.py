# Regular expressions for SEC (sec.gov) URL construction.
import os
import re

BASE_URL = "ftp://ftp.sec.gov/edgar/full-index/"
DATA_DIR = 'data'
DATA_BASE_PATH = os.path.join(os.getenv('HOME'), DATA_DIR)
IDX_FILE = "company.idx"
QTR = "QTR"

text = "123-45-789-234.txt"


def make_csf(str):
    '''Normalizes complete submission file name CSF'''
    return str.replace('-', '').replace('.txt', '')


def make_idx_url(year, qtr, base_url=BASE_URL):
    '''Returns a list with an URL of master file 'company.idx'.'''
    return base_url + str(year) + '/' + QTR + str(qtr) + '/' + IDX_FILE


def make_range_idx_url(start_year, end_year):
    '''Returns a list with the range of URLs of master files 'company.idx'.'''
    return [[[BASE_URL + str(year) + "/" + QTR + str(x) + "/" + IDX_FILE]
            for x in range(1, 5)] for year in range(start_year, end_year + 1)]


def make_dir(path):
    '''Create directory based on path'''
    if not os.path.exists(path):
        os.makedirs(path)


def make_dirs(start_year, end_year):
    '''Create dirs using list of paths'''
    paths = [DATA_BASE_PATH + '/' + str(year) + "/" + QTR + str(x)
             for x in range(1, 5) for year in range(start_year, end_year + 1)]
    for path in paths:
        make_dir(path)


def remove_none_ascii(text):
    ''' Removes none ASCII symbols from the text.
    Returns text with ASCII symbols only. Untested with all cases and 
    languges'''
    return ''.join([i if ord(i) < 128 else '' for i in str(text)])


# def extract_name(file_name):  


if __name__ == "__main__":
    print(make_idx_url(1993, 3, "good_man/"))
    make_dirs()
