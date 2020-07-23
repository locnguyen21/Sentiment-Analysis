from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC, LinearSVC
import time
import pickle
import datetime
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from TestSVM import *
from Evaluate import *

#todo train SVM model and testing

def SVM(data, label):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.33, random_state=42)
    print(X_train.shape)
    # clf = SVC(C=5, kernel='rbf')
    clf = LinearSVC(C=5, class_weight=None, dual=True, fit_intercept=True, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', random_state=None)
    print('done dataload')
    start = time.time()
    print(datetime.datetime.utcnow())
    # scores = cross_val_score(clf, X_train, y_train, cv = 5)
    # print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    print('begin training')
    clf.fit(X_train, y_train)
    end = time.time()
    print(end - start)
    print(datetime.datetime.utcnow())
    model = 'Model/SVM_model.sav'
    pickle.dump(clf, open(model, 'wb'))
    print('save model done')

    y_pred = clf.predict(X_test)
    result = accuracy_score(y_test, y_pred)
    print("Accuracy - test set: %.2f%%" % (result*100.0))
    print(classification_report(y_test, y_pred))
    print(type(y_pred))
    print(type(y_test))

    Evaluate_Model(y_pred.tolist(), y_test)

    # print(type(y_pred[1]))
    # print(type(y_test[1]))
