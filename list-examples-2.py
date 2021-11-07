names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

names.append('Cenk')
names.insert(0,'Sena')
names.remove('Deniz')
names.reverse()
names.sort()
years.sort()


a=years.count(1998)
#years.clear()
min= min(years)
max= max(years)
print(max,min)


str="ford, dacia"
result=str.split(',') #string ifadeyi listeye çeviriyoruz.

markalar=[]
marka=input("marka:")
markalar.append(marka)
print(markalar)

print(result)
print(a)

print(names)
print(years)

# text= '25'.isdigit()
# print(text)

# message="do something now. ı say for you."
# result= message.replace(' ','*',2)
# print(result)

# userA=['ayşe',21]
# userB=['şeyma',17]
# users=[userA,userB]
# result=users[0][1]

#  mylist = [1,2,3,4,5]

# result=mylist[0::2]
# result=mylist[-2:]

# result=(60+70+70)//3

cars= ["ay","by","cy"]
cars.insert(-1,"car")
print(cars)

print(len(cars))