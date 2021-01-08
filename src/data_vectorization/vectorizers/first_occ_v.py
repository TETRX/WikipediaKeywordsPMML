import json

class FirstOccVectorizer:
    def __init__(self, word_getter):
        self.word_getter=word_getter
    
    def vectorize(self,path_to_json):

        file=open(path_to_json,"r") 
        text=json.load(file)["text"]
        words=self.word_getter.get(text)
        result={}
        curr_pos=0
        for word in words:
            if not word in result:
                result[word]=curr_pos/len(words)
        return result
        

        