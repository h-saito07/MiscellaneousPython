# ライブラリをインポート
import sys

# クラスファイルをインポート
from Cpro import Cpro


# クラス一覧表示
select_class=Cpro.road_class()

# クラスを選択するか、新しく作るかを受け取る
# クラスの選択
if select_class!="00":

    # ログインの結果を受け取り、表示する
    judg=Cpro.call_comparison_pass()
    # ログイン成功
    if judg==True:
        print("\nログインに成功しました。")
    # ログイン失敗
    else:
        print("\nログインに失敗しました。")
        print("パスワードまたはクラスが間違っている可能性があります。")
        sys.exit()

# クラス作成
else:
    select_class=Cpro.new_class_dir()
    if select_class!="00":
        print("\n登録が完了しました。")

# ログイン
Cpro.call_spro()