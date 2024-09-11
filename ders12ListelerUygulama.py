#1 'bmw,mercedes,opel,mazda' elemanlarina sahip bir liste oluşturunuz.
liste1=['BMW','Mercedes','Opel','Mazda']

#2 liste kac elemanlidir?
elemanSayisi=len(liste1)
print(elemanSayisi)

#3 listenin ilk ve son elemani nedir?
ilkEleman=liste1[0]
soneleman=liste1[3]
print(ilkEleman,soneleman)

#4 Mazda yerine Toyota yazdirin.
liste2=liste1
liste2[3]='Toyota'
print(liste2)

#5 Mercedes listenin elemani midir?
mercedesVarmi='Mercedes' in liste1 #direkt olarka bu operator ile arama yapılabilir.
print(mercedesVarmi)

#6 listenin son 2 elemani yerine 'toyota ve 'renault' degerlerini ekleyin.
liste3=liste1[::]
liste3[-2]='Renault'
liste3[-1]='Toyota'
print(liste3)

#7 listenin üzerine 'audi' ve 'nissan'degerlerini ekleyin
liste4=liste3+['Audi','Nissan']
print(liste4)
print(len(liste4))

#8 listenin son elenanini silin
del liste1[-1]

#9 listeyi tersten yazdir
liste5=liste1[::-1]
print(liste5)

