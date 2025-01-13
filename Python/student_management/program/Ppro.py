# クラスファイルをインポート
from Pfile import Pfile


# 生徒の情報管理をするクラス
class Ppro:

    def __init__(self,path,student_name):

        self.path=path
        self.student_name=student_name

    # 生徒情報の操作全般
    def call_status(self):

        while True:

            print("\n{}を開いています。何をしますか？".format(self.student_name))
            print("1.生徒情報の表示 2.生徒情報を編集 3.生徒を削除 4.生徒選択に戻る")
            status_select=input(" >> ")

            try:

                # 生徒情報の表示
                if status_select=="1" or status_select=="１":
                    Pfile.road_status(self.path)

                # 生徒情報の編集
                elif status_select=="2" or status_select=="２":
                    Pfile.edit_status(self.path,self.student_name)

                # 生徒を削除
                elif status_select=="3" or status_select=="３":
                    print("\n本当によろしいですか？(削除したデータは戻せません)")
                    print("1を入力で続行。")
                    delete_select=input(" >> ")

                    if delete_select=="1" or delete_select=="１":
                        Pfile.delete_student(self.path)
                        print("\n生徒を削除しました。")
                        break

                # 生徒選択に戻る
                elif status_select=="4" or status_select=="４":
                        break

            except:
                pass