
class Evaluator:
    def __init__(self,weights):
        self.weights=weights

    def eval(self,y,results):
        result_matrix=[[0,0],[0,0]]
        for real,predicted in zip(y,results):
            real=int(real)
            predicted=int(predicted)
            result_matrix[real][predicted]+=self.weights[real]

        print(result_matrix[0])
        print(result_matrix[1])

        accuracy=(result_matrix[0][0]+result_matrix[1][1])/sum([sum(row) for row in result_matrix])
        print("accuracy: ", accuracy)

        precision=result_matrix[1][1]/(result_matrix[1][1]+result_matrix[0][1])
        print("precision: ", precision)

        recall=result_matrix[1][1]/(result_matrix[1][1]+result_matrix[1][0])
        print("recall: ", recall)

        f1=2*(precision*recall)/(precision+recall)
        print("f1: ", f1)