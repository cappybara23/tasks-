word=input("enter a word! ")
rev_word=""
list1 = list(word)
list2 = reversed(list1)
#rev_word = str(list2)
for i in list2:
    rev_word=rev_word+i

if (word == rev_word):
    print("the given word is a palindrome")
else:
    print("the word ain't a palindrome")
