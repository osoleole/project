import os
import codecs
import itertools as it
from gensim.models import Phrases
from gensim.models.word2vec import LineSentence

import settings

lemmatized = LineSentence(os.path.join(settings.DATA_PATH, 'lemmatized.txt'))
bigram_model_filepath = os.path.join(settings.DATA_PATH, 'bigram_model')

if 0 == 1:
    bigram_model = Phrases(lemmatized)
    bigram_model.save(bigram_model_filepath)

bigram_model = Phrases.load(bigram_model_filepath)
bigram_sentences_filepath = os.path.join(settings.DATA_PATH,
                                         'bigram_sentences.txt')

if 0 == 1:
    with codecs.open(bigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for sentence in lemmatized:
            bigram_sentence = ' '.join(bigram_model[sentence])
            f.write(bigram_sentence + '\n')

bigram_sentences = LineSentence(bigram_sentences_filepath)
trigram_model_filepath = os.path.join(settings.DATA_PATH,'trigram_model')

if 0 == 1:
    trigram_model = Phrases(bigram_sentences)
    trigram_model.save(trigram_model_filepath)

trigram_model = Phrases.load(trigram_model_filepath)
trigram_sentences_filepath = os.path.join(settings.DATA_PATH,
                                          'trigram_sentences.txt')
if 0 == 1:
    with codecs.open(trigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for sentence in bigram_sentences:
            trigram_sentence = ' '.join(trigram_model[sentence])
            f.write(trigram_sentence + '\n')

trigram_text_filepath = os.path.join(intermediate_directory,
                                        'trigram_transformed_text.txt')

f 0 == 1:
    with codecs.open(trigram_reviews_filepath, 'w', encoding='utf_8') as f:
        for parsed_review in nlp.pipe(line_review(review_txt_filepath),
                                      batch_size=10000, n_threads=4)
        unigram_review = [token.lemma_ for token in parsed_review
                          if not punct_space(token)
        bigram_review = bigram_model[unigram_review]
        trigram_review = trigram_model[bigram_review]
        trigram_review = [term for term in trigram_review if term not
                          in spacy.en.STOPWORDS]
        trigram_review = ' '.join(trigram_review)
        f.write(trigram_review + '\n')
