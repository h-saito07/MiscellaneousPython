# インポート
# 乱数用
import random as rd
# 時間を計る、待ち時間用
import time
# 計算用
import math

# 関数 keisan20 -------------------------------------------------------------------------------------------------------- #

def keisan20():

    # total:正解数
    total=0
    # gamestert:ゲーム開始用
    gamestert=0
    print("\n\n----------------------------------------")
    
    # 1が入力されるまで繰り返す
    while gamestert!="1" and gamestert!="１":
        # 始めるかルール説明を聞くかを入力させる
        gamestert=input("\n＜計算20＞\n\n1.はじめる     2.ルール説明\n >> ")
        # 2が入力されている間繰り返す
        while gamestert=="2" or gamestert=="２":
            # 解説文
            print("20問の簡単な四則演算が出題されます。")
            print("回答する場合はEnterを押してください。")
            print("正解の場合は回答の右下に「 〇 」不正解の場合は「 ✓ 」が表示されます。")
            print("速いタイムと正確な計算による高スコアを目指して頑張ってください。")
            # 入力させる
            gamestert=input("\n1.はじめる     2.もう一度聞く\n >> ")
    print("\n")

    # カウントダウン
    # 3回繰り返す
    for i in range(3):
        # 3-iを表示
        print(3-i)
        # 1秒待つ
        time.sleep(1)
    # stert!
    print("STERT!\n")

    # start:始まりの時間
    start=time.time()
    # 20問分繰り返す
    for i in range(20):
        try:
            # keihou:計算方法をランダムに決める
            keihou=rd.randint(1,4)

            # 計算方法:和
            if keihou==1:
                # 足される値をランダムに決める(1~19まで)
                rd1=rd.randint(1,19)
                # 足す値をランダムに決める(1~19まで)
                rd2=rd.randint(1,19)
                # 和を求める
                kai=rd1+rd2
                # 答えを入力させる
                ans=int(input("{} + {} = ".format(rd1,rd2)))
                # 答えが合っていた場合
                if ans==kai:
                    # 正解数+1
                    total+=1
                    # 「 〇 」を表示
                    print("            〇")
                # それ以外の場合
                else:
                    # 「 ✓ 」を表示
                    print("            ✓")

            # 計算方法:差
            elif keihou==2:
                # 引かれる値をランダムに決める(1~19まで)
                rd1=rd.randint(1,19)
                # 引く値をランダムに決める(1~引かれる値まで)
                rd2=rd.randint(1,rd1)
                # 差を求める
                kai=rd1-rd2
                # 答えを入力させる
                ans=int(input("{} - {} = ".format(rd1,rd2)))
                # 答えがあっていた場合
                if ans==kai:
                    # 正解数+1
                    total+=1
                    # 「 〇 」を表示
                    print("            〇")
                # それ以外の場合
                else:
                    # 「 ✓ 」を表示
                    print("            ✓")

            # 計算方法:積
            elif keihou==3:
                # かけられる値をランダムに決める(1~10まで)
                rd1=rd.randint(1,10)
                # かける値をランダムに決める(1~10まで)
                rd2=rd.randint(1,10)
                # 積を求める
                kai=rd1*rd2
                # 答えを入力させる
                ans=int(input("{} × {} = ".format(rd1,rd2)))
                # 答えがあっていた場合
                if ans==kai:
                    # 正解数+1
                    total+=1
                    # 「 〇 」を表示
                    print("            〇")
                # それ以外の場合
                else:
                    # 「 ✓ 」を表示
                    print("            ✓")

            # 計算方法:商
            elif keihou==4:
                # 答えとなる値をランダムに決める(2~6まで)
                waru=rd.randint(2,6)
                # 割られる値をランダムに決める(答えの3倍から30までの答えの倍数)
                rd1=rd.randrange(waru*3,30,waru)
                # 割る値を答えと割られる値から決める
                rd2=int(rd1/waru)
                # 商を求める
                kai=int(rd1/rd2)
                # 答えを入力させる
                ans=int(input("{} ÷ {} = ".format(rd1,rd2)))
                # 答えがあっていた場合
                if ans==kai:
                    # 正解数+1
                    total+=1
                    # 「 〇 」を表示
                    print("            〇")
                # それ以外の場合
                else:
                    # 「 ✓ 」を表示
                    print("            ✓")
        except:
            print("            ✓")

    # 経過時間を今の時間から始まりの時間(stert)を引いて求める
    end=time.time()-start
    # 小数点第2以下切り捨て
    endtime=math.floor(end*100)/100
    # 小数点以下を切り捨てた値を byou に格納
    byou=int(endtime)
    # 小数点以下のみを整数にした値を tenika に格納
    tenika=int((endtime-byou)*100)

    # 10000-経過した時間*100+間違えた問題数(総問題数-正解した問題数)*500をスコアとして score に格納
    score=10000-(endtime*100+(20-total)*500)
    # score が0以下の場合
    if score<0:
        # score を0にする
        score=0

    # 終了(結果発表)
    print("\n終了")
    # 1秒待つ
    time.sleep(1)
    input("結果は....")
    # 正解数とかかった時間を表示
    print("\n{}問正解  時間： {}秒{}".format(total,byou,tenika))
    # スコアを表示
    print("score {}".format(math.ceil(score)))
    input()
    print("\n----------------------------------------")
    
