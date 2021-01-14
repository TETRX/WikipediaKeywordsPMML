import json

class DocCountVectorizer:
    def __init__(self, path_to_corpora_data,word_getter):
        self.path_to_corpora_data=path_to_corpora_data
        with open(self.path_to_corpora_data,"r") as file:
            self.corpora_data=json.load(file)
        self.word_getter=word_getter
    
    def vectorize(self,path_to_json):
        file=open(path_to_json,"r") 
        text=json.load(file)["text"]

        words=self.word_getter.get(text)
        result={}
        all_doc_count=self.corpora_data["all docs"]
        for word in words:
            doc_count=0
            if word in self.corpora_data.keys():
                doc_count=self.corpora_data[word]["doc_count"]
            result[word]=[(doc_count)/(all_doc_count)]
        return result