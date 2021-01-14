import json

class InPartsVectorizer:
    def __init__(self,word_getter):
        self.word_getter=word_getter

    def vectorize(self, path_to_json):
        file=open(path_to_json,"r") 
        data=json.load(file)

        text=data["text"]
        summary=data["summary"]
        title=data["title"]
        section_titles=data["section titles"]

        parts=[summary,title,section_titles]

        words=self.word_getter.get(text)

        results={}
        for word in words:
            results[word]=[0,0,0]

        for i in range(len(parts)):
            part_words=self.word_getter.get(parts[i])
            for word in part_words:
                if word in results:
                    results[word][i]=1

        return results