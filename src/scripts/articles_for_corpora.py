from time import sleep
from nltk.util import pr
from wikipedia import exceptions
from ..data_gathering.random_article_gatherer import RandomArticleGatherer

N_ARTICLES=10000

random_art=RandomArticleGatherer("data/corpora/")

exceptions_num=0

for i in range(N_ARTICLES):
    print("getting the "+str(i)+"th article")
    try:
        random_art.get_random()
    except:
        exceptions_num+=1
        sleep(1) #so that you can kill it with ctrl+c in the mean time :D

print("failed to get "+str(exceptions_num)+" articles")