#this should filter out all punctuation marks
import string


class PunctiuationFilter():
    def __call__(self, words):
        return [word for word in words if not word in string.punctuation]