print('''1.print students' grade 
2.print subject score 
3.rank students
4.search for name
5.exit''')
choice=''
path="class.txt"
sum1 = sum2 = sum3 = 0

while (choice!="5"):
    
    choice=input("please chose one and enter its number:")
    
    match choice:
        case '1':
            with open(path) as file:
             for line in file.readlines():
                 s = line.strip()
                 s = s.split(' ')
                 sum=(float(s[1])+float(s[2])+float(s[3]))
                 final=round(sum/3,2)
                 print(s[0],s[1:4],sum,final)
        case '2':
            with open(path) as file:
             for line in file.readlines():
                 s = line.split(' ')
                
                 
                 sum1=sum1+int(s[1])
                 sum2=sum2+int(s[2])
                 sum3=sum3+int(s[3])

                 avg1=round(sum1/3,2)
                 avg2=round(sum2/3,2)
                 avg3=round(sum3/3,2)
            for i in range(1,4):
                 print( globals()["sum" + str(i)], globals()["avg" + str(i)])
               
        case '3':
            with open(path) as file:
             content = []
             for line in file.readlines():
              
                 s = line.split(' ')
                 comparison = []
                 comparison.append(s[0]) 
                 comparison.append(float(s[1])+float(s[2])+float(s[3]))
                 content.append(comparison)
            content.sort(key=lambda x:x[1], reverse=True)
            i = 1
            for student in content:
               print(i,student)
               i = i + 1
        #另外用dict做一個
        # case '3':
        #     with open(path) as file:
        #     comparison = {}
        #     for line in file.readlines():
              
        #          s = line.split(' ')
        #          comparison[s[0]] = float(s[1])+float(s[2])+float(s[3])
        #          test = sorted(comparison.items(), key=lambda x:x[1], reverse=True)
                
        #     print(test)

        case '4':
           name = input("enter student's name: ")
           with open(path) as file:
            comparison = {}
            for line in file.readlines():
              
                 s = line.strip()
                 s = s.split(' ')
                 comparison[s[0]] = s[1:4]
                 
                
            print(comparison[name])

        case '5':
          break; 
        case _:
         print("請輸入1-5")
   
