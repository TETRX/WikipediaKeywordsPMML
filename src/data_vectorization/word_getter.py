import nltk

class WordGetter:
    def __init__(self,filters):
        self.filters=filters

    
    def get(self,text):
        tokenized_text = nltk.sent_tokenize(text)
        words=[]
        for sentence in tokenized_text:
            words+=nltk.word_tokenize(sentence)

        for filter in self.filters:
            words=filter(words)


        return words