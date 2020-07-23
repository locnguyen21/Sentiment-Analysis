from Preprocessing import *
from Readfile import *
from pyvi import ViTokenizer
import underthesea
from nltk.tokenize import word_tokenize
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from TFIDF import *
from SVM import *
from RNN import *
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC
import time
import pickle
import datetime
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from TestSVM import *

label, id_list, indexxuoc, indexid, df, data = readfile()
new_review, uni_new_review = Preprocessing(data)

vectordata = Tfidf(new_review)
print(vectordata[1])
new_review = StandardScaler().fit_transform(vectordata)
print(new_review[1])
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(new_review)
print(principalComponents)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['pc1', 'pc2','pc3'])
principalDf['Label'] = label
print(type(label[1]))

# X_train, X_test, y_train, y_test = train_test_split(principalComponents, label, test_size=0.33, random_state=42)
# clf = LinearSVC(fit_intercept = True,multi_class='crammer_singer', C=1, dual=False)
# model = clf.fit(X_train, y_train)

# colors = {0: 'r', 1: 'b'}
# fig, ax = plt.subplots()
# #
# for i in range(len(principalDf['pc1'])):
#     ax.scatter(principalDf['pc1'][i], principalDf['pc2'][i], principalDf['pc3'][i], color = colors[principalDf['Label'][i]])
# # RNNmodel(vectordata, label)
# ax.set_title('Toxic comment')
# ax.set_xlabel('pc1')
# ax.set_ylabel('pc2')
# plt.show()

# id_listtest, indexxuoctest, indexidtest, datatest = readTestfile()
# test_review, uni_test_review = Preprocessing(datatest)

principalDf1 = principalDf[principalDf["Label"] == 1]
principalDf2 = principalDf[principalDf["Label"] == 0]
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter(principalDf1['pc1'], principalDf1['pc2'], principalDf1['pc3'], c= 'r', marker='o')
# ax.scatter(principalDf2['pc1'], principalDf2['pc2'], principalDf2['pc3'], c= 'b', marker='x')
ax.set_xlabel('pc1')
ax.set_ylabel('pc2')
ax.set_zlabel('pc3')
plt.show()
