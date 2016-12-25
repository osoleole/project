import sys
import os
from datetime import datetime

PROJECT_ROOT = '/home/astra/work/projects/lamedoc_new/project/'
sys.path.append(os.path.dirname(PROJECT_ROOT))

from settings import settings

def make_filename(filename, stage, file_type='text'):
    '''file_type 'text' or 'model'. By default it is text '''
    date_time = "{:%d_%m_%Y_%H_%M}".format(datetime.now())
    if file_type == 'text':
        return "{}_{}_{}.txt".format(filename, stage, date_time)
    elif file_type == 'model':
        return "{}_{}_model_{}".format(filename, stage, date_time)

def init_paths():
    return {'unigram_text_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(settings.FILE_NAME, settings.UNIGRAM)),
            'bigram_model_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(settings.FILE_NAME, settings.BIGRAM, file_type='model')),
            'bigram_text_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(settings.FILE_NAME, settings.BIGRAM)),
            'trigram_model_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(settings.FILE_NAME, settings.TRIGRAM, file_type='model')),
            'trigram_text_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(settings.FILE_NAME, settings.TRIGRAM)),
            'normalized_text_filepath':os.path.join(settings.NORMALIZED_DATA_PATH, make_filename(settings.FILE_NAME, settings.NORMALIZED))}