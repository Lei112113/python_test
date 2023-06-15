print('''1.print students' grade 
2.print subject score 
3.rank students
4.search for name
5.exit''')
choice=''
path="class.txt"

class Student:
    s=[]
    sum=0
    content = []
    def __init__(self):
        with open(path) as file:
          for line in file.readlines():
             s = line.strip()
             self.s.append(s.split(' ')) 
             
             
    def one(self):
        for s in self.s:
            sum=(float(s[1])+float(s[2])+float(s[3]))
            final=round(sum/3,2)
            s.append(sum)
            s.append(final)
            print(s)

    def two(self):
       sum1 = sum2 = sum3 = 0
       for s in self.s:
            sum1=sum1+int(s[1])
            sum2=sum2+int(s[2])
            sum3=sum3+int(s[3]) 
            avg1=round(sum1/3,2)
            avg2=round(sum2/3,2)
            avg3=round(sum3/3,2)
       print(sum1, sum2, sum3, avg1, avg2, avg3)

    def three(self):
      for s in self.s:
         self.content.append(s) 
         self.content.sort(key=lambda x:x[5], reverse=True)
         i = 1
      for student in self.content:
        print(i, student, student[4])
        i = i + 1

    def four(self):
     name = input("enter student's name: ")
     comparison={}
     for s in self.s:
        comparison[s[0]] = s[1:6]
     sum = 0
     for i in comparison:
            if(name in i ):
               print(i, comparison[i])
            else:
               sum = sum + 1
            if(sum == len(comparison) and name not in i):
               print('查無此人')
    
    
student=Student()
choice=''
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


            
