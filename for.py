name='ayse ykaya' # str
for n in name:
    print(n)

name=['ayse ykaya'] # list --> tek elemanlı
for n in name:
    print(n)

tuple=[(1,2),(2,3),(3,4)] # ==> tuple =(1,2),(2,3),(3,4)
for t in tuple:
    print(t)

for a,b in tuple:
    print(a,b)

tuple='ayse','banana'
print(type(tuple))

d={'k1':1,'k2':2} # dictionary
for value in d.items(): # key,value olarak alınarak teker teker erişim sağlanabilir.
    print(value)

# listedeki elemanlara göre işlemler yapıp, ekrana bazı çıktılar yazmakta.
numbers=[1,3,5,7,9,12,19,21]
sum=0
for a in numbers:
    if(a%3==0):
        print(a,"--a%3")
    sum+=a
    if(a%2==1):
        print(a**2," a**2")    
print(f"Sum of the numbers is: {sum}")        

# şehrin kelime sayısı 5' ten küçük olanları yazdırmakta.
cities=['Kocaeli','Istanbul','Trabzon','Izmir','Van'] # 7, 8, 7, 5, 3 
for  city in cities:
    if(len(city)<=5):
        print(city)
print("--------------------")
# dictionary listesi örneğidir.
pr=0
products=[
    {'name':'samsung 1','price':1500},
    {'name':'samsung 2','price':2500},
    {'name':'samsung 3','price':3500},
    {'name':'samsung 4','price':4500}
]
for product in products:
    for key,value in product.items(): 
        #print(key,value) # key-value çiftlerini yazdırır.
        if(type(value) == int):
            #if(value >= 3000):
            if((product['price']) >= 3000): # istenen key değerinin value' suna bu şekilde erişebiliriz.
                print(key,value)
            pr += value
print("pr:",pr)   

for product in products:
    if((product['price']) > 2500):
        print(product)