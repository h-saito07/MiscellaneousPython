# ライブラリをインポート
import sys
from cryptography.fernet import Fernet

# クラスファイルをインポート
from Comparison import Comparison
from Cdir import Cdir
from Spro import Spro


# クラスに関しての処理をまとめるクラス
class Cpro:

    # クラスの読み込みと選択する関数
    def road_class():

        print("\n＜クラスの選択＞")
        class_list=Cdir.acquisition_dir()
        class_list.append("+クラスの追加")

        # クラスを順に表示する
        for i in range(len(class_list)):
            print(i+1,".",class_list[i],sep="")
        
        # クラスを選択するか、新しく作るかを選択させる
        while True:

            try:
                select=int(input(" >> "))
                
                # クラス選択
                if select<len(class_list):
                    global path
                    path="../class/"+class_list[select-1]
                    global class_name
                    class_name=class_list[select-1]
                    break
                
                # クラス作成
                elif select==len(class_list):
                    return "00"

            except:
                pass
            

    # 新しいクラスのフォルダを作成
    def new_class_dir():

        print("\n新しくクラスを追加します。\nあなたのクラスを入力してください。")
        global class_name
        class_name=input(" >> ")
        global path
        path="../class/"+class_name

        try:
            Cdir.make_dir(path,class_name)
            return class_name

        except FileExistsError:
            print("すでに登録済みです。")
            sys.exit()


    # パスワードの確認
    def call_comparison_pass():

        judg=Comparison.comparison_pass(class_name)

        # 合っている場合
        if judg==True:
            return True

        # 間違っている場合
        if judg==False:
            return False

    # クラスの操作全般
    def call_spro():

        while True:

            spro=Spro(path)
            print("\n{}を開いています。何をしますか？".format(class_name))
            print("1.生徒一覧 2.生徒の選択 3.パスワード変更 4.クラスの削除 5.終了")
            select=input(" >> ")

            # 生徒一覧
            if select=="1" or select=="１":
                spro.student_list()

            # 生徒の選択
            elif select=="2" or select=="２":

                if spro.student_select()=="00":
                    spro.new_student_dir()
                spro.call_ppro()

            # パスワードの変更
            elif select=="3" or select=="３":
                print("\n新しいパスワードを入力してください。")
                password=input(" >> ")

                with open("./deep/class_key.key","rb") as file:
                    class_key=file.read()

                fernet=Fernet(class_key)
                password_byte=password.encode()
                password_enc=fernet.encrypt(password_byte)

                with open("./deep/"+class_name+"_pass.csv","wb") as file:
                    file.write(password_enc)
                print("\nパスワードを変更しました。")

            # クラスの削除
            elif select=="4" or select=="４":

                print("\n本当によろしいですか？(削除したデータは戻せません)")
                print("1を入力で続行。")
                delete_select_class=input(" >> ")

                if delete_select_class=="1" or delete_select_class=="１":
                    Cdir.delete_class(path,class_name)
                    print("\nクラスを削除しました。")
                    break

            # 終了
            elif select=="5" or select=="５":
                break