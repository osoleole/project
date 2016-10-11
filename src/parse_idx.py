from collections import defaultdict
import glob
import os

import utils

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
    ''' Finds header line in company.indx'''
    return  all([v in line for v in header])


def index_header(header):
    ''' Gets string of headers from file. Returns dictionary {'field_name: index}'''
    val_indx = dict()
    for value in VALUES:
        l = [0,0]
        l[0] = header.index(value)
        val_indx[value] = l
        print(val_indx)


def normalize_idx(files):
    header = False
    for file in files:
        with open(file, 'r') as f:
            for ln, line in enumerate(f):
                if is_header(VALUES, line):
                    hl = ln + 2
                    header = True
                    for val in VALUES:
                        INDXS[val] = line.index(val)
                if header == True and ln >= hl:
                    print(line)


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
header = 'Company Name                                                  Form Type   CIK         Date Filed  File Name'
files1= ['/db/sec/index_files/1993_QTR4_company.idx']
files2= ['/db/sec/index_files/1993_QTR4_company.idx','/db/sec/index_files/1995_QTR4_company.idx']

if __name__ == "__main__":
    #print(list_idx())
    print(index_header(header))
    normalize_idx(files1)