# 関数 koukakazoe ------------------------------------------------------------------------------------------------------ #

def koukakazoe():
    
    # gamestert:ゲーム開始用
    gamestert=0
    print("\n\n----------------------------------------")

    # 1が入力されるまで繰り返す
    while gamestert!="1" and gamestert!="１":
        # 始めるかルール説明を聞くかを入力させる
        gamestert=input("\n＜硬貨数え＞\n\n1.はじめる     2.ルール説明\n >> ")
        # 2が入力されている間繰り返す
        while gamestert=="2" or gamestert=="２":
            # 解説文
            print("お金の合計金額から、各硬貨の枚数を当てるゲームです。")
            print("「 〇 」は 1円、10円、100円 のどれかに、")
            print("「 ◎ 」は 5円、50円 のどれかに該当します。")
            print("速いタイムを目指して頑張ってください。")
            # 入力させる
            gamestert=input("\n1.はじめる     2.もう一度聞く\n >> ")

    # 初期値設定
    # more:問題変更繰り返し
    more="2"
    # flog:答え入力繰り返し
    flog=0

    # 2が入力されている間繰り返す
    while more=="2" or more=="２":
        # yen1:1円玉
        yen1=0
        # yen5:5円玉
        yen5=0
        # yen10:10円玉
        yen10=0
        # yen50:50円玉
        yen50=0
        # yen100:100円玉
        yen100=0
        print("\n")
        # 硬貨の枚数をランダムに決める(9~11枚まで)
        maisuu=rd.randint(9,11)
        # 硬貨の枚数分繰り返す
        for i in range(maisuu):
            # 硬貨の種類をランダムに決める(1~5まで)
            money=rd.randint(1,5)
            # 1のとき
            if money==1:
                # 「 〇 」を表示
                print("〇",end="")
                # 1円玉の枚数+1
                yen1+=1
            # 2のとき
            elif money==2:
                # 「 ◎ 」を表示
                print("◎",end="")
                # 5円玉の枚数+1
                yen5+=1
            # 3のとき
            elif money==3:
                # 「 〇 」を表示
                print("〇",end="")
                # 10円玉の枚数+1
                yen10+=1
            # 4のとき
            elif money==4:
                # 「 ◎ 」を表示
                print("◎",end="")
                # 50円玉の枚数+1
                yen50+=1
            # 5のとき
            elif money==5:
                # 「 〇 」を表示
                print("〇",end="")
                # 100円玉の枚数+1
                yen100+=1

        # 各硬貨の枚数から総金額を求める
        totalyen=yen1+yen5*5+yen10*10+yen50*50+yen100*100
        # 総金額を表示
        print("  {}円".format(totalyen))

        # 入力させる用
        more=""
        # 1か2が入力されるまで繰り返す
        while more!="1" and more!="１" and more!="2" and more!="２":
            # 答えるか問題を変更するかを入力させる
            more=input("\n1.答える     2.問題を変更\n >> ")

    # start:始まりの時間
    start=time.time()
    # 答えが入力されるまで繰り返し
    while flog==0:
        # エラー用
        try:    
            # 答え(1~100円玉の枚数)を入力させる
            ans1=int(input("\n1円の枚数は？  >> "))
            ans5=int(input("\n5円の枚数は？  >> "))
            ans10=int(input("\n10円の枚数は？  >> "))
            ans50=int(input("\n50円の枚数は？  >> "))
            ans100=int(input("\n100円の枚数は？  >> "))
            # 答えを入力したので繰り返し処理から抜ける
            flog=1
            # answerflog:最終確認ループ用
            answerflog=0
            # エラー時用の繰り返し
            while answerflog==0:
                # エラー用
                try:
                    # 答えてもいいかどうかを入力
                    if int(input("\n1.これでOK     2.答えなおす\n >> "))==2:
                        # 2が入力されたら繰り返す
                        flog=0
                    # ループを抜ける
                    answerflog=1
                # エラーが起きた場合    
                except:
                    # パス
                    pass
        # エラーが起きた場合
        except:
            # 整数での入力を促す表示
            print("整数で入力してください")
            # エラーが起きたので繰り返す
            flog=0

    # 経過時間を今の時間から始まりの時間(stert)を引いて求める
    end=time.time()-start
    # 小数点第2以下切り捨て
    endtime=math.floor(end*100)/100
    # 小数点以下を切り捨てた値を byou に格納
    byou=int(endtime)
    # 小数点以下のみを整数にした値を tenika に格納
    tenika=int((endtime-byou)*100)

    # 入力した答えの金額を求める
    ans=ans1+ans5*5+ans10*10+ans50*50+ans100*100
    # ランダムに決められた1円、10円、100円の総枚数を求める
    yenmai1=yen1+yen10+yen100
    # 入力した1円、10円、100円の総枚数を求める
    ansmai1=ans1+ans10+ans100
    # ランダムに決められた5円、50円の総枚数を求める
    yenmai5=yen5+yen50
    # 入力した5円、50円の総枚数を求める
    ansmai5=ans5+ans50

    # 総金額、1円 10円 100円の総枚数、5円 50円の総枚数が同じな場合
    if ans==totalyen and ansmai1==yenmai1 and ansmai5==yenmai5:
        # 正解の文を表示する
        print("\n\nおめでとうございます。あなたの勝ちです。")
        # クリアタイムを表示する
        print("クリアタイム： {}秒{}".format(byou,tenika))
        input()
        print("\n----------------------------------------")
            
    # そうでない場合
    else:
        # 不正解の文を表示させる
        print("\n\nあなたの負けです。次回は頑張ってください。")
        # ランダムに決められた1~100円玉の答えの枚数を表示させる
        print("\n答え     1円の枚数：",yen1)
        print("　　     5円の枚数：",yen5)
        print("　　    10円の枚数：",yen10)
        print("　　    50円の枚数：",yen50)
        print("　　   100円の枚数：",yen100)
        input()
        print("\n----------------------------------------")
        
