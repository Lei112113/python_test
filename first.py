path="class.txt"
file=open(path,"r")
final=0

with open(path) as file:
    for line in file.readlines():
        s = line.split(' ')
        print(s)
        sum=(float(s[1])+float(s[2])+float(s[3]))
        final=round(sum/3,2)
        print(sum,final)
      


