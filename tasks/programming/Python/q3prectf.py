import math
a=int(input("enter a number: "))
list1=[]
list2=[]
for i in range(a):
    i=i+1
    list1=list1+[i]
for j in list1:
    x=j*j
    list2=list2+[x]

for k in list2:
    for l in list2:
        if ((k+l) == a):
            print("a can be represented as the squares of",math.sqrt(k),math.sqrt(l))