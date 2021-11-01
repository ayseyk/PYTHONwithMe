i=5
while(i>6):
    print('hey there')
else:
    print("yess")    

def asalbul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1): #aralık arasındaki asal sayıları döndürür.
        if (sayi>1):
            for i in range(2,sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)
            
sayi1=int(input("sayi giriniz:" ))
sayi2=int(input("sayi giriniz:" ))

asalbul(sayi1,sayi2)

def myfunc(sayi):
    mylist=[]   
    for i in range(2,sayi+1):
        if(sayi % i == 0):
            mylist.append(i) # sayının kendisini listeye ekler, sadece.
    print(mylist)

 
sayi1=int(input("sayi giriniz: "))
myfunc(sayi1)