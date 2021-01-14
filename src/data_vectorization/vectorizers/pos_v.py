import json
import nltk
from nltk.tag import pos_tag

class POSVectorizer:
    def __init__(self,word_getter):
        self.word_getter=word_getter

    def vectorize(self,path_to_json):
        file=open(path_to_json,"r") 
        text=json.load(file)["text"]
        tokenized_sentences = nltk.sent_tokenize(text)
        tokenized_words= [nltk.word_tokenize(sent) for sent in tokenized_sentences]
        pos_tagged_text= nltk.pos_tag_sents(tokenized_words)

        words=self.word_getter.get(text)

        tags={}

        for sentence in pos_tagged_text:
            for tagged_word in sentence:
                if tagged_word[0] not in tags.keys():
                    tags[tagged_word[0]]=[]
                tags[tagged_word[0]].append(tagged_word[1])


        result={}      
        for word in words:
            result[word]=[0,0,0,0,0] #Noun, Verb, Foreign Word, adjective, cardinal digit

        for word, tag_list in tags.items():
            if word not in result.keys():
                continue
            for tag in tag_list:

                if tag.startswith("N"):
                    result[word][0]=1
                elif tag.startswith("V"):
                    result[word][1]=1
                elif tag=="FW":
                    result[word][2]=1
                elif tag.startswith("RB"):
                    result[word][3]=1
                elif tag=="CD":
                    result[word][4]=1
        return result

        
