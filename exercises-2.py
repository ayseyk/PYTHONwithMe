num=30 # değeri bloklar içinde de değiştirilebilir olsun istenirse değiştirileceği yerde global tanımlanmalıdır.

 def myFunc(number):
     """Sayıya 5 ekler"""
     global num
     num=5 #blok dışındaki değişkene erişilebiliyor ama değeri değiştirilemiyor.
     print("blok içindeki num: ",num)
     return number+5
 
 sayi=myFunc(3)
 print(num)

## tuple

# myTuple = (1,2,3)
# print(myTuple)
# # myTuple[0]=5 tupl elemanı değiştirilemez olan listeelrdir.
# #Tamamen tuple ın kendisini değiştirebiliyoruz.
# myTuple=(61,61)
# print(myTuple)
# =============================================================================

# =============================================================================
# #Is it a prime number or not?
# def asalBul(num):
#     if(num ==1):
#         return False
#     for i in range(2,num): # 2 3 ... num-1
#         if(number%i==0):
#             return False
#         else: return True
#             
# number=int(input("Enter an integer number: "))
# asalMi= asalBul(number)
# 
# if(asalMi):
#     print("The number is a prime number.")
# else: 
#     print("The number is not a prime number.")
#             
#     
# #faktöriyel hesabı    
# sayi = 5
# sonuc=1
# while(sayi>=1):
#     sonuc *=sayi    
#     sayi=sayi-1
#     
# print(sonuc)
# =============================================================================
            
            
            