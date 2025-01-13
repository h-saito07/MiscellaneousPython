# ライブラリをインポート
import os
import shutil
from cryptography.fernet import Fernet

# クラスファイルをインポート
from Encryption import Encryption


# 生徒の情報に関する処理をまとめるクラス
class Pfile:

    # 生徒の情報の読み取り
    def road_status(path):

        count=0
        global status_kinds
        status_kinds=["名前","生徒番号","生年月日","その他情報"]
        print("\n\n＜生徒情報＞\n")
        
        
        for i in status_kinds:
            count+=1
            index_path=path+"/"+i+".txt"

            if count==len(status_kinds):
                print(count,".",i,"▽",sep="")

            else:
                print(count,".",i,"：",end="",sep="")

            try:
                    
                with open(index_path,"rb") as file:
                    read_states_byte=file.read()

                read_states=read_states_byte.decode()
                dec_states=Encryption.dec(read_states)
                print(dec_states,end="")


            except:
                pass

            print("\n")

    # 生徒の情報の編集
    def edit_status(path,student_name):

        global status_kinds
        status_kinds=["名前","生徒番号","生年月日","その他情報"]
        
        while True:

            count=0
            print("\n\n＞どの情報を編集しますか？\n")

            for i in status_kinds:
                count+=1
                index_path=path+"/"+i+".txt"

                if count==len(status_kinds):
                    print(count,".",i,"▽",sep="")

                else:
                    print(count,".",i,"：",end="",sep="")

                try:

                    with open(index_path,"rb") as file:
                        read_states_byte=file.read()

                    read_states=read_states_byte.decode()
                    dec_states=Encryption.dec(read_states)
                    print(dec_states,end="")

                except:
                    pass

                print("\n")

            print("{}.終了\n".format(len(status_kinds)+1))

            # 編集個所の選択
            edit_select=int(input(" >> "))

            if edit_select==len(status_kinds)+1:
                break

            elif edit_select>=1 and edit_select<=len(status_kinds):

                with open(path+"/"+status_kinds[edit_select-1]+".txt","wb") as file:

                    if edit_select==len(status_kinds):
                        print(status_kinds[edit_select-1],"▽",sep="")

                    else:
                        print(status_kinds[edit_select-1],"：",end="",sep="")
                    
                    # 編集内容の保存
                    write_states=input()
                    En=Encryption(write_states)
                    enc_states=En.enc(write_states)
                    enc_states_byte=enc_states.encode()
                    file.write(enc_states_byte)

                print("\n編集が完了しました")
    
    # 生徒の削除
    def delete_student(path):

        shutil.rmtree(path)