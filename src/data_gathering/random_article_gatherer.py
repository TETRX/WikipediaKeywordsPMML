import wikipedia
import os
import json

class RandomArticleGatherer():
    def __init__(self, path, summary=False, section_titles=False):
        self.path=os.path.abspath(path)
        self.summary=summary
        self.section_titles=section_titles

    def get_random(self):
        random_wiki=wikipedia.random(1)
        random_load=wikipedia.page(random_wiki)
        to_json={}
        to_json["title"]=random_load.title
        to_json["text"]=random_load.content
        to_json["link"]=random_load.url
        if self.summary:
            to_json["summary"]=random_load.summary
        if self.section_titles:
            to_json["section titles"]=" ".join(random_load.sections)

        to_json["keywords"]=[]
        
        path=os.path.join(self.path,to_json["title"]+".json")
        with open(path, 'w') as f:
            json.dump(to_json, f)