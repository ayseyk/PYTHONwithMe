sisters={'ayşe','şeyma'}
print(sisters)

sisters.update(['feyza','zümra'])
print(sisters)
sisters.add('azra')
print(sisters)

x,y,z= 1,2,3 # tek satırda birden fazla atama
print(x,y,z)

a=(x+y+z)%3
print(a)

number1=input("enter a number: ")
number2=input("enter a number: ")
isbigger = (number1>number2)
print(f" {number1} sayısı {number2} sayısından büyüktür: {isbigger}")

num=int(input("number:"))
result= (0 < num < 100)
# print(f"Girilen sayı 0 ve 100 arasındadır :{result}")
result= (num > 0) and (num % 2 == 0) # True or False döndürür.
print(f"Girilen sayı pozifif bir çift sayıdır: {result}")

print('e' in 'ayşe') # True