from ..data_vectorization.corpora_data_gatherer import CorporaDataGatherer
from ..data_vectorization.word_counter import WordCounter
from ..data_vectorization.word_getter import WordGetter
from ..data_vectorization.filters.quirk_filter import QuirkFilter
from ..data_vectorization.filters.punctuation_filter import PunctuationFilter

filters=[QuirkFilter(),PunctuationFilter()]
word_getter=WordGetter(filters)
word_counter=WordCounter(word_getter)
data_gatherer=CorporaDataGatherer("data/corpora/","data/corpora_data.json",word_counter)

data_gatherer.gather()