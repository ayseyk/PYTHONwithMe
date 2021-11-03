# numbers=[1,3,5,7,9,12,19,21]

# # i=0
# # while i<len(numbers):
# #     print(numbers[i])
# #     i+=1

# first=int(input("Enter a number:"))
# last=int(input("Enter a number:"))
# i=0
# i=first
# while (i<=last):
#     if(numbers[i]%2==1):
#         print(numbers[i])
#     i+=1     

# i=100
# while i>=0:
#     print(i)
#     i-=1
number=[0,0,0,0,0]
i=0
while (i<5):
    number[i]= int(input("enter a number: ")) #number=diye alıp alt satırda ;
    i+=1              #numbers.append(number) şeklinde 0 atanmamış diziye eleman ekleyebiliyoruz.

print(number)

number.sort()
  
print(number)
