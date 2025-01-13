# ライブラリをインポート
import os
import shutil
import csv

# クラスファイルをインポート
from cryptography.fernet import Fernet


# クラスのフォルダに関するクラス
class Cdir:

    # クラスのフォルダの一覧を返す
    def acquisition_dir():

        return os.listdir("../class/")

    # クラスのフォルダの作成
    def make_dir(path,class_name):

        os.mkdir(path)

        # パスワードの設定
        print("\nパスワードを設定してください。")
        password=input(" >> ")

        with open("./deep/class_key.key","rb") as file:
            class_key=file.read()

        fernet=Fernet(class_key)
        password_byte=password.encode()
        password_enc=fernet.encrypt(password_byte)

        with open("./deep/"+class_name+"_pass.csv","wb") as file:
            file.write(password_enc)

    # クラスの削除
    def delete_class(path,class_name):

        os.remove("./deep/"+class_name+"_pass.csv")
        shutil.rmtree(path)