# name=input("name: ")
# age= int(input("age: "))
# education= input("education: ")

# if ((education=='highSchool') or (education== 'university' )) and (age>18):
#     print("you can take a driver licance")
# else:
#     print("you can't take a driver lisance")

# import datetime

# doğum=datetime.datetime(1976,8,10)
# simdi=datetime.datetime.now()
# result=simdi-doğum
# print(result.days)

# email= 'someone@gmail.com'
# password= '123'

# if(input('email: ')==email):
#     if(input('password: ')==password):
#         print('WELCOME')
#     else:
#         print('WRONG PASSWORD!')
# else:
#     print('WRONG USERNAME!')            

a= int(input('a: '))
b= int(input('b: '))
c= int(input('c: '))

if((a>b) and (a>c)):
    if(b>c):
        print(f'{a} > {b} > {c}')    
    else:
        print(f'{a} > {c} > {b}') 

elif((c>a) and (c>b)):
    if(b>a):
        print(f'{c} > {b} > {a}')    
    else:
        print(f'{c} > {a} > {b}')   

elif((b>a) and (b>c)):
    if(a>c):
        print(f'{b} > {a} > {c}')    
    else:
        print(f'{b} > {c} > {a}') 