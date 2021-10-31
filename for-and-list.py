 # while loop
i=0
sum=0
while i<=100:
    i+=1
    if(i%2==0):
        continue
    sum+=i
print(sum)

myList=list(range(5,10)) # 10 dahil değil.
print(myList)
#---------------
list1=[1,2,3]  
list2=['a','b']
print(list(zip(list1,list2))) # liste birleştirir, küçük olanın eleman sayısı kadarını birleştiriyor.

numbers=[x for x in range(5)] # liste oluşturulur.
print(numbers)
numbers=[x*x for x in range(5) if(x%3==0)] # 0 3 ==> 0 9 sadece eleman olarak alınır.
print(numbers)

#listeye sondan ekleme yapıyor. -->append()
text='hello'
mylist=[]
for x in text:
    mylist.append(x)
print(mylist)

mylist2=[1,2,2]
for x in mylist2:
    mylist.append(x)
print(mylist)

results=[x if(x%2==0) else 'TEK' for x in range(1,10) ]
print(results)

# random sayıyı bulma -- mini oyun

import random
number = random.uniform(0,101) #random.randint(0,1) 0 1 ... 100

for x in range(5): # 5 şansın var!
    estimate=int(input("enter a number: ")) #tahmin => estimate
    if (estimate==number):
        print("YOU ARE WINNER!")
        break
    else:
        if (4-x==0):
            print("Your chances finished.")
        else:    
            print(f"YOU ARE LOSER! and you have just {4-x} chances.")
        

number=int(input("Enter a number: "))
mylist=[i for i in range(2,number)]
print(mylist)

isprime=True

for i in mylist:
    if((number%i)==0):
        isprime=False
        break
    
if isprime:
    print(f"{number} is a prime number") 
else:
    print(f"{number} is not prime number.")
       
