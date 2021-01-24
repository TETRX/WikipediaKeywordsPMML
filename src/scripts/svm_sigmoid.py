from random import shuffle

from ..model_testing.data_processing.dataset import Dataset
from ..model_testing.data_processing.data_divider import DataDivider
from ..model_testing.data_processing.data_reader import DataReader
from ..metadata import *

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.svm import SVC
from ..model_testing.model_evaluating.graph_data_getter import GraphDataGetter
from ..model_testing.model_evaluating.result_evaluator import Evaluator

from sklearn.preprocessing import MinMaxScaler, StandardScaler

from ..config import *

weight={0: KEYWORDS/TOTAL,1: NON_KEYWORDS/TOTAL}


from datetime import datetime

print("Start: ",datetime.now())
clf=GridSearchCV(estimator=SVC(class_weight=weight),
param_grid={"kernel":['sigmoid'], "C":[0.1,1.0,100.0], "gamma": ["scale",1.0,0.1]}, 
scoring="balanced_accuracy" ,n_jobs=-1, cv=StratifiedKFold(10,shuffle=True), verbose=4)


data_reader=DataReader("data/vectors.data")
dataset=data_reader.read()
divider=DataDivider()

X,Y=dataset.get_X_y()
min_max_scaler=MinMaxScaler()
X=min_max_scaler.fit_transform(X)
dataset=Dataset([x.tolist()+[y] for x,y in zip(X,Y)])
clf.fit(X,Y)
print("Validation: ",datetime.now())

params=clf.best_params_
print(clf.best_score_)
print(params)

clf2=SVC(class_weight=weight,**params)

divider=DataDivider()
divisions=[divider.divide([9,1],dataset) for _ in range(10)]

evaluator=Evaluator(weight)
graph_getter=GraphDataGetter(evaluator,divider)

graph_getter.get_data(clf2,divisions,FRACTIONS)

print("End: ",datetime.now())