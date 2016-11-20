import os
import codecs
from gensim.models import Word2Vec
from gensim.models import Phrases
from gensim.models.word2vec import LineSentence
import pandas as pd

import settings

trigram_sentences = LineSentence(os.path.join(settings.DATA_PATH,
                                              'trigram_sentences.txt' ))
word2vec_filepath = os.path.join(settings.DATA_PATH, 'word2vec_model')

if 0 == 1:
    text2vec = Word2Vec(trigram_sentences, size=100, window=5,
                        min_count=20, sg=1, workers=4)
    text2vec.save(word2vec_filepath)
    for i in range(1,12):
        text2vec.train(trigram_sentences)
        text2vec.save(word2vec_filepath)

text2vec = Word2Vec.load(word2vec_filepath)
text2vec.init_sims()

print('{} training epochs so far.'.format(text2vec.train_count))
print('{:,} terms in the text2vec vocabulary.'.format(len(text2vec.vocab)))

# Work with pandas
ordered_vocab = [(term, voc.index, voc.count)
                 for term, voc in text2vec.vocab.items()]
#ordered_vocab = sorted(ordered_vocab, key=lambda count: -count)
ordered_terms, term_indices, term_counts = zip(*ordered_vocab)
#word_vectors = pd.DataFrame(text2vec.syn0norm[term_indices, :],
#                            index=ordered_terms)
print(ordered_terms)

# Terms relations

def get_related_terms(token, topn=10):
    for word, similarity in text2vec.most_similar(positive=[token], topn=topn):
        print('{:20} {}'.format(word, round(similarity, 3)))

get_related_terms('cost')

