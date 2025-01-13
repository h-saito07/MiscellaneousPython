# ライブラリをインポート
from cryptography.fernet import Fernet

# クラスのパスワードを暗号化する鍵を生成する
key=Fernet.generate_key()

with open("../deep/class_key.key","wb") as file:
    file.write(key)