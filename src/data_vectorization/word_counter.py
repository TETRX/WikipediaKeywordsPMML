from collections import Counter
from typing import Set

class WordCounter:
    def __init__(self,word_getter):
        self.word_occurence_counter=Counter()
        self.word_doc_counter=Counter()
        self.all_word_counter=0
        self.all_doc_counter=0
        self.word_getter=word_getter

    def count_words_in(self,text):
        self.all_doc_counter+=1
        words=self.word_getter.get(text)
        self.all_word_counter+=len(words)
        occured=set()
        for word in words:
            if not word in occured:
                occured.add(word)
                self.word_doc_counter[word]+=1
            self.word_occurence_counter[word]+=1
        