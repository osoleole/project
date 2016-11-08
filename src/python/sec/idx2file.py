import os
import re
import urllib.request
from config import BASE_DIR

TEST_PATH = 'edgar/data/1539425/0001193125-12-441828.txt'
TEST_URL = 'https://www.sec.gov/Archives/edgar/data/1539425/0001193125-12-441828.txt'

def modify_path(path):
    '''Returns path without extension and hyphens'''
    return os.path.splitext(path)[0].replace('-','')


def get_filename_links(path):
    ''' Returns a list of urls with documents. By the nature of the content
    we usually only need the first url in the list [0]. The document name
    we are interested in, follows the <FILENAME> tag'''
    links = []
    url = os.path.join(BASE_DIR, path)
    url_norm = modify_path(url)
    filename, headers = urllib.request.urlretrieve(url)
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('<FILENAME>'):
                m = re.search('(?<=<FILENAME>)\w+.+', line)
                links.append(os.path.join(url_norm, m.group(0)))
    return links

print(get_filename_links(TEST_PATH))

