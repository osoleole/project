import os
import codecs
import spacy
import settings

nlp = spacy.load('en')

def remove_puncts(token):
    '''Returns True in case of puncts or space'''
    return token.is_space or token.is_punct

def text_to_sentence(filename):
    '''Returns generator of sentences'''
   with codecs.open(filename, 'r') as f:
        for line in f:
            yield line.replace('\\n','\n')

# Lemmatize text.
def lemmatize_text(filename):
    for parsed_text in nlp.pipe(text_to_sentence(filename),
                                  batch_size=10000, n_threads=4):
        for sentence in parsed_text.sents:
            yield ' '.join([token.lemma_ for token in sentence
                             if not remove_puncts(token)])


lemmatized_filepath = os.path.join(settings.DATA_PATH, 'lemmatized.txt')
raw_file_filepath = os.path.join(settings.DATA_PATH, 'clean_book1.txt')

with codecs.open(lemmatized_filepath, 'w', encoding='utf_8') as f:
    for sentence in lemmatize_text(raw_file_filepath):
        f.write(sentence + '\n')
