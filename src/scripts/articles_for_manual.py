from ..data_gathering.random_article_gatherer import RandomArticleGatherer

N_ARTICLES=206

random_art=RandomArticleGatherer("data/manual/",section_titles=True,summary=True)

for i in range(N_ARTICLES):
    try:
        random_art.get_random()
    except:
        i-=1