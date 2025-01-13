# ライブラリをインポート
import sys

# クラスファイルをインポート
from Sdir import Ssum
from Ppro import Ppro


# 生徒に関しての処理をまとめるクラス
class Spro:

    def __init__(self,path):

        self.path=path

    # 生徒一覧の表示
    def student_list(self):

        student_list=Ssum.acquisition_dir(self.path)
        print("\n＜生徒一覧＞")

        for i in range(len(student_list)):
            print(student_list[i],sep="")

        print("\n合計生徒数：{}人".format(Ssum.student_sum(self.path)))

    # 生徒の選択
    def student_select(self):

        student_list=Ssum.acquisition_dir(self.path)
        print("\n＜生徒選択＞")
        count=0

        for i in range(len(student_list)):
            print(i+1,".",student_list[i],sep="")
            count+=1

        print("{}.+生徒を追加".format(count+1))

        while True:

            try:
                select=int(input(" >> "))

                if select<len(student_list)+1:
                    self.path=self.path+"/"+student_list[select-1]
                    global student_name
                    student_name=student_list[select-1]
                    return student_list[select-1]

                elif select==len(student_list)+1:
                    return "00"

            except:
                pass

    # 生徒の追加
    def new_student_dir(self):
        
        print("\n新しく生徒を追加します。\n生徒の名前を入力してください")
        global student_name
        student_name=input(" >> ")
        
        try:
            Ssum.make_dir(self.path,student_name)
            print("\n登録が完了しました。")
            self.path=self.path+"/"+student_name
            return student_name

        except FileExistsError:
            print("\nすでに登録済みです。")
            self.path=self.path+"/"+student_name


    # 生徒の情報管理をするクラスを呼び出す
    def call_ppro(self):

        ppro=Ppro(self.path,student_name)
        ppro.call_status()