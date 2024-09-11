#bunlar en cok kullanilan metodlardir.

cumle='Benim adim Alper. Ben muhendisim.'
cumle1=cumle.upper() #hepsini buyuk harf yapar.
print(cumle1)
cumle2=cumle.lower() #hepsini kucuk harf yapar.
print(cumle2)
cumle3=cumle.title() #kelimelerin ilk harfleri buyuk olur.
print(cumle3)
cumle4=cumle.capitalize() #sadece cumlenin ilk harfi buyuk olur.
print(cumle4)
cumle5=cumle.strip() #eger cumlede bosluk karkteri varsa onlari siler.
print(cumle5)
cumle6=cumle.split() #cumle ogelerini dizi ogelerine ayirir.
print(cumle6)
cumle7=cumle.split('.') #noktali ogeleri ayirir.
print(cumle7)
cumle8='*'.join(cumle6) #ayrilan ogeleri birlestirir. arasina yildiz koyar, istenilen karakter koyulabilir.
print(cumle8)
indeks=cumle.find('Ahmet') #eger cumle icinde alper kelimesi varsa pozitif yoksa -1 degeri dondurur.
indeks2=cumle.find('haha')
print(indeks)
print(indeks2)
cumle9=cumle.replace('Ahmet','Alptekin')
print(cumle9)


