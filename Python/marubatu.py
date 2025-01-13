
import random

print("ＯＸゲームを始めます")

def hyou():
    print("   ーーーーーー ")
    print("  ｜{}｜{}｜{}｜".format(marubatu[1],marubatu[2],marubatu[3]))
    print("   ーーーーーー ")
    print("  ｜{}｜{}｜{}｜".format(marubatu[4],marubatu[5],marubatu[6]))
    print("   ーーーーーー ")
    print("  ｜{}｜{}｜{}｜".format(marubatu[7],marubatu[8],marubatu[9]))
    print("   ーーーーーー ")

gameflog="1"

while gameflog=="1":
    marubatu={1:"１",2:"２",3:"３",4:"４",5:"５",6:"６",7:"７",8:"８",9:"９"}
    gamemode=input("ゲームモードを選択してください\n1.CPUとの対戦     2.二人で対戦\n >> ")
    jun=random.randint(0,1)
    if gamemode=="1":
        print("あなたはＯです")
        hyou()
        flog=0
        for i in range(9):
            if i%2==jun:
                if i==0:
                    print("先行はあなたです")
                while flog==0:
                    player=int(input("どこにする？ >> "))
                    if marubatu[player]!="Ｏ" and marubatu[player]!="Ｘ":
                        marubatu[player]="Ｏ"
                        flog=1
                    else:
                        print("そこにはすでに{}が置かれています".format(marubatu[player]))
                if (marubatu[1]=="Ｏ" and marubatu[2]=="Ｏ" and marubatu[3] =="Ｏ") or (marubatu[4]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[6] =="Ｏ") or (marubatu[7]=="Ｏ" and marubatu[8]=="Ｏ" and marubatu[9] =="Ｏ") or (marubatu[1]=="Ｏ" and marubatu[4]=="Ｏ" and marubatu[7] =="Ｏ") or (marubatu[2]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[8] =="Ｏ") or (marubatu[3]=="Ｏ" and marubatu[6]=="Ｏ" and marubatu[9] =="Ｏ") or (marubatu[1]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[9] =="Ｏ") or (marubatu[3]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[7] =="Ｏ"):
                    hyou()
                    print("Ｏが3つ揃いました\nあなたの勝ちです")
                    break
                flog=0
            else:
                if i==0:
                    print("先行はCPUです")
                while flog==0:
                    if marubatu[5]=="５":
                        marubatu[5]="Ｘ"
                        flog=1
                        hyou()
                    else:
                        num=random.randint(1,10)
                        if num>=3:
                            player=random.randrange(1,9,2)
                            if marubatu[player]!="Ｏ" and marubatu[player]!="Ｘ":
                                marubatu[player]="Ｘ"
                                flog=1
                                hyou()
                        else:
                            player=random.randrange(2,8,2)
                            if marubatu[player]!="Ｏ" and marubatu[player]!="Ｘ":
                                marubatu[player]="Ｘ"
                                flog=1
                                hyou()
                if (marubatu[1]=="Ｘ" and marubatu[2]=="Ｘ" and marubatu[3] =="Ｘ") or (marubatu[4]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[6] =="Ｘ") or (marubatu[7]=="Ｘ" and marubatu[8]=="Ｘ" and marubatu[9] =="Ｘ") or (marubatu[1]=="Ｘ" and marubatu[4]=="Ｘ" and marubatu[7] =="Ｘ") or (marubatu[2]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[8] =="Ｘ") or (marubatu[3]=="Ｘ" and marubatu[6]=="Ｘ" and marubatu[9] =="Ｘ") or (marubatu[1]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[9] =="Ｘ") or (marubatu[3]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[7] =="Ｘ"):
                    print("Ｘが3つ揃いました\nあなたの負けです")
                    break
                flog=0
        if flog==0:
            hyou()
            print("引き分けです")
    elif gamemode=="2":
        flog=0
        for i in range(9):
            hyou()
            if i%2==jun:
                if i==0:
                    print("先行はplayer1です")
                while flog==0:
                    player=int(input("player1はどこにする？ >> "))
                    if marubatu[player]!="Ｏ" and marubatu[player]!="Ｘ":
                        marubatu[player]="Ｏ"
                        flog=1
                    else:
                        print("そこにはすでに{}が置かれています".format(marubatu[player]))
                if (marubatu[1]=="Ｏ" and marubatu[2]=="Ｏ" and marubatu[3] =="Ｏ") or (marubatu[4]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[6] =="Ｏ") or (marubatu[7]=="Ｏ" and marubatu[8]=="Ｏ" and marubatu[9] =="Ｏ") or (marubatu[1]=="Ｏ" and marubatu[4]=="Ｏ" and marubatu[7] =="Ｏ") or (marubatu[2]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[8] =="Ｏ") or (marubatu[3]=="Ｏ" and marubatu[6]=="Ｏ" and marubatu[9] =="Ｏ") or (marubatu[1]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[9] =="Ｏ") or (marubatu[3]=="Ｏ" and marubatu[5]=="Ｏ" and marubatu[7] =="Ｏ"):
                    hyou()
                    print("Ｏが3つ揃いました\nplayer1の勝ちです")
                    break
                flog=0
            else:
                if i==0:
                    print("先行はplayer2です")
                while flog==0:
                    player=int(input("player2はどこにする？ >> "))
                    if marubatu[player]!="Ｏ" and marubatu[player]!="Ｘ":
                        marubatu[player]="Ｘ"
                        flog=1
                    else:
                        print("そこにはすでに{}が置かれています".format(marubatu[player]))
                if (marubatu[1]=="Ｘ" and marubatu[2]=="Ｘ" and marubatu[3] =="Ｘ") or (marubatu[4]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[6] =="Ｘ") or (marubatu[7]=="Ｘ" and marubatu[8]=="Ｘ" and marubatu[9] =="Ｘ") or (marubatu[1]=="Ｘ" and marubatu[4]=="Ｘ" and marubatu[7] =="Ｘ") or (marubatu[2]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[8] =="Ｘ") or (marubatu[3]=="Ｘ" and marubatu[6]=="Ｘ" and marubatu[9] =="Ｘ") or (marubatu[1]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[9] =="Ｘ") or (marubatu[3]=="Ｘ" and marubatu[5]=="Ｘ" and marubatu[7] =="Ｘ"):
                    hyou()
                    print("Ｘが3つ揃いました\nplayer2の勝ちです")
                    break
                flog=0
        if flog==0:
            hyou()
            print("引き分けです")
    gameflog=input("\n続けますか\n1.はい     2.いいえ\n >> ")






