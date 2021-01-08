import os
import json


class CorporaDataGatherer:
    def __init__(self,path_to_dir,path_to_json, word_counter):
        self.path_to_dir=path_to_dir
        self.path_to_json=path_to_json
        self.word_counter=word_counter

    def gather(self):
        results=dict()
        for filename in os.listdir(self.path_to_dir):
            filepath=os.path.join(self.path_to_dir,filename)
            with open(filepath,"r") as file:
                text=json.load(file)["text"]
                self.word_counter.count_words_in(text)
        
        results=dict()
        for word in self.word_counter.word_doc_counter:
            results[word]={
                "doc_count": self.word_counter.word_doc_counter[word],
                "occurence_count": self.word_counter.word_occurence_counter[word]
            }

        results["all words"]=self.word_counter.all_word_counter
        results["all docs"]=self.word_counter.all_doc_counter
        with open(self.path_to_json,"w") as result_file:
            json.dump(results,result_file)