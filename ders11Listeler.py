mesaj='Merhabalar. Benim adim Ahmet.'
mesaj2=mesaj.split() #ögelere ayirarak liste yapti.
print(mesaj2)
print(mesaj2[0])

liste1=['alper',2]
liste2=[4,5]
liste3=liste1+liste2 #listeler direkt olarak böyle eklenebilir.
print(liste3)

print(len(liste3)) #liste uzunlugu bulundu

liste4=[liste1,liste2]
print(liste4)
print(liste4[0][1])