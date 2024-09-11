websitesi="www.facebook.com"
kurs="python kursu"

#1 kus karakter dizisinde kaç karakter var?
karakterSayisi=len(kurs)
print(karakterSayisi)

#2 websitesi icinden .com karakterlerini alın
websitesiDizi=websitesi[0:12]
print(websitesiDizi)

#3 kurs icindeki karakterleri tersten yazdirin
kursDizi2=kurs[::-1] # :: ifadesi dizinin bütün ögelerini alur. -1 ise tersten alır 1 ise normal alır
print(kursDizi2)

isim, soyisim, yas, meslek='ahmet','yilmaz', 28, 'muhendis'

#1 bilgileri anlamli sekilde yazdir
cumle=f"benim adim {isim}, soyadim{soyisim}, yasim {yas}, meslegim {meslek}" # f yazarak string degiskenler ekrana basilir.
print(cumle)

#2 'Hello world' string i icindeki w yerine W yazdir.
cumle2='Hello world'
cumle2.replace('w','a')
print(cumle2)

#3 'abc' ifadesini 3 kere yazdir
kelime='abc'
kelime2=kelime*3
print(kelime2)