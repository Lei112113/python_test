#為了正規表達式
import re
choice = ''
path = 'class.txt'
_sum = [0, 0, 0]
_avg = [0, 0, 0]
content = []


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
        return file_item

def list2string(origin_list):
    #顯示時不要有[]的處理
    #1.轉字串
    file_item = str(origin_list)
    #2.將字串正規去掉不要的符號
    file_item =  re.sub(r"[\[\]']", "", file_item)
    return file_item

while choice != '5':

    choice = input('''
1.print students' grade
2.print subject score
3.rank students
4.search for name
5.exit
please chose one and enter its number: ''')

    match choice:
        case '1':
            print('name, score1, score2, score3, sum, avg')
            with open(path, 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    file_item = everytodo(line)
                    #將list轉字串後，再將不必要的符號去除
                    file_item = list2string(file_item)
                    print(file_item)

        case '2':
            with open(path, 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    file_item = everytodo(line)
                    for idx, x in  enumerate(_sum):
                        _sum[idx] = x + int(file_item[idx + 1])
                        _avg[idx] = round(_sum[idx] / 3, 2)
                #顯示時不要有[]的處理
                #1.轉字串
                _sum = str(_sum)
                _avg = str(_avg)
                #2.將字串正規去掉不要的符號
                _sum =  re.sub(r"[\[\]]", "", _sum)
                _avg =  re.sub(r"[\[\]]", "", _avg)


                #f-string好像不是function的特殊語法，雖然不知道她到底屬於什麼，暫時當作func
                #可以讓字串中間夾雜變數的方便東西
                print(f'各科成績總和: {_sum}\n各科成績平均: {_avg}')


                '''
                TODO UX的作法
                print("score1_sum, score2_sum, score3_sum")
                print(_sum)
                print("score1_avg, score2_avg, score3_avg")
                print(_avg)
                '''

        case '3':
            print('ranking, name, score1, score2, score3, sum, avg')
            with open(path, 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    file_item = everytodo(line)

                    #全部資料都放進 list 方便排序
                    content.append(file_item)
                    #key是排序的標準 需要透過function才能附值 所以用lambda 將x[4]的值賦予x 而key=x
                    #reverse=True表示從大排到小
                    content.sort(key=lambda x:x[4], reverse=True)
                #enumerate 讓 list 可以在 for 有 key 跟 value 可以顯示
                for idx, x in  enumerate(content):
                    #將list變成字串才能進行正規劃，去除不要的符號(UX表現的部分)
                    x = str(x)
                    x =  re.sub(r"[\[\]']", "", x)
                    #idx+1 顯示排名 x 是個學生資料
                    print(idx + 1, x)

        case '4':
            name = input("enter student's name (case sensitive): ")
            #為了設定沒有找到學生時的數值
            found = False
            with open(path, 'r', encoding="utf-8") as file:
                    for line in file.readlines():
                        file_item = everytodo(line)
                        for txt_name in file_item[0]:
                            if(txt_name == name):
                                #將list轉字串後，再將不必要的符號去除
                                file_item = list2string(file_item)
                                print(file_item)
                                #當學生被找到
                                found = True
                    #全部都找不到相符的學生
                    if not found:
                        print("Couldn't find the student.")



        case '5':
          break
        case _:
         print("enter 1-5")
