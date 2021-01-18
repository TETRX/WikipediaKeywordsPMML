from random import shuffle
from ..model_testing.data_processing.data_divider import DataDivider
from ..model_testing.data_processing.data_reader import DataReader
from ..metadata import *

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

from ..model_testing.model_evaluating.graph_data_getter import GraphDataGetter
from ..model_testing.model_evaluating.result_evaluator import Evaluator

from ..config import *

weight={0: KEYWORDS/TOTAL,1: NON_KEYWORDS/TOTAL}

clf=GridSearchCV(estimator=RandomForestClassifier(class_weight=weight),
param_grid={"min_samples_leaf": [0.005, 0.001, 1], "max_samples": [0.1,0.01,None]}, 
scoring="balanced_accuracy" ,n_jobs=-1, cv=StratifiedKFold(10,shuffle=True), verbose=0)

data_reader=DataReader("data/vectors.data")
dataset=data_reader.read()

X,Y=dataset.get_X_y()

clf.fit(X,Y)

params=clf.best_params_
print(params)

clf2=RandomForestClassifier(class_weight=weight,**params)

divider=DataDivider()
divisions=[divider.divide([9,1],dataset) for _ in range(10)]

evaluator=Evaluator(weight)
graph_getter=GraphDataGetter(evaluator,divider)

graph_getter.get_data(clf2,divisions,FRACTIONS)