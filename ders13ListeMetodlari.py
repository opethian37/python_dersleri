sayilar=[1,222,31,4,5]
harfler=['a','b','c','z','k']

minDeger1=min(sayilar) #liste izindeki minimum ögeyi bulur.
maxDeger1=max(harfler) #liste icindeki maksimum ögeyi bulur. karakter dizilerinde alfabetik olarak calisir.
print(minDeger1,maxDeger1)

sayilar.append(67) #liste sonuna eleman ekler.
print(sayilar)

sayilar.insert(3,37) #listenin belirlenen indeksine eleman ekler.
print(sayilar)

harfler.pop() #listenin en son elemanini siler
print(harfler)
harfler.pop(1) #1.indeksini siler.
print(harfler)

sayilar.sort() #listeyi kucukten buyuge siralar
print(sayilar)

print(sayilar.count(1)) #liste icinde ilgili elemanin kac adet oldugunu sayar
