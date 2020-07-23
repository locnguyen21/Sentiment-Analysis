# from Preprocessing import *
# from Readfile import *
# from nltk.tokenize import word_tokenize
from Ftext import *
from RNN import *
from SVM import *
from TFIDF import *
#from Doc2vec import *
import pickle
import numpy as np
# from Test_RNN_Fasttext import *
from gensim.models.fasttext import FastText
#from tensorflow import keras
#import tensorflow as tf
#import gensim.models as g
#from keras.models import model_from_json,load_model
# from keras.utils import CustomObjectScope
# from keras.initializers import glorot_unifo
# from sklearn.preprocessing import StandardScaler


# label, id_list, indexxuoc, indexid, df, data = readfile()
# new_review, uni_new_review= Preprocessing(data)
# # # # # with open('data.txt', 'w', encoding="utf-8") as f:
# # # # #     for item in new_review:
# # # # #         f.write("%s\n" % item)
# new_review = new_review + uni_new_review
# label = label + label

# feature_name = custom.columns
# custom = custom.values
# custom = custom.tolist() + custom.tolist()
# custom = pd.DataFrame(custom, columns= feature_name)
#todo word_token for fasttext
#Fasttext and RNN model

# reviews = list()
# for review in new_review:
#     review = word_tokenize(review)
#     reviews.append(review)
# dataf = BuildFastText(reviews, label)
# RNNmodel(dataf, label)


# #TFIDF and SVM model
# vectordata = Tfidf(new_review)
# # # # # # # data = pd.concat([tframe, custom], axis=1)
# # # # # # # # # print(new_review[17244])
# # # # # # # vectordata = StandardScaler().fit_transform(data.values)
# SVM(vectordata, label)

# todo Doc2Vec and RNN model
# vectordata  = Doc2vec(new_review)
# RNNmodel(vectordata, label)

# print('read file:')
data_new = ["Tệ. Giày sứt chỉ hộp rách. Thời gian giao hàng rất chậm",
            "Chất lượng sản phẩm rất kém !!!Toàn bị sờn chỉ !!! Không đúng với mô tả của sản phẩm !!!",
            "Hàng lỗi. Sạc hỏng. Lm ăn quá chán Rất không đáng tiền Rất không đáng tiền",
            "Sản phẩm gội rất là cứng tóc.mùi thơm như kiểu hoá chất. Chất lượng sản phẩm rất kém.",
            "cực không ổn 🙁🙁🙁, chất lượng kém",
            "không tốt như kỳ vọng",
            'hàng không tốt',
            "Kém chất lượng",
            'hàng dởm',
            'Hàng tốt. Đóng gói sp kỹ. Nhân viên tư vấn nên có thái độ dễ chịu hơn',
            "ổn",
            "rất ổn",
            "chất lượng kém, pin hết nhanh",
            "Ốp nào cũng đẹp hết thích cực luônnnnn",
            "Hàng rất tốt",
            "bực mình, chán",
            "Shop phục vụ quá tệ. Mua pho mai sợi mà bán pho mai lát. Lát pho mai có mùi và móp méo",
            "Đã nhận đc 1 cái. Thanks shop chất lượng sản phẩm tuyệt vời Đóng gói sản phẩm rất đẹp và chắc chắn Shop phục vụ rất tốt",
            "Sản phẩm không biết có tốt hay không ?vì muốn đánh giá phải có thời gian kiểm tra  đã kiểm tra chất lượng như con cac",
            "Hàng nhái ọp à ọp ẹp",
            "Lấy size từ 12/14 kg mà mặc ko vừa .chât lượng thì ok nhưng mặc chật", #1
            "ưng cực kỳ.",
            "Hàng quá chán mấy bộ bé zai khác với hình shop đăng bán không  có bộ nào mình chọn giống như lúc đặt"]
# data_label = np.array([1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1, 1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1])
# data, unidata = Preprocessing(data_new)
# data = data + unidata

def SVM_Tfidf(data):
    tfidf_model = pickle.load(open("C://Users//locco//PycharmProjects//SentimentAnalysis//Model//tfidf.pickle", "rb"))
    vector = tfidf_model.transform(data)
    vectordata = vector.todense()
    # vectordata = StandardScaler().fit_transform(vectordata)
    # print(vectordata.shape)
    clf = pickle.load(open("C://Users//locco//PycharmProjects//SentimentAnalysis//Model//SVM_model.sav", "rb"))
    result = clf.predict(vectordata)
    return result

# result = SVM_Tfidf(data)
# # # result = RNN_Fasttext(data)
# print(result)
# print("Kết quả: ")
# for i in range(0, len(result)):
#     if (result[i] != data_label[i]):
#         print(data[i])
#         print(result[i])
# Evaluate_Model(result, data_label)


# result = RNN_Fasttext(data)
# print(result)
# Evaluate_Model(result, data_label)
#todo doc2vec
# doc2vecfile="Model/doc2vec_model.bin"  #point to downloaded pre-trained doc2vec model
# #load model
# m = g.Doc2Vec.load(doc2vecfile)
# token = "chất lượng kém, pin hết nhanh"
# vector = m.infer_vector(word_tokenize(token))
# print(vector)
# token = list()
# for i in data_new:
#     vector2 = word_tokenize(i)
#     token.append(vector2)
# vectors = m.infer_vector([token[0]])
# print(vector)
# print(len(vector))
# print(vector2)
#
# print(type(vector))
# test = np.reshape(vector,(1,len(vector),1))
# print(test.shape)
# print(type(load_model1))
# labels_test = load_model1.predict(test)
# # print(reviews[2])
# a = labels_test.tolist()
# if(a[0][0] <0.5):
#     print(0)
# if(a[0][0] >= 0.5):
#     print(1)


# # if (a[0] >= 0.5):
#     print(1)
# if (a[0] < 0.5):
#     print(0)


# labels = []
# for i in labels_test:
#     if (i >= 0.5):
#         a = 1
#         labels.append(a)
#     else:
#         a = 0
#         labels.append(a)
# labels = np.asarray(labels)
# # print(type(labels))
# print(labels)
