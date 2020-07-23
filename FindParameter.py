from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC, LinearSVC
import time
import pickle
import datetime
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from TestSVM import *
from Evaluate import *
from sklearn.model_selection import GridSearchCV
from Preprocessing import *
from Readfile import *
from TFIDF import *
label, id_list, indexxuoc, indexid, df, data = readfile()
new_review, uni_new_review = Preprocessing(data)
vectordata, dframe = Tfidf(new_review)

X_train, X_test, y_train, y_test = train_test_split(vectordata, label, test_size=0.33, random_state=42)

param_grid = {'C': [0.1, 1, 3, 5, 10, 100]}
grid = GridSearchCV(LinearSVC(), param_grid, cv=5, refit=True, verbose=3)

# fitting the model for grid search
grid.fit(X_train, y_train)
print(grid.best_params_)

# print how our model looks after hyper-parameter tuning
print(grid.best_estimator_)
grid_predictions = grid.predict(X_test)
print(classification_report(y_test, grid_predictions))