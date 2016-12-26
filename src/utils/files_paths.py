import sys
import os
from datetime import datetime

#PROJECT_ROOT = '/home/astra/work/projects/lamedoc_new/project/'
#sys.path.append(os.path.dirname(PROJECT_ROOT))

PROJECT_ROOT = '/home/astra/work/projects/lamedoc_new/project/'
if os.path.dirname(PROJECT_ROOT) not in sys.path:
    sys.path.append(os.path.dirname(PROJECT_ROOT))

from settings import settings

def make_filename(file_name, stage, file_type='text'):
    '''file_type 'text' or 'model'. By default it is text '''
    date_time = "{:%d_%m_%Y_%H_%M}".format(datetime.now())
    if file_type == 'text':
        return "{}_{}_{}.txt".format(os.path.splitext(file_name)[0], stage, date_time)
    elif file_type == 'model':
        return "{}_{}_model_{}".format(os.path.splitext(file_name)[0], stage, date_time)

def init_paths(file_name):
    return {'unigram_text_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(file_name, settings.UNIGRAM)),
            'bigram_model_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(file_name, settings.BIGRAM, file_type='model')),
            'bigram_text_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(file_name, settings.BIGRAM)),
            'trigram_model_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(file_name, settings.TRIGRAM, file_type='model')),
            'trigram_text_filepath':os.path.join(settings.NGRAMS_DATA_PATH, make_filename(file_name, settings.TRIGRAM)),
            'normalized_text_filepath':os.path.join(settings.NORMALIZED_DATA_PATH, make_filename(file_name, settings.NORMALIZED))}

def model_init_path(file_name):
    return {'w2v_model_filepath':os.path.join(settings.MODELS_DATA_PATH, make_filename(file_name, settings.W2V, file_type='model'))}