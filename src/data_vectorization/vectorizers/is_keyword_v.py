import json

class IsKeywordVectorizer:
    def __init__(self,word_getter):
        self.word_getter=word_getter

    def vectorize(self, path_to_json):
        file=open(path_to_json,"r") 
        data=json.load(file)

        text=data["text"]
        keywords=data["keywords"]


        words=self.word_getter.get(text)

        results={}
        

        for word in words:
            if word in keywords:
                results[word]=[1]
            else:
                results[word]=[0]

        return results