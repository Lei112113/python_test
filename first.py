'''
先寫在前面：
首先這個三連符號可以用來打註解（python）

1. "建議" 在同一個檔案裡面，使用同一種引號，
   除非有特殊理由（例如文字內容有 "'s" 這種）。

2. 運算子（等於、大於小於、賦值等等）前後留空格，函數內的參數指定不留空格。
   多個參數之間逗號加空格隔開。
   這部分比較需要一點點練習，我在下面直接改，你對照著看。

3. 你可以安裝一個叫做 winmerge 的軟體，他可以做檔案的比對，先裝，不懂怎麼用的話再問我。

4. 檔案命名不太好，改名叫做什麼 Question1.py, main.py 之類的會好一些。
   主要是因為你這個檔名不方便一般化，例如你假如有一天需要從 Q1 ~ Q10 都跑一次，你才有辦
   法下一個 for i in range(1, 11) 之類的跑一遍。
   假如要取名叫做 main.py 的話，記得要把每個練習放在不同資料夾，資料夾命名一樣是叫做 Q1
   之類的（或者看你啦，這部分就都可以）。
'''

PATH = 'class.txt' # 這是個不會變的變數，我們稱之為常數，所以會用全大寫 + 底線分隔命名
# file = open(path, 'r')
# 這行刪掉是因為這個其實是在處理開檔，但你在下面的 with open 就已經做了，不需要。
# BTW 這個是舊版的寫法，現在大家都用下面那個寫法了
final = 0 # 這行建議跟上面兩行隔開來，因為沒關聯，應該分開來，增加易讀性。
# 看到後面意外發現你這裡根本不需要先宣告這個變數。

with open(PATH, 'r') as file:
    # 前一行要加 'r'：這個跟 'w' 是相對的，'r'是指讀檔，'w'是指寫檔。
    for line in file.readlines():
        # 我有回饋你一個問題是你的最後一個 element 有多餘的 '\n' 字元，可以在這邊先用
        # line.strip() 來去除句子前後的空格、換行符號。
        # s = line.strip()
        # s = s.split(' ')
        s = line.split(' ')
        # s 這種變數命名稍微不明確，可以的話打清楚一點會比較好，但這邊還好滿簡單看得懂
        print(s)
        sum = (float(s[1]) + float(s[2]) + float(s[3]))
        final = round(sum / 3, 2)
        print(sum, final)



