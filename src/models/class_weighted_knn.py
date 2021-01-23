import heapq
from operator import ne
import numpy
from numpy.core.fromnumeric import argmax
from numpy.linalg import norm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.base import BaseEstimator

class CWKNN(KNeighborsClassifier):
    def __init__(self, class_weights={0:1,1:1}, algorithm='brute',n_neighbors=10, p=2):
        super().__init__(algorithm=algorithm, n_neighbors=n_neighbors, p=p)
        self.class_weights=class_weights

    def fit(self,X,Y):
        self.Y=Y
        return super().fit(X,Y)

    def predict(self, X):
        neighbors=self.kneighbors(X, return_distance=False)
        predicted=[]
        for ns in neighbors:
            votes=[0.0,0.0]
            for n in ns:
                vote=int(self.Y[n])
                votes[vote]+=self.class_weights[vote]
            predicted.append(argmax(votes))
        return numpy.array(predicted)