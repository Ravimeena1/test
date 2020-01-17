import  math
n=int(input("how many data you want enter \n"))
up,down,left,p1,p2,rigth=0,0,0,0,0,0
list1=[]
for i in range(n):
    list1 = []
    s=input("enter data \n")
    list1=s.split(" ")
    if list1[0]=="UP":
        up+=int(list1[1])
    elif list1[0]=="DOWN":
        down+=int(list1[1])
    elif list1[0] == "LEFT":
        left+= int (list1[1])
    elif list1[0] == "RIGTH":
        rigth+= int (list1[1])

if(up>down):
    p1=up-down
else:
    p1=down-up
if (left>rigth):
    p2 = left -rigth
else:
    p2 =rigth-left



s= (p1*p1)+(p2*p2)
s=int(math.sqrt(s))
print(s)

