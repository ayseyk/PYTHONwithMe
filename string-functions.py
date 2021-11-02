print(10//3)   #3
print(-10//3)  #-4

# ** üs almadır.

a= "Ayse" 
s= "Seyma"
newString= a + s
print(newString)

#Değişken tanımlayınca mutlaka değer ataması yapmak gerekiyor.

#input fonksiyonu kullanıcıdan veri alır, string tipinde tutar.

alan=25
cevre=20
print("alan="+str(alan)+" çevre="+str(cevre))
#Aynı satırda bazı yazdırmaları yapacaksak tip dönüşümünden faydalanılır.

name= "Ayşe" #0 1 2 3 --- -4 -3 -2 -1 indekslemedir.

#stringdizisi[a:b]--> a dan b ye kadar, b dahil değil.
#stringdizisi[:b]--> baştan b ye kadar, b dahil değil.
#stringdizisi[a:b:2]--> a dan b ye kadar, 2şer 2şer.

surname="Ykaya"
age=21
print('My name is {} {} {}'.format(name,surname,age)) 
#format yöntemi kullanılarak tip dönüşümüne gerek kalmaz.

#fstring yöntemi de tip dönüşümü gerktirmez.
print(f'My name is {name} {surname} and my age is {age}')

print(name[::]+" "+name[::2]+" "+name[::-1]) #Ayşe Aş eşyA

again= name*5     #5 kez yan yana yazar.
print(again[::4]) #AAAAA, 2-->AşAşAş.. oluyor.

text=" hello world"
text1="hello.world"
#BAZI ÖZEL FONKSİYONLAR

result=name.upper() #Hepsini büyük harfe çevirir.
print(result)

result=text.title() #Her kelimenin baş harfini büyütür.
print(result)

result=text.strip() #Başta ve sonda bulunan boşluk karakterlerini siler.
print(result)

result=result.capitalize() #Sadece cümlenin ilk harfini büyütür.//ilk harf boşluk olduğu için bu sonuç üzerinden kullandım.
print(result)

result=text.split() #Verilen cümle boşluk karakterlerinden bölünür ve karakter dizisi olarak geri döner.
             #['hello','world']-->cümleyi parçalara ayırır.
print(result)   

result1=text1.split('.') #. dan itibaren ayırır.
print(result1)

result=' '.join(result) #Ayrılmış ifadeyi yeniden birleştirir.
print(result)

#result1='.'.join(result1) #Ayrılmış ifadeyi yeniden birleştirir.
# print(result1)

index=text.find('world') #Kelimeyi arar, bulduğu yerde ilk harfin indeksini döndürür.
                #Kelime cümlede yoksa -1 döndürür.
print(index) # hello w-->7. index w!, boşluk var başta.

isTrue=text.startswith('H') #text H ile başlıyorsa True döndürür.
print(isTrue) #False, çünkü boşluk ile başlıyor.

isTrue=text.endswith('d') #text d ile bitiyorsa True döndürür.
print(isTrue) #True

print(text)
result=text.replace('h','H') # soldakini bulduğu yere sağdakini yazar.
print(result)

print(name)
result=name.replace('e','E') # soldakini bulduğu yere sağdakini yazar.
print(result)

result=name.replace('A','a').replace('y','Y') #şeklinde ardışık da yazılabilir.
print(result)

result=text.center(50) #50 karakter içinde ortalıyor bizim metni.
print(result)

result=text.center(50,"*") #Metni ortalıyor boş kalanları sağdaki ile dolduruyor.
print(result)

"""upper()              strip()             startswitch()
   lower()              split()             endswitch()
   title()              join()              replace()
   capitalize()         find()              center()         """
   #strip()-->baştan-sondan boşluk siler.
   #split()-->verilen metin boşluk veya ilgili karakterden bölünür, karakter dizisi döner.
   #join()-->ayrılan metin birleştirilir. name=' '.join(name) gibi.
   #find()-->bulunan kelimenin başlangıç indexini döndürür.
   #start/endswitch-->ilgili karakter ile başlayıp bitme durumuna göre True-False döndürür.
   #replace('','')-->yazılan iki karakter/string yeri değiştirilir.
   #center()-->verilen değer kadar yer ayrılır ve metin ortalanır. virgülden sonra bir şey yazarsan kalan yerler o karakterle doldurulur.