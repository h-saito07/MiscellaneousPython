# ライブラリをインポート
from cryptography.fernet import Fernet
import csv


# パスワードの確認をするクラス
class Comparison:

    # パスワードの確認
    def comparison_pass(class_name):

        print("\nパスワードを入力してください。")
        password=input(" >> ")

        with open("./deep/class_key.key","rb") as file:
            class_key=file.read()

        fernet=Fernet(class_key)

        with open("./deep/"+class_name+"_pass.csv","rb") as file:
            read_password_byte=file.read()

        read_password=fernet.decrypt(read_password_byte)
        read_password_dec=read_password.decode()

        if password==read_password_dec:
            return True

        else:
            return False    