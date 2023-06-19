#為了正規表達式
import re
choice = ''
path = 'class.txt'
_sum = [0, 0, 0]

def everytodo(line):
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
        return file_item

while (choice != '5'):
    
    choice = input('''
1.print students' grade 
2.print subject score 
3.rank students
4.search for name
5.exit
please chose one and enter its number: 
''')
    
    match choice:
        case '1':
            with open(path, 'r') as file:
             for line in file.readlines():
                file_item = everytodo(line)
                print(file_item)
        case '2':
           pass
               
        case '3':
            pass

        case '4':
           pass
        case '5':
          break; 
        case _:
         print("input 1-5")



   
