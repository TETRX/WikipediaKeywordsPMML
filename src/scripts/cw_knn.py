from random import shuffle
from ..model_testing.data_processing.data_divider import DataDivider
from ..model_testing.data_processing.data_reader import DataReader
from ..model_testing.data_processing.dataset import Dataset
from ..metadata import *

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from ..models.class_weighted_knn import CWKNN

from ..model_testing.model_evaluating.graph_data_getter import GraphDataGetter
from ..model_testing.model_evaluating.result_evaluator import Evaluator

from sklearn.neighbors import NearestNeighbors

from sklearn.preprocessing import MinMaxScaler

from ..config import *

weight={0: KEYWORDS/TOTAL,1: NON_KEYWORDS/TOTAL}

clf=GridSearchCV(estimator=CWKNN(class_weights=weight,algorithm='brute'),
param_grid={"n_neighbors": [10,13,15,17,20], "p": [1,2,3]}, 
scoring="balanced_accuracy" ,n_jobs=1, cv=StratifiedKFold(10,shuffle=True), verbose=4)


data_reader=DataReader("data/vectors.data")
dataset=data_reader.read()

X,Y=dataset.get_X_y()
min_max_scaler=MinMaxScaler()
X=min_max_scaler.fit_transform(X)

dataset=Dataset([x.tolist()+[y] for x,y in zip(X,Y)])

clf.fit(X,Y)

params=clf.best_params_
print(clf.best_score_)
print(params)

clf2=CWKNN(class_weights=weight,algorithm='brute',**params)

divider=DataDivider()
divisions=[divider.divide([9,1],dataset) for _ in range(10)]

evaluator=Evaluator(weight)
graph_getter=GraphDataGetter(evaluator,divider)

graph_getter.get_data(clf2,divisions,FRACTIONS)