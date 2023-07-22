#讀取的檔案位置
path = 'class.txt'

#讀取後數值的預處理
def val_preprocess(line):
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

#將個人成績的list轉為字串
def list2string(origin_list):
    #join 每一個人的成績從list轉為字串,用以去除不必要的符號
    file_item = ' '.join(origin_list)
    return file_item

#預設選項，不先預設choice會出現錯誤
choice = ''
#成績總數與平均的設定
_sum = [0, 0, 0]
_avg = [0, 0, 0]
#第三題要用的容器，方便排序
content = []
while choice != '5':

    choice = input('''
        1.print students' grade
        2.print subject score
        3.rank students
        4.search for name
        5.exit
        please chose one and enter its number: ''')

    match choice:
        #1.print students' grade
        case '1':
            print('name, score1, score2, score3, sum, avg')
            with open(path, 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    file_item = val_preprocess(line)
                    #將list轉字串後，再將不必要的符號去除
                    file_item = list2string(file_item)
                    print(file_item)

        # 2.print subject score
        case '2':
            with open(path, 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    file_item = val_preprocess(line)
                    #enumerate可以丟idx跟element出來，一般情況只能丟element
                    for idx, x in  enumerate(_sum):
                        _sum[idx] = int(x) + int(file_item[idx + 1])
                        _avg[idx] = round(_sum[idx] / 3, 2)
                        # print(_sum, file_item[0], file_item[idx + 1])

                #f-string好像不是function的特殊語法，雖然不知道她到底屬於什麼，暫時當作func
                #可以讓字串中間夾雜變數的方便東西
                print(f"各科成績總和: { _sum[0] }, { _sum[1] }, { _sum[2] }\n各科成績平均: { _avg[0] }, { _avg[1] }, { _avg[2] }")
                _sum = [0, 0, 0]
                _avg = [0, 0, 0]


                '''
                TODO UX的作法
                print("score1_sum, score2_sum, score3_sum")
                print(_sum)
                print("score1_avg, score2_avg, score3_avg")
                print(_avg)
                '''
        # 3.rank students
        case '3':
            print('ranking, name, score1, score2, score3, sum, avg')
            with open(path, 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    file_item = val_preprocess(line)

                    #全部資料都放進 list 方便排序
                    content.append(file_item)

                    #key是排序的標準 需要透過function才能附值 所以用lambda 將x[4]的值賦予x 而key=x
                    #reverse=True表示從大排到小
                    content.sort(key=lambda x:x[4], reverse=True)

                #enumerate 讓 list 可以在 for 有 key 跟 value 可以顯示
                for idx, element in  enumerate(content):
                    #idx+1 顯示排名
                    element.insert(0, str(idx + 1))
                    #將list組成字串
                    element =  list2string(element)
                    # x 是一個學生資料
                    print(element)
                content = []

        # 4.search for name
        case '4':
            txt_name = input("enter student's name : ")
            #為了設定沒有找到學生時的數值
            found = False
            #確定指印一次標題
            i = 0
            with open(path, 'r', encoding="utf-8") as file:
                    for line in file.readlines():
                        #將讀取的值進行預處理，去除不必要的符號及計算總成績等
                        file_item = val_preprocess(line)
                        txt_name = txt_name.lower()
                        file_item_chk = file_item[0].lower()

                        if txt_name in file_item_chk:
                            if i == 0:
                                print('name, score1, score2, score3, sum, avg')
                            i = i + 1
                            #當學生被找到
                            #將list組成字串
                            file_item =  list2string(file_item)
                            #印出學生資料
                            print(file_item, i)
                            #將有沒有找到學生的參數設為true
                            found = True
                    #全部都找不到相符的學生
                    if not found:
                        print("Couldn't find the student.")


        # 5.exit
        case '5':
          break
        case _:
         print("enter 1-5")

