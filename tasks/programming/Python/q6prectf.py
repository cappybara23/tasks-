stringo=input("enter a string: ")
listo=list(stringo)
list_ascii=[]
list_xor=[]
re_list_ascii=[]
re_string=""
for i in listo:
    list_ascii=list_ascii+[ord(i)]
for j in list_ascii:
    xor_char=j^0x69
    list_xor=list_xor+[xor_char,]

for k in list_xor:
    re_ascii=k^0x69
    re_list_ascii=re_list_ascii+[re_ascii,]
for l in list_ascii:
    re_string=re_string+chr(l)

print(list_xor)
print(re_string)