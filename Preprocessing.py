import codecs
import re
import unidecode
import string
from Readfile import *
from underthesea import *
#todo
# 1. Đưa về viết thường không viết hoa
# 2. Loại bỏ khoảng trắng
# 3. Loại bỏ số
# 4. Loại bỏ ký tự đặc biệt
# 5. Loại bỏ email
# 6. Loại bỏ stop words
# 7. Loại bỏ NAN
# 8. Loại bỏ weblinks
# 9. Expand contractions (if possible not necessary)
# 10. Tokenize tiếng việt
# 11. Loại bỏ các câu giống nhau.

def Filetolist(sourcepath):
    with codecs.open(sourcepath, 'r', encoding='utf-8') as f:
        li = f.readlines()

    review = list()
    for row in li:
        if (row != "\n"):
            review.append(row)
    return review

stopword2 = ["bị", "bởi", "cả", "các", "cái", "cần", "càng", "chỉ", "chiếc", "cho",
            "chứ", "chưa", "chuyện", "có", "có thể", "cứ", "của", "cùng", "cũng",
            "đã", "đang", "đây", "để", "đến_nỗi", "đều", "điều", "do", "đó",
            "được", "dưới", "gì", "không", "khi", "là", "lại", "lên", "lúc", "mà",
            "mỗi", "một_cách", "này", "nên", "nếu", "ngay", "nhiều", "như", "nhưng",
            "những", "nơi", "nơi", "nữa", "phải", "qua", "ra", "rằng", "rất", "rồi",
            "sau", "sẽ", "so", "sự", "tại", "theo", "thì", "trên", "trước", "từ",
            "từng", "và", "vẫn", "vào", "vậy", "vì", "việc", "với", "vừa"]

stopword = ["rằng", "thì", "là", "mà"]
punctuation = ['!', '"', '#', '$', '%', '&',"'", '(', ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '~', '`', '{', '|', '}']

# stopword_puctuation = stopword + punctuation
#print(stopword_puctuation)

