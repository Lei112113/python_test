path='class.txt'

#為了正規表達式
import re

#欄位名稱
print('name, score1, score2, score3, sum, avg')
#開檔案
with open(path, 'r') as file:
    for line in file.readlines():
        #去除字尾\n
        file_item = line.strip()
        #切割成list
        file_item = file_item.split(' ')
        #計算個人總和及平均
        _sum = (float(file_item[1]) + float(file_item[2]) + float(file_item[3]))
        _avg = round(_sum / 3, 2)

        #總和及平均塞進list
        file_item.append(str(_sum)) 
        file_item.append(str(_avg)) 

        #顯示時不要有[]的處理
        #1.轉字串
        file_item = str(file_item)
        #2.將字串正規去掉不要的符號
        file_item =  re.sub(r"[\[\]']", "", file_item)
   
        print(file_item)
        
        
        
 
      


