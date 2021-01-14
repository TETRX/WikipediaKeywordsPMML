import json
from typing import Text

class DataVectorizer:
    def __init__(self, partial_vectorizers, word_getter):
        self.partial_vectorizers=partial_vectorizers
        self.word_getter=word_getter

    def vectorize(self,path_to_json):
        partial_results=[]

        for v in self.partial_vectorizers:
            partial_results.append(v.vectorize(path_to_json))
        
        file=open(path_to_json,"r") 
        text=json.load(file)["text"]
        words=self.word_getter.get(text)
        vectors={}

        for word in words:
            vectors[word]=[]
            for res in partial_results:
                vectors[word]+=res[word]

        return vectors