#todo Loại bỏ ngày tháng, email, url
def RelgularExpression(sentence):
    datetime = '\d{1,2}\s?[:/-]\s?\d{1,2}\s?[:/-]\s?\d{4}' \
               '|\d{1,2}\s?[:/-]\s?\d{4}' \
               '|\d{1,2}\s?[:/-]\s?\d{1,2}' \
               '|\d{4}' \
               '/(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d/'\


    email = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+'
    url = 'https?:\/\/[^\s]*'
    url2 = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    num_punctuation = 0
    punctuation1 = r'[!#"$%&()*+,-./:;<=>?@[\]^_`{|}~]'
    punctuation2 = r"[']"
    # cam_than = r'([^a-zA-Z])\1+'
    #cam_than = r'(\D)\1+'
    re_datetime = re.compile(datetime)
    re_email = re.compile(email)
    re_url = re.compile(url)
    re_punc = re.compile(punctuation1)
    match_punc = re.findall(punctuation1, sentence)
    if match_punc:
        num_punctuation = len(match_punc)
    match_punc2 = re.findall(punctuation2,sentence)
    if match_punc2:
        num_punctuation = num_punctuation + len(match_punc2)
    # new_row = list()
    # for row in frame:
    # matchdatetime = re.findall(datetime, sentence)
    # match_email = re.findall(email, sentence)
    # match_url1 = re.findall(url, sentence)
    # match_camthan = re.findall(cam_than, sentence)
    #     #match_url2 = re.findall(url2, row)
    # if matchdatetime:
    #     print(matchdatetime)
    #
    # if match_email:
    #     print(match_email)
    #
    # if match_url1:
    #     print(match_url1)
    #     # if match_url2:
    #     #     print(match_url2)
    #
    #
    # if match_camthan:
    #     print(match_camthan)

    sentence = re.sub(re_datetime,r' date ', sentence)
    sentence = re.sub(re_email, r' email ', sentence)
    sentence = re.sub(re_url,r' url ', sentence)
    #sentence = re.sub(r'[^\w\s]','    ',sentence)
    sentence = re.sub(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', r' ', sentence)
    # sentence = re.sub(r'["]', r' ', sentence)
    sentence = re.sub(r"[']", r' ', sentence)
    # sentence = re.sub(r'([A-z])\1+', r'\1', sentence)
    # sentence = ' '.join(sentence.split())
    # loại bỏ các kí tự space thừa, các từ cảm thán dài như ngonnnnnnnn -> ngon, hayyy -> hay
    # sentence = re.sub(r'(\D)\1+', r'\1', sentence)
    # sentence = re.sub(re_camthan,' ', sentence)
        # new_row.append(row)
    return sentence, num_punctuation

#todo Loại bỏ stopword
def RemovePunc(sentence):
    vn_char_low = r"ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđð"
    vn_char_up = r"ẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸÐĐ"
    non_special_char = re.compile(
        r"[^A-Za-z0-9 ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđðẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸÐĐ]+")

    punctuation = re.compile(r"[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]")
    return re.sub(non_special_char, ' ', sentence)

    # sentence = sentence.split()
    # # print(sentence)
    # new_sentence = []
    # for word in sentence:
    #     if word not in punctuation:
    #         new_sentence.append(word)
    # return ' '.join(new_sentence)

# new_frame = RelgularExpression(review)
# daugach = re.compile(r"[_]")
# tên = r"dấu_gạch"
# a = re.sub(daugach, ' ', tên)
# print("đã xong")
# print(review)
# new_frame2 = RelgularExpression(new_frame)

# print(new_frame2)
# r = u' \xa0\n'
# a = re.sub(r,"",review[0])
# print(a)
# # print(review)
# # print(review[0])
# # print(review[1])
# b = re.sub(r,"",review[1])
# print(b)
# newlist = [a,b]
# print(newlist)
# def RegularExpression()

# word = r"    Đông thì rấtttt   đẹp trai  nên là xinh gái he    he   "
# word1 = r"Đang xài MX1. Dùnggggggg bình thườnnng ngon, pinnnnn trâu"
# word2 = r"Mỗi tội   thằng cùng dùng mà ngồi một chỗ thì cà giựt cà tang"
# # .strip()
# a = (re.sub(r'(\D)\1+', r'\1', word1))
# print(a)

emoji = {
    '❤': ' positive ', '😘': ' positive ', '😋': ' positive ', '😆': ' positive ' , '😡': ' negative ', '♥': ' positive ', '😁': ' positive ',
    '💋' : ' positive ', '🎉' : ' positive ', '💯' : ' positive ', '👍🏻' : ' positive ', '😍' : ' positive ',
    '🌺': ' positive ', '😗': ' positive ', '💚' : ' positive ', '💕': ' positive ',
    '😊': ' positive ', '😭': ' negative ', '👎': ' negative ', '🙄': ' positive ', '👌🏻': ' positive ', ':<': ' negative ', '👶': ' positive ',
    '☺': ' positive ', '😓': ' negative ', '😂': ' positive ', '👍': ' positive ', '✨': ' positive ',  '😝': ' positive ',
    '🙁': ' negative ', '😠': ' negative ', '🤣': ' positive ', '😳': ' negative ', '😢': ' negative ', '😄': ' positive ', '😅': ' positive ', '😌': ' positive ',
    '😤': ' negative ', '⭐': ' positive ', '☹' : ' negative ','😑': ' negative ', '😣': ' negative ', '👏': ' positive ', '😈': ' negative ', '😀': ' positive ', '😉': ' positive ',
    '🖒': ' positive ', '👌': ' positive ', '😞': ' negative ', '💪🏻': ' positive ', '😩': ' positive ', '💓': ' positive ', '😥':' negative ',
    '💟': ' positive ', '💙': ' positive ', '😒': ' negative ',  '🌟': ' positive ', '😶': ' negative ', '🤗': ' positive ',
    '😯': ' negative ', '🤔': ' negative ', '✌': ' positive', '😏': ' negative ', '😎': ' positive ', '😜': ' positive ', '🤑':' positive ', '😚': ' positive ',
    '🤨': ' negative ',  '😬': ' negative ', '😟': ' negative ', '😫': ' negative ', '😻': ' positive ', '😇': ' positive ', '😛': ' positive ',
    '🤤': ' positive ', '😔': ' negative ', '😐': ' negative ' , '😪': ' negative ', '😧': ' negative ', '😱': ' negative ', '😰':' nagative ', '🤭': ' positive ',
    '😖': ' negative ', '🙏': ' positive ', '🚫': ' positive ',  '❤️': ' positive ', '🤝': ' positive ', ":'>": ' positive ', '🌷': ' positive ',
    '=))' : ' positive ', ':))' : ' positive ', ':(' : ' negative ', ':)': ' positive ', '∩_∩': ' positive ', '^^': ' positive ', ':|': ' negative ', '^=^': ' positive ',
    '(๑>◡<๑)': ' positive ', 'ㄟ(￣▽￣ㄟ)': ' positive ', ':3': ' positive ', ':v': ' positive ', ':((': ' negative ', '=}}': ' positive ', 'T^T': ' negative ', '<3': ' positive ',
    '^_^' : ' positive ', '1 sao': ' negative ', '1*': ' negative ', '2 sao': ' negative ', '2sao': ' negative ', '2*': ' negative ', '3 sao': ' positive ', '3*': ' positive ', '3sao': ' positive ',
    '4 sao': ' positive ', '4*': ' positive ', '4sao' : ' positive ', '5 sao': ' positive ', '5*': ' positive ', '💮': ' positive ', '😃': ' positive ', '💐': ' positive ',
    'vcl': ' negative ', 'he he': ' positive ','hehe': ' positive ','hihi': ' positive ', 'haha': ' positive ', 'hjhj': ' positive ', '🆗': ' positive ', '💖': ' positive ',
    ' lol ': ' negative ',' cc ': ' negative ','huhu': ' negative ', 't^t': ' negative ', '💗': ' positive ', '😙': ' positive ', '🙂': ' negative ',
    '💛': ' positive ', '💞': ' positive ', '-.-': ' negative ', 'okê': ' ok ', '🌸': ' positive  ', '❣':  ' positive ', '🤪': ' positive ', '🤙🏻': ' positive ', '♡': ' positive ',
    '5sao': ' positive ', '1sao': ' negative '
}

#vị trí dấu thanh ở việt nam chỉ tồn tại không nhất trí với các tổ hợp oa, oe, ua, ue, uy chẳng hạn như
# Họa, hòe, hủy, qủa, qủe, quý, hoạ, hoè, quả, quẻ, quý... thì phải điều chỉnh về đúng dấu
# họa
vitridauthanh = {
    'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè', 'óe': 'oé','ỏe': 'oẻ',
    'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý', 'ủy': 'uỷ', 'ũy': 'uỹ','ụy': 'uỵ', 'ủa': 'uả'
}
rightword = {
    ' kb ': ' không ', 'sp': ' sản phẩm ', 'ship': ' vận chuyển ', 'đc': ' được ', 'dc': ' được ', 'dx': ' được ',
    'shop': ' cửa hàng ', 'tks': ' cảm ơn ', 'thank': ' cảm ơn ', 'thanks': ' cảm ơn ', 'tl': ' trả lời ',
    'rep': ' trả lời ', 'delivery': ' vận chuyển ', 'poor ': ' kém ', 'product ': ' sản phẩm ', 'quality': ' chất lượng ',
    'hk': ' không ', 'wá': ' quá ', 'đt': ' điện thoại ', 'kq': ' kết quả ', 'mk': ' mình ', 'check': ' kiểm tra ',
    'update': ' cập nhật ', 'mn': ' mọi người ', 'feedback': ' phản hổi ', 'wa': ' quá ', 'app': ' ứng dụng ',
    'mik': ' mình ', 'ntn': ' như thế này ', 'size': ' kích cỡ ', ' j ': ' gì ', ' ji ': ' gì ', 'đk': ' được ',
    'authentic': ' chính hãng ', 'auth': ' chính hãng', 'fake': ' giả mạo ', 'pack': ' đóng gói ', 'packing': ' đóng gói ', 'order': ' đặt hàng ',
    'chất lg': ' chất lượng ', 'okie': ' ok ', 'oke': ' ok ', 'oki': ' ok ', ' m ': ' mình ', 'sd': ' sử dụng ', 'fb ': ' facebook ',
    'ib': ' nhắn tin ', 'time': ' thời gian ', 'dt': ' điện thoại ',
    'đt ': ' điện thoại ', 'thik': ' thích ', 'mjh': ' mình ', 'okey': ' ok ', 'sz ': ' kích cỡ ', ' very ': ' rất ', 'hsd': ' hạn sử dụng ', 'qá': ' quá ',
    'bt': ' bình thường ', 'money': ' tiền ', 'value': ' giá trị ', 'fast': ' nhanh ', 'excelent': ' tốt ',
    ' k ': ' không ',' kh ':' không ', 'kô':' không ', 'hok':' không ',' kp ': ' không phải ',' kô ': ' không ', 'ko': ' không ',
    'khong': ' không ', ' hok ': ' không ', 'inbox': ' nhắn tin ',
}

correctmapping = {**emoji, **rightword}

# string = r"SẢN PHẨMhttp://tnews.vn/index.php?threads/43/Review giới thiệu :Giới thiệu kèm bị bởi cả Lộc  cái   cần   càng <  =, >, ?, @"
# print(string.isalpha())
# url = 'https?:\/\/[^\s]*'
# match_url1 = re.findall(url, string)
# if match_url1:
#     print(match_url1)
# string1 = "Đông thì rất đẹp trai nên là hấp dẫn he he"
# # print(string1.lower())
# a = ViTokenizer.tokenize(string1)
# print(a)
# a = RelgularExpression(string)
# a = RemoveStopword(a)
# for row in a.split():
#     if row.isalpha() is False:
#         print(row)

# print(review)

#todo tìm emoji trong data
def NonCharacter(data):
    notcharacter = '[^A-Za-z0-9 ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđðẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸÐĐ".,]+'
    for row in data:
        match = re.findall(notcharacter, row)
        if match:
            print(match)

#
# NonCharacter(data)
# count = 0
# a = list()
# for row in data:
#     tmp = list()
#     for i in row:
#         if i in correctmapping:
#             tmp.append(correctmapping[i])
#             # count = count + 1
#     a.append(tmp)
# print(count)

# with open('emoji.txt', 'w', encoding="utf-8") as f:
#     for item in a:
#         f.write("%s\n" % item)

# string1 = "Uống rất ngon Giao hàng nhanh Chất lượng sản phẩm tuyệt vời ....................😋😋😋😋......................"

# print(a)
# print(a)

# string1 = string1.strip().split()
# for i in string1:
#     print(i)
#     if i in correctmapping:
#         print(i)

# string1 = underthesea.word_tokenize(string1)
# print(string1)

#todo thay thế các emoji và các từ viết tắt
def ReplaceWithCorrectmapping(row):
    keys = correctmapping.keys()
    for i in keys:
        if i in row:
            # print(i)
            row = row.replace(i, correctmapping[i])
    return row

#todo thay thế các vị trí dấu thanh đặc biệt
def ReplaceDauThanh(row):
    keys = vitridauthanh.keys()
    for i in keys:
        if i in row:
            # print(i)
            row = row.replace(i, vitridauthanh[i])
    return row

#todo dem emoji positive and negative
def PosNegCount(data):
    pos = "positive"
    neg = "negative"
    num_positive = 0
    num_negative = 0

    matchpos = re.findall(pos, data)
    matchneg = re.findall(neg, data)
    if matchpos:
        num_positive = matchpos.__len__()

    if matchneg:
        num_negative = matchneg.__len__()

    return num_positive, num_negative

#todo xử lý data với các function
def Preprocessing(frame):
    pos, neg, not_dict = SentimentFile()
    new_review = list()
    uni_new_review = list()
    # daugach = re.compile(r"[_]")
    a = 0
    # customfeature = list()
    # customfeature = pd.DataFrame(columns=['count_not', 'count_neg', 'count_pos', 'num_words', 'num_punc' , 'emo_positive', 'emo_negative'])
    for row in frame:
        row = row.lower()
        row = ReplaceWithCorrectmapping(row) # kp lỗi từ đây
        row = ReplaceDauThanh(row) #kp lỗi từ đây
        row, numpunc = RelgularExpression(row) #kp lỗi từ đây
        #row = RemovePunc(row) #RemovePunc có vấn đề
        row = re.sub(r'(\D)\1+', r'\1', row)
        row = re.sub(r'\xa0', r' ', row)
        row = re.sub(r'\n', r' ', row)
        row = row.strip()
        row = row.split()
        row1 = list()
        for word in row:
            if (word.isdigit() == False):
                row1.append(word)
        row = ' '.join(row1)
        # row = ' '.join(row.split())
        # row = re.sub(daugach, ' ', row)

        reviewfinal = []
        #tokenize
        review = list()
        review1 = word_tokenize(row)
        for i in review1:
            i_ = "_".join(i.split())
            review.append(i_)
        # review = (ViTokenizer.tokenize(row)).split(" ")
        # num_words = len(review)
        review, smallfeature = neg_pos(review, not_dict, neg, pos)
        # print(review)
        #remove stopword
        for word in review:
            if word not in stopword:
                if (("_" in word) or (word.isalpha() == True)):
                    reviewfinal.append(word)

        # smallfeature.append(num_words)
        # smallfeature.append(numpunc)
        review1 = ' '.join(reviewfinal)
        new_review.append(review1)
        # num_positive, num_negative = PosNegCount(review1)
        # smallfeature.append(num_positive)
        # smallfeature.append(num_negative)
        #data ko dau
        unirow = unidecode.unidecode(' '.join(reviewfinal))
        uni_new_review.append(unirow)
        a = a + 1
        # print(smallfeature)
        # customfeature.append(smallfeature)
    # with open('data.txt', 'w', encoding="utf-8") as f:
    #     for item in new_review:
    #         f.write("%s\n" % item)
        # custom = pd.DataFrame(customfeature,
        #                       columns=['count_not', 'count_neg', 'count_pos', 'num_words', 'num_punc', 'emo_positive',
        #                                'emo_negative']) # print(type(smallfeature))

    return new_review, uni_new_review


# # print(data[347])
# data,unicodedata = Preprocessing(data)
# datafinal = data + unicodedata
# labelfinal = label + label

# with open('data_final.txt', 'w', encoding="utf-8") as f:
#      for item in data:
#           f.write("%s\n" % item)
