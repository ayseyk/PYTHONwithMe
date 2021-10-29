myList= [1,2,3,4]

def tekMi(mylist):
    
    for i in range(0,len(mylist)):
        if(mylist[i] % 2 == 0):
            mylist[i]="cift"
        else:
            mylist[i] = "tek"
            
    for i in mylist:
        print(i)

tekMi(myList) #fonk çağrısı

print("***********************************")
i=1
while i<5:
    print(i,'*5= ',i*5)
    i+=1