import pandas as pd

def Evaluate_Model(y_pred,y_test):

    #change pandas Dataframe to numpy array tien cho de so sanh
    machine = y_pred
    test = y_test
    a = 0

    # print(len(y_pred))
    # print(len(y_test))

    for i in range (len(machine)):
        if (machine[i] == test[i]):
            a = a + 1
    # print(a * 100 / len(machine))

    truepositive = 0
    truenagative = 0
    falsepositive = 0
    falsenagative = 0

    for i in range (len(machine)):
        #tinh true positive = 0
        if (machine[i] == test[i] and test[i] == 1):
            truepositive = truepositive + 1
        #tinh true negative = 1
        elif (machine[i] == test[i] and test[i] == 0):
            truenagative = truenagative + 1
        #tinh false positive
        elif (machine[i] != test[i] and test[i] == 0):
            falsepositive = falsepositive + 1
        else:
            falsenagative = falsepositive + 1

    print("true positive: " + str(truepositive))
    print("true negative: " + str(truenagative))
    print("false negative: " + str(falsenagative))
    print("false positive: " + str(falsepositive))
    precision = truepositive * 100 / (truepositive + falsepositive)
    recall = truepositive * 100 / (truepositive + falsenagative)
    F1_score = 2 * precision * recall / (precision + recall)

    print('Accuracy: ' + str(a * 100 / len(machine)))
    print('Precision : ' + str(precision))
    print('Recall: ' + str(recall))
    print('F1 Score with positive: ' + str(F1_score))
