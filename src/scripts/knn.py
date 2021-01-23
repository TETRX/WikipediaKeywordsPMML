from ..model_testing.data_processing.data_divider import DataDivider
from ..model_testing.data_processing.data_reader import DataReader
from ..model_testing.data_processing.dataset import Dataset
from ..metadata import *

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier 

from ..model_testing.model_evaluating.graph_data_getter import GraphDataGetter
from ..model_testing.model_evaluating.result_evaluator import Evaluator

from ..config import *

from imblearn.under_sampling import RandomUnderSampler

from sklearn.preprocessing import MinMaxScaler

weight={0: KEYWORDS/TOTAL,1: NON_KEYWORDS/TOTAL}

clf=GridSearchCV(estimator=KNeighborsClassifier(algorithm='brute', weights='distance'),
param_grid={"n_neighbors": [10,13,15,17,20], "p": [1,2,3]}, 
scoring="balanced_accuracy" ,n_jobs=-1, cv=StratifiedKFold(50,shuffle=True), verbose=0)


data_reader=DataReader("data/vectors.data")
dataset=data_reader.read()

X,Y=dataset.get_X_y()
min_max_scaler=MinMaxScaler()
X=min_max_scaler.fit_transform(X)

undersampler=RandomUnderSampler(sampling_strategy=1.0)

X_sampled, Y_sampled=undersampler.fit_resample(X,Y)
clf.fit(X_sampled, Y_sampled)

params=clf.best_params_
print(params)

clf2=KNeighborsClassifier(**params,weights='distance')

divider=DataDivider()
list=[x+[y] for x,y in zip(X.tolist(),Y)]
dataset=Dataset(list)
_,Y_test=dataset.get_X_y()
divisions=[divider.divide([9,1],dataset) for _ in range(50)]
divisions2=[]
for train,test in divisions:
    X_temp,Y_temp =train.get_X_y()
    X_temp, Y_temp=undersampler.fit_sample(X_temp,Y_temp)
    sampled_dataset=Dataset([x+[y] for x,y in zip(X_temp,Y_temp)])
    divisions2.append((sampled_dataset,test))

divisions=divisions2
evaluator=Evaluator(weight)
graph_getter=GraphDataGetter(evaluator,divider)

graph_getter.get_data(clf2,divisions,FRACTIONS)