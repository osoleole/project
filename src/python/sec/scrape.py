# Module for getting files from sites.
# Uses wget.

import subprocess
import os

SAVE_DIR = '/disk/sec/index_files/'
BASE_URL = "ftp://ftp.sec.gov/edgar/full-index/"
QTR = 'QTR'
IDX_FILE = 'company.idx'


def filename_from_url(url):
    return '_'.join(url.split('/')[-3:])

def create_urls(start_year, end_year):
    '''Returns a list with the range of URLs of master files 'company.idx'.'''
    return [BASE_URL + str(year) + "/" + QTR + str(x) + "/" + IDX_FILE
             for x in range(1, 5) for year in range(start_year, end_year + 1)]

def download(start_year,end_year):
    ''' Takes the list of links. Uses wget to download.'''
    urls = create_urls(start_year, end_year) 
    [subprocess.run(['wget', url, '-O', SAVE_DIR + filename_from_url(url)],
                     stdout=None, stderr=None) for url in urls]


if __name__ == "__main__":
    download(1993,1999)


