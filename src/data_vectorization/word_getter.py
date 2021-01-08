import nltk

class WordGetter:
    def __init__(self,filters):
        self.filters=filters

    def normalize_words(self,words):
        return [word.lower() for word in words]
    
    def get(self,text):
        tokenized_text = nltk.sent_tokenize(text)
        words=[]
        for sentence in tokenized_text:
            words+=nltk.word_tokenize(sentence)

        words = self.normalize_words(words)

        for filter in self.filters:
            words=filter(words)


        return words