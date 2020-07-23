from sklearn.model_selection import train_test_split
from Preprocessing import *
import tensorflow
#from keras.models import model_from_json
import time
import datetime
import numpy as np
from Evaluate import *
#todo train RNN model and testing model
def RNNmodel(dataf, label):
    X_train, X_test, y_train, y_test = train_test_split(dataf, label, test_size=0.33, random_state=42)

    # clf = LinearSVC(fit_intercept = True,multi_class='crammer_singer', C=1, dual=False)
    # clf.fit(X_train, y_train)
    # y_pred = clf.predict(X_test)
    # result = accuracy_score(y_test, y_pred)
    # print(result)

    # print(doc2vecdata.values)
    print(type(X_train))
    X_train = np.array(X_train)
    sample = X_train.shape[0]
    feature = X_train.shape[1]

    # convert 2D to 3D for input RNN
    new_train = np.reshape(X_train, (sample, feature, 1))  # shape (10778, 120, 1)
    opt = tensorflow.keras.optimizers.Adam(learning_rate= 0.01)
    Model = tensorflow.keras.Sequential([
        # tensorflow.keras.layers.Dense(150, input_dim=(new_train.shape[1],)),
        # tensorflow.keras.layers.LSTM(200, input_shape=(feature, new_train.shape[2]),
        #                              return_sequences=True),
        tensorflow.keras.layers.LSTM(100,input_shape=(feature, new_train.shape[2]),activation='tanh', return_sequences=True),
        tensorflow.keras.layers.Dropout(0.5),
        tensorflow.keras.layers.LSTM(50, activation = 'tanh'),
        tensorflow.keras.layers.Dense(1, activation='sigmoid')
    ])
    # Model.compile(optimizer= opt , loss = tensorflow.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])
    Model.compile(optimizer= tensorflow.keras.optimizers.Adam(), loss=tensorflow.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])
    print('begin training')
    start = time.time()
    print(datetime.datetime.utcnow())

    Model.fit(new_train, np.array(y_train), epochs=50, batch_size=32)
    print('training done at')
    end = time.time()
    print(end - start)
    print('save model to JSON file')
    # serialize model to JSON
    model_json = Model.to_json()
    with open("C://Users//locco//PycharmProjects//SentimentAnalysis//Model//RNN_model_ftext.json", "w") as json_file:
        json_file.write(model_json)

    Model.save_weights("C://Users//locco//PycharmProjects//SentimentAnalysis//Model//RNN_model_ftext.h5")
    print("Saved model to disk")
    Model.summary()

    X_test = np.array(X_test)
    new_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    score_keras = Model.evaluate(new_test, np.array(y_test), batch_size=32)
    label = Model.predict(new_test, batch_size=32)
    labels = []
    for i in label:
        if (i >= 0.5):
            a = 1
            labels.append(a)
        else:
            a = 0
            labels.append(a)
    labels = np.asarray(labels)
    Evaluate_Model(labels.tolist(), y_test)
    print(score_keras)

