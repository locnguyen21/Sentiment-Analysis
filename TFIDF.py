from sklearn.feature_extraction.text import TfidfVectorizer
from Preprocessing import *
from Readfile import *
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC
import time
import pickle
import datetime
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
# from TestSVM import *
# from Evaluate import *

# review = newpos_review + newneg_review
#todo representation data to vector with TFIDF
def Tfidf(new_review):
    length = new_review.__len__()
    print(length)
    tfidf_vectorizer = TfidfVectorizer(min_df = 5,max_df = 0.5,use_idf=True,ngram_range=(1,2),sublinear_tf=True)
    tfidf_vectorizer_vectors = tfidf_vectorizer.fit(new_review)

    vectors = tfidf_vectorizer_vectors.transform(new_review)
    print(vectors)
    features_name = tfidf_vectorizer.get_feature_names()
    # print(features_name)
    vectordata = vectors.todense()
    print(vectordata.shape)
    df = pd.DataFrame(vectordata, columns= features_name)
    print(features_name)
    print(df)
    print(df.shape)
    pickle.dump(tfidf_vectorizer_vectors, open("Model/tfidf.pickle", "wb"))
    pickle.dump(vectors, open("Model/tfidftrain_features.pickle", "wb"))
    # pos = 0
    # neg = 1
    # half = newpos_review.__len__()
    # poslabel = [0] * half
    # print(poslabel)
    #
    # neglabel = [1] * half
    # label = poslabel + neglabel

    # print(label.__len__())
    # print(df.head(10))

    return vectordata

# label, id_list, indexxuoc, indexid, df, data = readfile()
# new_review, uni_new_review = Preprocessing(data)
# new_review = new_review + uni_new_review
# vectordata = Tfidf(new_review)

# vectordata = Tfidf(new_review)
# df["Label"] = label
#print(df)
# first_vector_tfidfvectorizer = features[0]

# print(first_vector_tfidfvectorizer.T.todense())
# df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
# df = df.sort_values(by=["tfidf"], ascending=False)
# print(df.head(10))
#
# string_new = ["Cái điện thoại này dùng rất thích, pin trâu và nhanh"]
# vector = tfidf_vectorizer_vectors.transform(string_new)
# df = pd.DataFrame(vector.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
# df = df.sort_values(by=["tfidf"], ascending=False)
# print(df.head(10))
# with open('TF_IDF_Features.txt', 'w', encoding="utf-8") as f:
#     for item in features_name:
#         f.write("%s\n" % item)

# a = ["dùng rất ổn, cảm ơn shop", "khá xịn ủng hộ shop dài dài", "cho cửa hàng mình 5 sao, chất lượng", "dở ẹc", "dùng rất tệ", "pin không tốt"]
#

#data_test
# id_list1, indexxuoc1, indexid1, data1 = readTestfile()
# test_review, test_uni_new_review = Preprocessing(data1)
# test_vectors = tfidf_vectorizer_vectors.transform(test_review)
# b = test_vectors.todense()
# print(b.shape)
# df = pd.DataFrame(b, columns= features_name)

# count = -1
# result = clf.predict(df)
# with open('result.txt', 'w', encoding="utf-8") as f:
#      for item in result:
#           count = count + 1
#           f.write("%d: %s\n" % (count,item))