while True:
    q1 = input('Q1　時間はいつですか？1　朝/2　昼/3　夕方/4　夜：')
    q2 = input('Q2　場所はどこですか？1　屋内/2　屋外/')
    q3 = input('Q3　あなたの今の感情はどんなものですか？1　楽しい/2　悲しい/3　イライラ：')
    if   q1 == '1' and q2 == '1' and q3 =='1' :
        ans = 'FIVE NEW OLDのHallelujah（https://youtu.be/iSsgv0pZ1Y4）'
    elif q1 == '1' and q2 == '2' and q3 =='1' :
        ans = 'リュックと添い寝ごはんのThank you for the Music（https://youtu.be/In5s-Xuqm18）'
    elif q1 == '1' and q2 == '1' and q3 =='2' :
        ans = 'sumikaのフィクション（https://youtu.be/IKHGAuNaGuA）'
    elif q1 == '1' and q2 == '1' and q3 =='3' :
        ans = 'SiMのKiLLiNG ME（https://youtu.be/vyUMYYc8lxU）'
    elif q1 == '1' and q2 == '2' and q3 =='2' :
        ans = 'SUPER BEAVERの人として（https://youtu.be/5cvXmuuC1GI）'
    elif q1 == '1' and q2 == '2' and q3 =='3' :
        ans = 'coldrainのENVY（https://youtu.be/2teepAfDrXI）'
    elif q1 == '2' and q2 == '1' and q3 =='1' :
        ans = 'FLOWのGO!!!（https://youtu.be/zejYD43HyQo）'
    elif q1 == '2' and q2 == '2' and q3 =='1' :
        ans = '東京事変のキラーチューン（https://youtu.be/lC8la4l4RhQ）'
    elif q1 == '2' and q2 == '1' and q3 =='2' :
        ans = '[Alexandros]の明日、また（https://youtu.be/qVDgV2JQydk）'
    elif q1 == '2' and q2 == '1' and q3 =='3' :
        ans = 'Fear, and Loathing in Las VegasのRave-up Tonight（https://youtu.be/BDFD2WopIjY）'
    elif q1 == '2' and q2 == '2' and q3 =='2' :
        ans = 'ねぐせ。の日常革命（https://youtu.be/Z-1qpeyaNb0）'
    elif q1 == '2' and q2 == '2' and q3 =='3' :
        ans = 'サイダーガールの週刊少年ゾンビ（https://youtu.be/G72ZSi951i4）'
    elif q1 == '3' and q2 == '1' and q3 =='1' :
        ans = 'マカロニえんぴつの洗濯機と君とラヂオ（https://youtu.be/LLYPfI-cFcc）'
    elif q1 == '3' and q2 == '1' and q3 =='2' :
        ans = 'Saucy Dogのコンタクトケース（https://youtu.be/62aNm2fVxXs）'
    elif q1 == '3' and q2 == '1' and q3 =='3' :
        ans = 'Mrs. GREEN APPLEのツキマシテハ（https://youtu.be/P2GhoO-u0kI）'
    elif q1 == '3' and q2 == '2' and q3 =='1' :
        ans = 'Official髭男dismの犬かキャットかで死ぬまで喧嘩しよう！（https://youtu.be/IzyrINr2Xj4）'
    elif q1 == '3' and q2 == '2' and q3 =='2' :
        ans = 'TETORAの今日くらいは（https://youtu.be/1fC8wAwBqXc）'
    elif q1 == '3' and q2 == '2' and q3 =='3' :
        ans = 'THE ORAL CIGARETTESのカンタンナコト（https://youtu.be/X0g5BO6zyxA）'
    elif q1 == '4' and q2 == '1' and q3 =='1' :
        ans = '浪漫革命の楽しい夜ふかし（https://youtu.be/FZOmkLbm66I）'
    elif q1 == '4' and q2 == '2' and q3 =='1' :
        ans = 'Tempalayの革命前夜（https://youtu.be/219q3PhaYuE）'
    elif q1 == '4' and q2 == '1' and q3 =='2' :
        ans = 'PEOPLE1の113号室（https://youtu.be/4ewLWtoDhjQ）'
    elif q1 == '4' and q2 == '1' and q3 =='3' :
        ans = 'Mr.FanTastiCのヨルノブルース（https://youtu.be/bEuCFKk0cCQ）'
    elif q1 == '4' and q2 == '2' and q3 =='2' :
        ans = 'koboreのヨルノカタスミ（https://youtu.be/q4WgiiOlZj8）'
    elif q1 == '4' and q2 == '2' and q3 =='3' :
        ans = 'RADWIMPSのDADA（https://youtu.be/Yy6XeGCNkSM）'
    else:
        print('A, あなたへのオススメの曲はスパムです。')
        break

    print('A, 今のあなたへオススメの曲は{}です。'.format(ans))