# 関数 timerap --------------------------------------------------------------------------------------------------------- #

def timerap():

    # 初期値設定
    # end:現在までの総秒数
    end=0
    # yuyo:成功猶予
    yuyo=3
    # nok:成功失敗を表示
    nok=""
    # roop:特に意味のない無限ループ用
    roop=0
    # keikatime:playerの押したタイム
    keikatime=0
    # seikou:成功回数
    seikou=0
    # seikouyuyo:最後に成功した最短猶予
    seikouyuyo=" - "
    # gamestert:ゲーム開始用
    gamestert=0
    
    print("\n\n----------------------------------------")
    
    # 1が入力されるまで繰り返す
    while gamestert!="1" and gamestert!="１":
        # 始めるかルール説明を聞くかを入力させる
        gamestert=input("\n＜タイムラップ＞\n1.はじめる     2.ルール説明\n >> ")
        # 2が入力されている間繰り返す
        while gamestert=="2" or gamestert=="２":
            # 解説文
            print("ランダムに表示される時間に合わせてEnterを押してください。")
            print("成功した場合はそのまま続き、またランダムに時間が表示されます。")
            print("そのときの猶予はどんどん短くなっていきます。")
            print("最高難易度(猶予0.1秒)成功を目指して頑張ってください。")
            # 入力させる
            gamestert=input("\n1.はじめる     2.もう一度聞く\n >> ")

    # タイムスタート(Enterを入力)
    input("\nEnterでスタート\n")

    # カウントダウン
    # 3回繰り返す
    for i in range(3):
        # 3-iを表示
        print(3-i)
        # 1秒待つ
        time.sleep(1)
    # stert!
    print("STERT!\n")

    # starttime:始まりの時間
    starttime=time.time()

    # 無限ループ
    while roop==0:

        # 押させる時間をランダムに決める(3~10秒まで)
        rap=rd.randint(3,10)
        # 表示する時間をランダムに決める(1~押させる時間-1秒まで)
        hyoujitime=rd.randint(1,rap-1)
        # 総経過時間
        end+=rap

        # ランダムに決めた hyoujitime の分だけ待つ
        time.sleep(hyoujitime)
        # 押させる時間を表示し、時間になったら押させる
        input("\n{}秒でラップ(猶予{}秒)".format(end,yuyo))
        # 始まりの時間から押された時間を引いた時間を求める
        endtime=time.time()-starttime
        # 小数点第2以下切り捨て
        keikatime=math.floor(endtime*100)/100

        # 小数点以下を切り捨てた値を byou に格納
        byou=int(keikatime)
        # 小数点以下のみを整数にした値を tenika に格納
        tenika=int((keikatime-byou)*100)

        # 押した時間がランダムに決められた時間の猶予内に収まっていた場合(成功した場合)
        if keikatime<=end+yuyo and keikatime>=end-yuyo:
            # 「ok」を nok に格納
            nok="ok"
            # 成功数+1
            seikou+=1
            # 成功猶予を格納
            seikouyuyo=str(yuyo)
            # 猶予が0.1であった場合
            if yuyo==0.1:
                # 押した時間を表示する
                print("{}秒{}   {}".format(byou,tenika,nok))
                # 終了
                input("\n\n終了")
                # クリアした文を表示する
                print("あなたは最高難易度(猶予0.1秒)をクリアしました。\nおめでとうございます。")
                input()
                print("\n----------------------------------------")
                break
        else:
            # 「失敗」を nok に格納
            nok="失敗"
            # 押した時間を表示する
            print("{}秒{}   {}".format(byou,tenika,nok))
            # 終了
            input("\n\n終了")
            # 成功回数と成功最短猶予を表示する
            print("{}回成功(成功最短猶予{}秒)".format(seikou,seikouyuyo))
            input()
            print("\n----------------------------------------")
            break

        # 猶予時間を0.3秒減らす
        yuyo=math.floor((yuyo-0.3)*10)/10
        # 猶予時間が0秒以下の場合
        if yuyo<=0:
            # 猶予時間を0.1秒とする
            yuyo=0.1    

        # 押した時間を表示する
        print("{}秒{}   {}".format(byou,tenika,nok))

