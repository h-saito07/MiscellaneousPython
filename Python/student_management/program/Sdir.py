# ライブラリをインポート
import os


# 生徒のフォルダに関するクラス
class Sdir:

    # 生徒のフォルダの一覧を返す
    def acquisition_dir(path):

        return os.listdir(path)

    # 生徒のフォルダの作成
    def make_dir(path,student_name):

        os.mkdir(path+"/"+student_name)

# 生徒の総数を数えるクラス
class Ssum(Sdir):

    def student_sum(path):

        return len(os.listdir(path))