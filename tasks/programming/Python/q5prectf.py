stringo=input("enter a string: ")
listo=list(stringo)
list_ascii=[]
re_string=""
for i in listo:
    list_ascii=list_ascii+[ord(i),]
print(list_ascii)
for j in list_ascii:
    re_string=re_string+chr(j)
print("the re-formed string is, ",re_string)