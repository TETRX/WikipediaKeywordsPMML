from sklearn.utils import class_weight
from ..model_testing.data_processing.data_divider import DataDivider
from ..model_testing.data_processing.data_reader import DataReader

from sklearn import tree

from ..model_testing.model_evaluating.result_evaluator import Evaluator

import graphviz

data_reader=DataReader("data/vectors.data")
dataset=data_reader.read()

data_divider=DataDivider()

training, testing=data_divider.divide([8,1],dataset)
weigth={0: 1217/(1217+54064),1: 54064/(1217+54064)}
clf = tree.DecisionTreeClassifier( max_depth=2)
X,Y=training.get_X_y()

clf.fit(X,Y)

# training_res=clf.predict(X)

# print(training_res)
# evall=Evaluator()
# evall.eval(Y,training_res,weigth)

# X_t, Y_t= testing.get_X_y()

# testing_res=clf.predict(X_t)
# evall.eval(Y_t,testing_res,weigth)

dot_data=dot_data = tree.export_graphviz(clf, out_file=None, filled=True, rounded=True,special_characters=True,feature_names=["doc%","word%","first occ", "noun", "verb", "foreign", "adjective", "cardinal digit", "summary", "title", "section title"]) 
graph=graphviz.Source(dot_data)
graph.render("test_tree_diagram.gv",directory="results/")