print('''1.print students' grade 
2.print subject score 
3.rank students
4.search for name
5.exit''')
choice=''
path="class.txt"

class Student:
    s=[]
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
            print(s[0],s[1:4],sum,final)
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
         
         comparison = []
         comparison.append(s[0]) 
         comparison.append(float(s[1])+float(s[2])+float(s[3]))
         self.content.append(comparison)
         self.content.sort(key=lambda x:x[1], reverse=True)
         i = 1
      for student in self.content:
        print(i,student)
        i = i + 1
    
    
student=Student()
student.three()

            
