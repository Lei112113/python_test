path='class.txt'

#欄位名稱
print('name, score1, score2, score3, sum, avg')
#開檔案
with open(path, 'r', encoding="utf-8") as file:
    for line in file.readlines():
        #去除字尾\n
        file_item = line.strip()
        #切割成list
        file_item = file_item.split(' ')
        #計算個人總和及平均
        _sum = (float(file_item[1]) + float(file_item[2]) + float(file_item[3]))
        _avg = round(_sum / 3, 2)

        #總和及平均塞進list
        #這裡如果不轉字串無法用join
        file_item.append(str(_sum))
        file_item.append(str(_avg))

        #每一個人的成績從list轉為字串,用以去除不必要的符號
        print(' '.join(file_item))
