import random
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nブラックジャックを始めます\n")
name1=input("１人目の名前を入力してください >> ")
name2=input("２人目の名前を入力してください >> ")

toranpu=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
toranpu_ten=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
motite1_ban=[]
motite2_ban=[]
motite1_ten=[]
motite2_ten=[]
motite1=[]
motite2=[]

motite1_ban.append(random.randint(0,len(toranpu)-1))
motite2_ban.append(random.randint(0,len(toranpu)-1))

tt="Y"
ff="Y"
i=0
j=0
flog1=1
flog2=1

while (tt!="N" and tt!="No" and tt!="no" and tt!="n") or (ff!="N" and ff!="No" and ff!="no" and ff!="n"):
    
        if tt=="Yes" or tt=="yes" or tt=="Y" or tt=="y":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            input("{}さんの番です".format(name1))
            motite1_ban.append(random.randint(0,len(toranpu)-1))
            while i < len(motite1_ban):
                motite1.append(toranpu[motite1_ban[i]])
                motite1_ten.append(toranpu_ten[motite1_ban[i]])
                del toranpu[motite1_ban[i]]
                del toranpu_ten[motite1_ban[i]]
                i+=1
            print("\n持ち札は")
            for n in range(len(motite1)):
                print("[",motite1[n],"]",sep="",end="")
            tt=input("\nトランプを引きますか？ Yes or No >> ")

        elif tt!="N" and tt!="No" and tt!="no" and tt!="n":
            tt=input("Yes か No を入力してください >> ")
    

        if ff=="Y" or ff=="yes" or ff=="Y" or ff=="y":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            input("{}さんの番です".format(name2))
            motite2_ban.append(random.randint(0,len(toranpu)-1))
            while j < len(motite2_ban):
                motite2.append(toranpu[motite2_ban[j]])
                motite2_ten.append(toranpu_ten[motite2_ban[j]])
                del toranpu[motite2_ban[j]]
                del toranpu_ten[motite2_ban[j]]
                j+=1
            print("\n持ち札は")
            for m in range(len(motite2)):
                print("[",motite2[m],"]",sep="",end="")
            ff=input("\nトランプを引きますか？ Yes or No >> ")
        
        elif ff!="N" and ff!="No" and ff!="no" and ff!="n":
            ff=input("Yes か No を入力してください >> ")

else:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    tokuten1=sum(motite1_ten)
    tokuten2=sum(motite2_ten)

    brk1=""
    brk2=""

    if tokuten1>21:
        tokuten1=0
        brk1="OVER!"
    if tokuten2>21:
        tokuten2=0
        brk2="OVER!"


    print("\n{}さんの点数は{}点  {}".format(name1,sum(motite1_ten),brk1))
    print("{}さんの点数は{}点  {}".format(name2,sum(motite2_ten),brk2))


    if tokuten1>tokuten2:
        print("\nよって{}さんの勝利！".format(name1))
    elif tokuten1<tokuten2:
        print("\nよって{}さんの勝利！".format(name2))
    else:
        print("\nよって引き分け")