import json

class WordCountVectorizer:
    def __init__(self, path_to_corpora_data,word_counter):
        self.path_to_corpora_data=path_to_corpora_data
        with open(self.path_to_corpora_data,"r") as file:
            self.corpora_data=json.load(file)
        self.word_counter=word_counter
    
    def vectorize(self,path_to_json):
        file=open(path_to_json,"r") 
        text=json.load(file)["text"]
        
        self.word_counter.count(text)
        words=self.word_counter.word_doc_counter.keys()
        result={}
        all_words_count=self.corpora_data["all words"]
        for word in words:
            result[word]=[((self.word_counter.word_occurence_counter[word]+1)/(self.word_counter.all_word_counter+1))
            /((self.corpora_data[word]["occurence_count"]+1)/(all_words_count+1))]
        return result