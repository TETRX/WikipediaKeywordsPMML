

class GraphDataGetter():
    def __init__(self,evaluator,divider):
        self.evaluator=evaluator
        self.divider=divider

    def get_data(self, clf, divisions, fractions):
        for fraction in fractions:
            print("Dataset fraction: ", fraction)
            total_real=[]
            total_predicted=[]
            for train, test in divisions:
                train=self.divider.get_first([fraction,1-fraction],train)
                X_1,Y_1=train.get_X_y()
                clf.fit(X_1,Y_1)
                X_2,Y_2=test.get_X_y()
                total_predicted+=clf.predict(X_2).tolist()
                total_real+=Y_2
            self.evaluator.eval(total_real,total_predicted)
            print("---------------")