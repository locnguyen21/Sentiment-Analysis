from sklearn.naive_bayes import MultinomialNB
from Preprocessing import *
from Readfile import *
from TFIDF import *
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
from Evaluate import *
# label, id_list, indexxuoc, indexid, df, data = readfile()
# new_review, uni_new_review= Preprocessing(data)
# new_review = new_review + uni_new_review
# label = label + label

def Naive(data, label):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.33, random_state=42)
    clf = MultinomialNB()
    print(X_train.shape)
    scores = cross_val_score(clf, X_train, y_train, cv = 5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
# y_pred = clf.predict(X_test)
# print(classification_report(y_test, y_pred))
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
    model = 'Model/NaiveB.sav'
    pickle.dump(clf, open(model, 'wb'))
    print('save model done')

    y_pred = clf.predict(X_test)
    result = accuracy_score(y_test, y_pred)
    print("Accuracy - test set: %.2f%%" % (result * 100.0))
    print(classification_report(y_test, y_pred))
    print(type(y_pred))
    print(type(y_test))
    Evaluate_Model(y_pred.tolist(), y_test)

# vectordata = Tfidf(new_review)
# Naive(vectordata,label)

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
# data_label = np.array([1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,    1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1])
# data, unidata = Preprocessing(data_new)
# data = data + unidata
def Naive_TFidf(data):

    tfidf_model = pickle.load(open("C://Users//locco//PycharmProjects//SentimentAnalysis//Model//tfidf.pickle", "rb"))
    vector = tfidf_model.transform(data)
    vectordata = vector.todense()
    clf = pickle.load(open("C://Users//locco//PycharmProjects//SentimentAnalysis//Model//NaiveB.sav", "rb"))
    result = clf.predict(vectordata)
    return result

# result = Naive_TFidf(data)
# print(result)
#
# for i in range(0, len(result)):
#     if (result[i] != data_label[i]):
#         print(i)
#         print(data[i])
#         print(result[i])
# Evaluate_Model(result, data_label)