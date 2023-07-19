print('''1.print students' grade
2.print subject score
3.rank students
4.search for name
5.exit''')
choice=''
path="class.txt"

class Student:
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
       #每一個人的成績從list轉為字串,用以去除不必要的符號
       file_item = ' '.join(origin_list)
       return file_item

   #1.print students' grade
   def print_person_grade(self):
      #1.print students' grade
      print('name, score1, score2, score3, sum, avg')
      with open(path, 'r', encoding="utf-8") as file:
            for line in file.readlines():
               file_item = self.val_preprocess(line)
               #將list轉字串後，再將不必要的符號去除
               file_item = self.list2string(file_item)
               print(file_item)


student = Student()
choice = ''
while (choice != '5'):
   choice = input("please chose one and enter its number:")
   match choice:
      case '1':
         student.one()
      case '2':
         student.two()
      case '3':
         student.three()
      case '4':
         student.four()
      case '5':
         break
      case _:
          print("請輸入1-5")



