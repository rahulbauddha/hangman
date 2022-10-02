hng=['____',
'|    |',
'|    |',
'|    O',
'''|   /|\ ''''',
'|    |',
'|   /|\ '''
]
name=input("please enter your name:- ")
print("welcome",name)
import random

list1=['rahul','manjitey','ram','pravin']
word=random.choice(list1)
a=[]
for j in range(len(word)):
   a+='_'
print(a)
count=0
cond=True
while cond:
   guess=input("guess your alphabet.. ")
   alpha=word.find(guess)
   if guess in word:
       a[alpha]=guess
       print(a)
   else:
       print("wrong guess")
       count+=1
       for i in range(count):
           print(hng[i])
   if count==len(hng):
       cond=False
       