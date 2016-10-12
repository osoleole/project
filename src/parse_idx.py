from collections import defaultdict
import glob
import os

import utils


##########################
# Const for sec.gov path #
##########################
BASE_URL = "ftp://ftp.sec.gov/edgar/full-index/"
QTR = 'QTR'
IDX_FILE = 'company.idx'

#########################
# Const for local paths #
#########################
BASE_PATH = '/db/sec/index_files/'
SAVE_DIR = '/disk/sec/index_files/'

###########################
# Idx files header format #
###########################
HEADER = ['Company Name', 'Form Type', 'CIK', 'Date Filed', 'File Name' ]


###################################################
# Main functions for company.idx files processing #
###################################################
def normalize_idx(files, header):
    ''' Looks for header line in file by template. Process strings that follows after it '''
    is_found = False
    for file in files:
        with open(file, 'r') as f:
            for ln, line in enumerate(f):
                if is_header(header, line):
                    header_line = line
                    hl = ln + 2
                    is_found = True
                if is_found == True and ln >= hl:
                    print(get_record(header, header_line, line))  # Returns dictionary with header fields and values. 


def is_header(header, line):
    ''' Finds header line in company.indx. Returns True if the string id header'''
    return  all([v in line for v in header])


def list_idx():
    ''' Lists all idx files. Returns '''
    idx_files = glob.glob(os.path.join(BASE_PATH,'*.idx'))
    idx_files.sort()
    return idx_files


def files_path(start_year, end_year):
    '''Returns a list with the range of paths to master files 'company.idx'.'''
    return[BASE_PATH + str(year) + '_' + QTR + str(qtr) +  '_' +  IDX_FILE
             for qtr in range(1, 5) for year in range(start_year, end_year + 1)]



#####################################################################
# Functions to pocess headers and extract data fields from records. #
#####################################################################


def index_fields(header_fields, header):
    ''' Find 'start' and 'end' indexes of fields. Return the dictionary with the
    'field name' and 'start' and 'end' indexes '''
    indx = []
    indx_dict = dict()

    for v in header_fields:
        indx.append(header.index(v))
    indx.append(None)

    for i, v in enumerate(header_fields):
        di = dict()
        di['start'] = indx[i]
        di['end'] = indx[1:][i]
        indx_dict[v] = di

    return indx_dict


def get_record(header_fields, header, record):
    ''' Extracts fields from records. Returns dictionary with key as header and records as a record field'''
    indxs = index_fields(header_fields, header)
    records_dict = dict()

    for k, v in indxs.items():
        records_dict[k] = record[v['start']:v['end']].strip()

    return records_dict


header = 'Company Name                                                  Form Type   CIK         Date Filed  File Name'
files1= ['/db/sec/index_files/1993_QTR4_company.idx']
files2= ['/db/sec/index_files/1993_QTR4_company.idx','/db/sec/index_files/1995_QTR4_company.idx']

if __name__ == "__main__":
    #print(list_idx())
    normalize_idx(files2, HEADER)