# 関数 kaiwa --------------------------------------------------------------------------------------------------------- #

# ゲームロボ(案内役)の標準的な喋り用
# 会話の配列(kaihai)を受け取る
def kaiwa(kaihai):
    # kaihai の要素数だけ繰り返す
    for go in range(len(kaihai)):
        # 0.1秒待つ
        time.sleep(0.1)
        # kaihaiの要素を改行なし、即時で表示
        print(kaihai[go],end="",flush="True")

# 関数 yukkurikaiwa -------------------------------------------------------------------------------------------------- #

# ゲームロボ(案内役)のゆっくりとした喋り用
# 会話の配列(kaihai)を受け取る
def yukkurikaiwa(kaihai):
    # kaihai の要素数だけ繰り返す
    for go in range(len(kaihai)):
        # kaihaiの要素を改行なし、即時で表示
        print(kaihai[go],end="",flush="True")
        # 0.5秒待つ
        time.sleep(0.5)

# 初期値設定 ---------------------------------------------------------------------------------------------------------- #

# koukando:ゲームロボの好感度(おまけ要素)
koukando=0
# game:ゲーム選択用
game=""
# gameendflog:終了用
gameendflog=0

# メイン処理 ---------------------------------------------------------------------------------------------------------- #

# 会話文
kaiwa(["\nこ","ん","に","ち","は","！"])
input()
kaiwa(["私","は","ゲ","ー","ム","ロ","ボ","、","よ","ろ","し","く","ね","。"])
input()

