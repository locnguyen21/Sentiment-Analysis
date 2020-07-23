from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split, cross_val_score
from Readfile import *
from Preprocessing import *
from tensorflow import keras
import numpy as np
from keras.models import model_from_json
import time
import datetime
from gensim.test.utils import get_tmpfile
# label, id_list, indexxuoc, indexid, df, data = readfile()
# new_review, uni_new_review = Preprocessing(data)

#todo train model Doc2vec and return senteces representaion
def Doc2vec(new_review):
    tagged_data = [TaggedDocument(words= word_tokenize(_d),
                                  tags = [str(i)]) for i, _d in enumerate(new_review)]

    model = Doc2Vec(vector_size=120, window = 4, min_count = 5, workers = 4, epochs = 20)
    model.build_vocab(tagged_data)
    model.train(tagged_data, total_examples= model.corpus_count, epochs= model.epochs)

    #X_train, X_test, y_train, y_test = train_test_split(df, label, test_size=0.33, random_state=42)

    doc2vecdata = model.docvecs
    fname = "Model/doc2vec_model.bin"
    model.save(fname)
    # doc2vecdata = np.array(doc2vecdata)
    return doc2vecdata

# doc2vecdata = Doc2vec(new_review)
# X_train, X_test, y_train, y_test = train_test_split(doc2vecdata, label, test_size=0.33, random_state=42)
#
# # clf = LinearSVC(fit_intercept = True,multi_class='crammer_singer', C=1, dual=False)
# # clf.fit(X_train, y_train)
# # y_pred = clf.predict(X_test)
# # result = accuracy_score(y_test, y_pred)
# # print(result)
#
# # print(doc2vecdata.values)
# print(type(X_train))
# X_train = np.array(X_train)
# sample = X_train.shape[0]
# feature = X_train.shape[1]
#
# #convert 2D to 3D for input RNN
# new_train = np.reshape(X_train, (sample, feature, 1)) #shape (10778, 120, 1)
# Model = keras.Sequential([
#     keras.layers.LSTM(80, input_shape= (feature, new_train.shape[2]),
#                      activation = 'tanh', recurrent_activation = 'hard_sigmoid'),
#     keras.layers.Dense(1, activation = 'tanh')
# ])
# Model.compile(optimizer ='rmsprop', loss= 'mse', metrics = ['accuracy'])
#
# print('begin training')
# start = time.time()
# print(datetime.datetime.utcnow())
#
# Model.fit(new_train, np.array(y_train), epochs=30, batch_size= 32)
# print('training done at')
# end = time.time()
# print(end - start)
# print('save model to JSON file')
# # serialize model to JSON
# model_json = Model.to_json()
# with open("RNN_model.json", "w") as json_file:
#     json_file.write(model_json)
#
# Model.save_weights("RNN_model.h5")
# print("Saved model to disk")
# Model.summary()
#
# X_test = np.array(X_test)
# new_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
# score_keras = Model.evaluate(new_test, np.array(y_test), batch_size = 32)
# print(score_keras)