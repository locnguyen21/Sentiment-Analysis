from nltk.tokenize import word_tokenize
from Preprocessing import *
from gensim.models.fasttext import FastText
from gensim.test.utils import get_tmpfile
import numpy as np

# label, id_list, indexxuoc, indexid, df, data = readfile()
# new_review, uni_new_review = Preprocessing(data)
#
# reviews = list()
# for review in new_review:
#     review = word_tokenize(review)
#     reviews.append(review)
#)

#todo build Fasttext model and return sentences representation
def BuildFastText(reviews, label):
    #input: sentences da dc tokenize thanh list
    model = FastText(size = 200, window=3, min_count = 4)
    model.build_vocab(sentences=reviews)
    model.train(sentences=reviews, total_examples= len(reviews), epochs= 50)
    # fname = get_tmpfile("Model/fasttext.model")
    model.save("Model/fasttext.bin")
    print("Save model done!")
    a = 0
    b = 0
    dataf = list()
    for review in reviews:
    # print(a)
        len_sen = len(review)
    # print(type(len_sen))
        try:
            vectors = model.wv[review]
        # print(type(vectors))
            sumvec = 0
            for i in range(0, len_sen):
                sumvec = sumvec + vectors[i]
            sumvec = sumvec / len_sen
        # print(type(sumvec))
        # print(sumvec)
            dataf.append(sumvec)
        except:
            sumvec = 0
        # print(a)
        # print(review)
            b = b + 1
            if(label[a] == 0):
                sumvec = model.wv["positive"]
                print(type(sumvec))
            if(label[a] == 1):
                sumvec = model.wv["negative"]
            print(type(sumvec))
            dataf.append(sumvec)
        # print(sumvec)
        # print(type(sumvec))
    # print(len(vectors))
    # if (len(vectors) == 0):
    #     print(a)
    # a = a + 1
    #5953 #6253 #11001 #11801 #12051 #13937 #14005

    dataf = np.array(dataf)
    return dataf
