from Preprocessing import *
from Readfile import *
import underthesea
from nltk.tokenize import word_tokenize
from Ftext import *
from RNN import *
from SVM import *
from TFIDF import *
from Doc2vec import *
import pickle
import numpy as np
from gensim.models.fasttext import FastText
from tensorflow import keras
import tensorflow as tf
import gensim.models as g
from keras.models import model_from_json,load_model



# label, id_list, indexxuoc, indexid, df, data = readfile()
# new_review, uni_new_review= Preprocessing(data)
# new_review = new_review + uni_new_review
# label = label + label
# #
# # # todo Doc2Vec and RNN model
# vectordata  = Doc2vec(new_review)
# RNNmodel(vectordata, label)

data_new = ["Tệ. Giày sứt chỉ hộp rách. Thời gian giao hàng rất chậm",
            "Chất lượng sản phẩm rất kém !!!Toàn bị sờn chỉ !!! Không đúng với mô tả của sản phẩm !!!",
            "Hàng lỗi. Sạc hỏng. Lm ăn quá chán Rất không đáng tiền Rất không đáng tiền",
            "Sản phẩm gội rất là cứng tóc.mùi thơm như kiểu hoá chất. Chất lượng sản phẩm rất kém.",
            "cực không ổn 🙁🙁🙁, chất lượng kém",
            "không tốt như kỳ vọng",
            'hàng dởm',
            'hàng không tốt',
            "Kém chất lượng",
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
data_label = np.array([1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1, 1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1])
data, unidata = Preprocessing(data_new)
data = data + unidata

doc2vecfile="Model/doc2vec_model.bin"  #point to downloaded pre-trained doc2vec model
#load model
m = g.Doc2Vec.load(doc2vecfile)

json_file = open('Model/RNN_model_doc2vec.json','r')
loaded_model_json = json_file.read()
json_file.close()
load_model1 = tf.keras.models.model_from_json(loaded_model_json)
# # # with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
# # #     model = load_model('imdb_mlp_model.h5')
# # #load weights vào model
load_model1.load_weights('Model/RNN_model_doc2vec.h5')

token = list()
for i in data:
    vector2 = word_tokenize(i)
    token.append(m.infer_vector(vector2))
token = np.array(token)
print(token.shape)
dataf = np.reshape(token, (token.shape[0], token.shape[1], 1))
result = load_model1.predict(dataf)
print(type(result))
labels = []
for i in result:
    if (i >= 0.5):
        a = 1
        labels.append(a)
    else:
        a = 0
        labels.append(a)
labels = np.asarray(labels)
Evaluate_Model(labels.tolist(), data_label)

for i in range(0, len(labels)):
    if (labels[i] != data_label[i]):
        print(data[i])
        print(labels[i])