import json
import nltk
from nltk.tag import pos_tag

class POSVectorizer:
    def __init__(self,word_getter):
        self.word_getter=word_getter

    def vectorize(self,path_to_json):
        file=open(path_to_json,"r") 
        text=json.load(file)["text"]
        tokenized_text = nltk.sent_tokenize(text)
        pos_tagged_text= nltk.pos_tag_sents(tokenized_text)

        words=self.word_getter.get(text)

        result={}

        
