
from ..data_vectorization.data_vectorizer import DataVectorizer
from ..data_vectorization.word_getter import WordGetter
from ..data_vectorization.word_counter import WordCounter

from ..data_vectorization.filters.punctuation_filter import PunctuationFilter
from ..data_vectorization.filters.quirk_filter import QuirkFilter


from ..data_vectorization.vectorizers.in_parts_v import InPartsVectorizer
from ..data_vectorization.vectorizers.first_occ_v import FirstOccVectorizer
from ..data_vectorization.vectorizers.pos_v import POSVectorizer
from ..data_vectorization.vectorizers.word_count_v import WordCountVectorizer
from ..data_vectorization.vectorizers.doc_count_v import DocCountVectorizer
from ..data_vectorization.vectorizers.is_keyword_v import IsKeywordVectorizer

import os

corpora="data/corpora_data.json"

filters=[PunctuationFilter(),QuirkFilter()]
word_getter=WordGetter(filters)
word_counter=WordCounter(word_getter)
vectorizers=[DocCountVectorizer(corpora,word_getter),WordCountVectorizer(corpora,word_counter),FirstOccVectorizer(word_getter),POSVectorizer(word_getter),InPartsVectorizer(word_getter),IsKeywordVectorizer(word_getter)]

vectorizer=DataVectorizer(vectorizers,word_getter)

datapath=os.path.abspath("data/manual")
filenames=os.listdir(datapath)
filepaths=[os.path.join(datapath,filename) for filename in filenames]

vector_dicts=[]

for filepath in filepaths:
    vector_dicts.append(vectorizer.vectorize(filepath))

vectors=[]

for vector_dict in vector_dicts:
    for _, vector in vector_dict.items():
        vectors.append(vector)

for vector in vectors:
    print(*vector)