# 会話文
kaiwa(["\n\nあ","な","た","は","ゲ","ー","ム","、","好","き","？"])
# ゲームについて入力させる
kaiwahajime=input("\n >> ")

# 「すき」と入力された場合
if "すき" in kaiwahajime:
    # 会話文
    kaiwa(["ほ","ん","と","？","う","れ","し","い","！"])
    input()
    koukando+=1
# 「きらい」と入力された場合
elif "きらい" in kaiwahajime:
    # 会話文
    kaiwa(["そ","っ","か",".",".",".","残","念",".",".",".","。"])
    input()
    kaiwa(["\nで","も","、","こ","れ","を","機","に","ゲ","ー","ム","を","好","き","に","な","っ","て","も","ら","え","る","よ","う","、"])

# 会話文
kaiwa(["\n3","つ","の","楽","し","い","ゲ","ー","ム","を","用","意","し","た","か","ら","、"])
kaiwa(["\n良","け","れ","ば","遊","ん","で","い","っ","て","欲","し","い","な","。"])
input("\n\n\n")


while gameendflog==0:
    # エラー用
    try:
        # 会話文
        print("\n")
        rdkaiwaokaeri=rd.randint(1,2)
        if koukando>=8:
            if game=="1" or game=="１" or game=="2" or game=="２" or game=="3" or game=="３":
                if rdkaiwaokaeri==1:
                    kaiwa(["\n\nお","か","え","り","、","楽","し","か","っ","た","？"])
                elif rdkaiwaokaeri==2:
                    kaiwa(["\n\nあ","っ","、","帰","っ","て","き","た","！"])
                input()
        elif koukando<=-5:
            yukkurikaiwa(["\n\n.",".","."])
        else:
            if game=="1" or game=="１" or game=="2" or game=="２" or game=="3" or game=="３":
                if rdkaiwaokaeri==1:
                    kaiwa(["\n\nど","う","だ","っ","た","か","な","？"])
                elif rdkaiwaokaeri==2:
                    kaiwa(["\n\n楽","し","ん","で","く","れ","た","か","な","？"])
                input()
                kaiwa(["次","は"])
        
        # 会話文
        rdkaiwagamesentaku=rd.randint(1,2)
        if koukando>=8:
            if rdkaiwagamesentaku==1:
                kaiwa(["あ","な","た","は","ど","の","ゲ","ー","ム","が","好","き","？"])
            elif rdkaiwagamesentaku==2:
                kaiwa(["ど","れ","に","し","よ","う","か","な"])
                yukkurikaiwa([".",".","."])
                rdrobokaiwa=rd.randint(1,3)
                if rdrobokaiwa==1:
                    kaiwa(["計","算","2","0","な","ん","て","ど","う","？"])
                elif rdrobokaiwa==2:
                    kaiwa(["硬","貨","数","え","な","ん","て","ど","う","？"])
                elif rdrobokaiwa==3:
                    kaiwa(["タ","イ","ム","ラ","ッ","プ","な","ん","て","ど","う","？"])
        elif koukando<=-5:
            if rdkaiwagamesentaku==1:
                kaiwa(["で","、","ど","う","す","る","の","？"])
            elif rdkaiwagamesentaku==2:
                kaiwa(["早","く","き","め","て","。"])
        else:
            if rdkaiwagamesentaku==1:
                kaiwa(["ど","の","ゲ","ー","ム","に","す","る","？"])
            elif rdkaiwagamesentaku==2:
                kaiwa(["な","に","で","遊","ぶ","？"])
        
        # ゲームを選択させる
        game=input("\n\n1.計算20     2.硬貨数え     3.タイムラップ     4.さようなら\n >> ")
        # 1を選択した場合
        if game=="1" or game=="１":
            # 会話文
            kaiwa(["ち","ょ","っ","と","ま","っ","て","て","、","今","準","備","す","る","か","ら"])
            yukkurikaiwa([".",".","."])
            # ゲーム「計算20」呼び出し
            keisan20()
            koukando+=1
        # 2を選択した場合
        elif game=="2" or game=="２":
            # 会話文
            kaiwa(["ち","ょ","っ","と","ま","っ","て","て","、","今","準","備","す","る","か","ら"])
            yukkurikaiwa([".",".","."])
            # ゲーム「硬貨数え」呼び出し
            koukakazoe()
            koukando+=1
        # 3を選択した場合
        elif game=="3" or game=="３":
            # 会話文
            kaiwa(["ち","ょ","っ","と","ま","っ","て","て","、","今","準","備","す","る","か","ら"])
            yukkurikaiwa([".",".","."])
            # ゲーム「タイムラップ」呼び出し
            timerap()
            koukando+=1
        # 4を選択した場合
        elif game=="4" or game=="４":
            print("\n")
            # gameendflog に1を格納してループを抜ける
            gameendflog=1
            # 以下会話文が続く
            rdkaiwasayounara=rd.randint(1,2)
            if koukando>=8:
                if rdkaiwasayounara==1:
                    kaiwa(["さ","よ","う","な","ら","、","ま","た","き","て","ね","！"])
                elif rdkaiwasayounara==2:
                    kaiwa(["ば","い","ば","い","、","ま","た","き","て","く","れ","る","と","嬉","し","い","な","！"])
            elif koukando<=-5:
                if rdkaiwasayounara==1:
                    yukkurikaiwa([".",".",".","。"])
                elif rdkaiwasayounara==2:
                    kaiwa(["も","う","こ","な","い","で","ね","。"])
            else:
                if rdkaiwasayounara==1:
                    kaiwa(["さ","よ","う","な","ら","！"])
                elif rdkaiwasayounara==2:
                    kaiwa(["ば","い","ば","い","！"])
            print("\n")
        elif "おすすめ" in game:
            kaiwa(["\n私","の","お","す","す","め","は","ね"])
            yukkurikaiwa([".",".","."])
            kaiwa(["硬","貨","数","え","！"])
            input("\n\n")
        elif "せいべつ" in game:
            kaiwa(["\nロ","ボ","ッ","ト","に","性","別","な","ん","て","な","い","よ","。"])
            input("\n\n")
        elif "きらい" in game:
            kaiwa(["\nそ","っ","か"])
            yukkurikaiwa([".",".","."])
            if koukando>0:
                koukando=koukando-1
            input("\n\n")
        elif "かっこいい" in game:
            kaiwa(["\nほ","ん","と","？","あ","り","が","と","う","！"])
            input("\n\n")
            koukando+=1
        elif "かわいい" in game:
            kaiwa(["\nえ","へ","へ","、","う","れ","し","い","な","。"])
            input("\n\n")
            koukando+=1
        elif "すき" in game:
            kaiwa(["\nう","え","ぇ","っ","、"])
            time.sleep(0.8)
            yukkurikaiwa(["あ","っ"])
            kaiwa(["あ","り","が","と","う",""])
            yukkurikaiwa([".",".","."])
            koukando+=2
            input("\n\n")
        elif "あいして" in game:
            kaiwa(["\nう","え","ぇ","っ","、"])
            time.sleep(0.8)
            yukkurikaiwa(["あ","っ"])
            kaiwa(["あ","り","が","と","う",""])
            yukkurikaiwa([".",".","."])
            koukando+=2
            input("\n\n")        
        elif "えらー" in game:
            erorr=1/0
            input("\n")
        elif "ばか" in game:
            if koukando>=1:
                kaiwa(["\nそ","ん","な","こ","と","言","う","人","じ","ゃ","な","い","と","思","っ","て","た","の","に"])
            yukkurikaiwa([".",".","."])
            koukando=koukando-1
            input("\n\n")
        elif "あほ" in game:
            if koukando>=1:
                kaiwa(["\nそ","ん","な","こ","と","言","う","人","じ","ゃ","な","い","と","思","っ","て","た","の","に"])
            yukkurikaiwa([".",".","."])
            koukando=koukando-1
            input("\n\n")
        elif "しね" in game:
            if koukando>=1:
                kaiwa(["\nそ","ん","な","こ","と","言","う","人","じ","ゃ","な","い","と","思","っ","て","た","の","に"])
            yukkurikaiwa([".",".","."])
            koukando=koukando-2
            input("\n\n")
        elif "ころす" in game:
            kaiwa(["\nひ","っ",])
            yukkurikaiwa([".",".","."])
            kaiwa(["こ","わ","い",".",".","."])
            koukando=koukando-2
            input("\n\n")
        elif "こうかんどそうさ" in game:
            kaiwa(["\nﾎ","ﾝ","ﾄ","ｳ","ﾆ","ｺ","ｳ","ｶ","ﾝ","ﾄﾞ","ｦ","ｿ","ｳ","ｻ","ｼ","ﾃ","ﾓ","ﾖ","ｲ","ﾃﾞ","ｽ","ｶ","?"])
            if input(" >> ")=="はい":
                kaiwa(["\nｺ","ｳ","ｶ","ﾝ","ﾄﾞ","ﾉ","ｱ","ﾀ","ｲ","ｦ","ﾆ","ｭ","ｳ","ﾘ","ｮ","ｸ","ｼ","ﾃ","ｸ","ﾀﾞ","ｻ","ｲ"])
                koukando=int(input(" >> "))
                yukkurikaiwa(["\n.",".","."])
                kaiwa(["ｺ","ｳ","ｶ","ﾝ","ﾄﾞ","ｦ","ﾍ","ﾝ","ｺ","ｳ","ｼ","ﾏ","ｼ","ﾀ"])
            else:
                kaiwa(["\nﾁ","ｭ","ｳ","ｼ","ｼ","ﾃ","ｲ","ﾏ","ｽ"])
                yukkurikaiwa([".",".","."])
            input("\n\n")
        elif "こうかんど" in game:
            kaiwa(["\nﾀ","ﾀﾞ","ｲ","ﾏ","ﾉ","ｺ","ｳ","ｶ","ﾝ","ﾄﾞ","ﾊ","｢"])
            yukkurikaiwa(["",koukando])
            kaiwa(["｣","ﾃﾞ","ｽ"])
            input("\n\n")
        elif "ありがと" in game:
            kaiwa(["\nど","う","い","た","し","ま","し","て","。"])
            koukando+=1
            input("\n\n")
        elif "ごめん" in game:
            if koukando<=-1:
                koukando+=2
            if koukando>=-1:
                kaiwa(["\n大","丈","夫","だ","よ","。"])
            else:
                yukkurikaiwa(["\n.",".","."])
            input("\n\n")
        elif game!="":
            print("\n",game,end="")
            kaiwa(["っ","て","ど","う","い","う","意","味","だ","ろ","う","？"])
            input("\n\n")

    # エラーが起きた場合ここまで処理を飛ばす
    except:
        kaiwa(["\n\nエ","ラ","ー","が","発","生","し","ち","ゃ","っ","た","み","た","い","。"])
        input("")
        kaiwa(["い","ま","戻","す","ね"])
        yukkurikaiwa([".",".","."])
        print("\n\n")