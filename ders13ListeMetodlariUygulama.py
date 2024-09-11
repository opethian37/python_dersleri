isimler=['Ali','Yagmur','Hakan','Deniz']
yillar=[1998,2000,1998,1987]

#1 'cenk ismini liste sonuna ekleyiniz.
isimler.append('Cenk')
print(isimler)

#2 'sena ismini liste basina ekleyiniz.
isimler.insert(0,'Sena')
print(isimler)

#3 "Deniz" ismini listeden siliniz.
isimler.pop(4)
print(isimler)

#4 "Hakan" isminin indeksi nedir.
hakanIndeks=isimler.index('Hakan')
print(hakanIndeks)

#5 "Ali" listenin elemani midir?
aliVarmi='Ali' in isimler
print(aliVarmi)

#6 Liste elemanlarini tersten cevirin.
isimler.reverse()
print(isimler)

#7 Liste elemanlarini alfabetik olarak siralayin.
isimler.sort()
print(isimler)

#8 str="Chevrolet,Dacia" karakter dizisini listeye cevir.
str="Chevrolet,Dacia"
dizi1=str.split(',')
print(dizi1)

#9 yillar dizisinin en buyuk ve en kucuk karakterleri nelerdir?
yillarBuyuk=max(yillar)
yillarKucuk=min(yillar)
print(yillarKucuk,yillarBuyuk)

#10 yillar dizisinde kac tane 1998 degeri vardir?
adet=yillar.count(1998)
print(adet)

#11 yillar dizisinin tum elemanlarini siliniz.
yillar.clear()
print(yillar)

#12 kullanicidan aldiginiz 3 adet marka bilgisini bir listede saklayiniz.
print('1.markayi gir:')
veri1=input()
print('2.markayi gir:')
veri2=input()
print('3.markayi gir:')
veri3=input()
liste1=[veri1,veri2,veri3]
print(liste1)