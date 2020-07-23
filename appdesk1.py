import tkinter as tk
from Preprocessing import *
import time
from Testing import *
from NaiveB import *
from Test_RNN_Fasttext import *

class SentimentGUI:
    def __init__(self, main):
        self.main = main
        main.title("Sentiment Analysis App")

        self.nhap_label = tk.Label(main, text="Nhập câu bình luận:")
        self.nhap_label.grid(row=0, column=0, columnspan=2)

        self.giaithich_label = tk.Label(main, text="Tích cực: 0   Tiêu cực: 1")
        self.giaithich_label.grid(row=1, column=0, columnspan=2)

        self.text = tk.Text(main, height=10, width=50)
        self.text.grid(row=2, column=0, columnspan=2)

        self.SVM_label = tk.Label(main, text="Kết quả từ SVM:")
        self.SVM_label.grid(row=3, column=0)

        self.Naive_label = tk.Label(main, text="Kết quả từ Naive Bayes:")
        self.Naive_label.grid(row=4, column=0)

        self.RNN_label = tk.Label(main, text="Kết quả từ RNN:")
        self.RNN_label.grid(row=5, column=0)

        self.Entry_ResultSVM = tk.Entry(main, width=43)
        self.Entry_ResultSVM.grid(row=3, column=1)

        self.Entry_ResultNaive = tk.Entry(main, width=43)
        self.Entry_ResultNaive.grid(row=4, column=1)

        self.Entry_ResultRNN = tk.Entry(main, width=43)
        self.Entry_ResultRNN.grid(row=5, column=1)

        self.check_button = tk.Button(main, text='Kiểm tra', command=self.show_answer, width=10)
        self.check_button.grid(row=6, column=0, columnspan=2)

        self.clear_button = tk.Button(main, text='Xóa', command=self.cleartext, width=10, fg="red")
        self.clear_button.grid(row=7, column=0, columnspan=2)


    def show_answer(self):
        sentences = self.text.get("1.0",'end-1c').encode('utf-16', 'surrogatepass').decode('utf-16')
        # print(type(sentences))
        # sen1 = sentences.decode('utf-8')
        # print(sen1)
        data_text = sentences.split('\n')
        # print(data_text)
        data, unidata = Preprocessing(data_text)
        # print(data)
        SVM_Tfidf_labels = SVM_Tfidf(data)
        Naive_TFidf_labels = Naive_TFidf(data)
        RNN_Fasttext_labels = RNN_Fasttext(data)
        sentences1 = '\n' + str(SVM_Tfidf_labels)
        sentences2 = '\n' + str(Naive_TFidf_labels)
        sentences3 = '\n' + str(RNN_Fasttext_labels)
        # sentences = str(SVM_Tfidf_labels)
        # he = r'1234'
        self.Entry_ResultSVM.insert(tk.END, sentences1)
        self.Entry_ResultNaive.insert(tk.END, sentences2)
        self.Entry_ResultRNN.insert(tk.END, sentences3)

    def cleartext(self):
        self.text.delete('1.0', 'end-1c')
        self.Entry_ResultSVM.delete(0, tk.END)
        self.Entry_ResultNaive.delete(0, tk.END)
        self.Entry_ResultRNN.delete(0, tk.END)


def main():
    print("Initialize the program")
    print("Welcome your highness")
    main = tk.Tk()
    my_APP = SentimentGUI(main)
    main.mainloop()

if __name__ == "__main__":
    main()