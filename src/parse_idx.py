from collections import defaultdict
import glob
import os

SAVE_DIR = '/disk/sec/index_files/'
BASE_URL = "ftp://ftp.sec.gov/edgar/full-index/"
QTR = 'QTR'
IDX_FILE = 'company.idx'


BASE_PATH = '/db/sec/index_files/'
COMPANY_NAME = 'Company Name'
FORM_TYPE = 'Form Type'
CIK = 'CIK'
DATE_FIELD = 'Date Filed'
FILE_NAME = 'File Name'
#STARTLINE = len(f)
VALUES = [COMPANY_NAME, FORM_TYPE, CIK, DATE_FIELD, FILE_NAME, ]
INDXS = dict()
DATA = []


def list_idx():
    ''' Lists all idx files. Returns '''
    idx_files = glob.glob(os.path.join(BASE_PATH,'*.idx'))
    idx_files.sort()
    return idx_files


def is_header(header, line):
    return  all([v in line for v in header])


def normalize_idx(files):
    for file in files:
        with open(file, 'r') as f:
            print(f)
            for i, line in enumerate(f.readlines()):
                if is_header(VALUES, line):
                    print(i)
                    for val in VALUES:
                        INDXS[val] = line.index(val)
                        sl = i + 2
                break


def files_path(start_year, end_year):
    '''Returns a list with the range of paths to  master files 'company.idx'.'''
    return[BASE_PATH + str(year) + '_' + QTR + str(qtr) +  '_' +  IDX_FILE
             for qtr in range(1, 5) for year in range(start_year, end_year + 1)]

'''
for line in f[STARTLINE:]:
    company_data = {}
    for val in VALUES:
        indxs = INDXS[val]
        company_data[val] = line[indxs['start']: indxs.get('end', len(line))].strip()
    DATA.append(company_data)
'''
files= ['/db/sec/index_files/1993_QTR4_company.idx']

if __name__ == "__main__":
    #print(list_idx())
    normalize_idx(files_path(2011,2015))

