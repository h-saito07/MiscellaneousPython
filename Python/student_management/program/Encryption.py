# ライブラリをインポート
from sys import argv


# 生徒情報を暗号化するクラス
class Encryption:

    def __init__(self,word):

        global words
        words=word

    #暗号化
    def enc(*args):

        word_list=list(words)
        point_list=[ord(w)+1 for w in word_list]
        enc_word_list=[chr(p) for p in point_list]
        return "".join(enc_word_list)

    #復号
    def dec(strings):

        word_list=list(strings)
        point_list=[ord(w)-1 for w in word_list]
        dec_word_list=[chr(p) for p in point_list]
        return "".join(dec_word_list)