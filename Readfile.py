import codecs
import pandas as pd
import numpy as np
import re
import unidecode

#todo doc file va phan tach data, label
def readfile():
    sourcepath = r"C:\Users\locco\PycharmProjects\SentimentAnalysis\SA2016\train.crash.txt"
    with codecs.open(sourcepath, 'r', encoding='utf-8') as f:
        li = f.readlines()

    label = list()
    n = 0
    id_list = list()
    indexid = list()
    indexxuoc = list()
    indexlabel = list()
    index = -1
    data = list()
    temp = ""
    #cac thao tac ben trong deu khong anh huong den index cua li
    for row in li:
        index = index + 1
        if (row == '\n'):
            indexxuoc.append(index)
        row = re.sub(r'\n', '', row)
        id = r'train_+[0-9]+'
        match = re.findall(id, row)
        if match:
            # print(match)
            indexid.append(index)
            id_list.append(''.join(match))
        if (row.isnumeric()):
            label.append(int(row))
            indexlabel.append(index)
    data = list()
    temp = ""
    for i in range (0, li.__len__()):
        if i in indexid:
            a = i + 1
            tmp = ""
            while True:
                tmp = tmp + li[a]
                a = a + 1
                if a in indexlabel:
                    break
            # tmp = re.sub(r'\n', '. ', tmp)
            data.append(tmp)

    df = pd.DataFrame(list(zip(id_list, data, label)), columns= ['ID',
                                                'Comments', 'Label'])

    # print(df)
    # df.to_csv("Data.csv", header = 0, index=None, encoding= "utf-8")
    return label, id_list, indexxuoc, indexid, df, data

def SentimentFile():
    sourcepath = r"C:\Users\locco\PycharmProjects\SentimentAnalysis\SA2016\VietSentiWordnet_ver1.0.txt"
    with codecs.open(sourcepath, 'r', encoding='utf-8') as f:
      li = f.readlines()
    dataraw = li[22:]
    data = list()
    neg = list()
    pos = list()
    for row in dataraw:
        row = row.split('\t')
        score = row[2:4]
        word = row[4]
        word = word.split('#')
        word = word[0]
        if (float(score[0]) > float(score[1]) and float(score[0])>= 0.5):
            pos.append(word)
        elif (float(score[1]) > float(score[0]) and float(score[1]) >= 0.5):
            neg.append(word)

    not_dict = [r"không", r"chẳng", r"nỏ", r"not", r"đâu", r"vô", r"chưa"]
    return pos, neg, not_dict

# pos, neg, not_dict = SentimentFile()
# string1 = r"hấp dẫn, chất lượng đảm bảo, nỏ không cái này không hấp dẫn, nỏ chất lượng chưa tốt, không tệ, chất lượng"
# string1 = ViTokenizer.tokenize(string1)
# string1 = string1.split(" ")

def neg_pos(string1, not_dict, neg, pos):
    count_not = 0
    count_neg = 0
    count_pos = 0
    newstring = list()
    for i in range(0, len(string1)):
        # print(string1[i])
        if string1[i] in not_dict:
            before = i + 1
            count_not = count_not + 1
            if before >= len(string1):
                newstring.append(string1[i])
            elif string1[before] in pos:
                # print(string1[i] + " " + string1[before])
                newstring.append(r"not_pos")
            elif string1[before] in neg:
                # print(string1[i] + " " +  string1[before])
                newstring.append(r"not_neg")
            else:
                newstring.append(string1[i])
        elif string1[i] in neg:
            count_neg = count_neg + 1
            after = i - 1
            if after == -1:
                newstring.append("negative")
            elif string1[after] in not_dict:
                continue
            else:
                newstring.append("negative")
        elif string1[i] in pos:
            count_pos = count_pos + 1
            after = i - 1
            if after == -1:
                newstring.append("positive")
            elif string1[after] in not_dict:
                continue
            else:
                newstring.append("postive")
        else:
            newstring.append(string1[i])
    smallfeature = [count_not, count_neg, count_pos]
    return newstring, smallfeature
# with open('pos.txt', 'w', encoding="utf-8") as f:
#      for word in pos:
#         f.write("%s\n" % word)
# a1 = li[0]
# a1 = a1.split('\t')
# print(a1)

# label, id_list, indexxuoc, indexid, df, data = readfile()
# print(review.__len__())
# print(id_list.__len__())
# print(indexid)
# lis = list()
# for i in range (0, indexid.__len__()):
#     lis.append(li[indexxuoc[i]])



