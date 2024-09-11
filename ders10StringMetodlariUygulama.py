website="www.facebook.com"
kurs="Python Kursu"

#' Hello World ' karkater dizisinin bas ve son bosluklarini silin.
cumle='Hello World'
cumle=cumle.strip()
print(cumle)

#2 website icinde facebook haric digerlerini silin
website2=website.strip('w.com')
print(website2)

#3 kurs degiskeni icindeki tum karakterleri kucuk yap.
kurs2=kurs.lower()
print(kurs2)

#4 website icinde kac tane a harfi vardir?
website3=website.count('a')
print(website3)

#5 website www ile baslayip .com ile bitiyor mu?
website4=website.startswith('www')
website5=website.endswith('com')
print(website4,website5)

#6 website icinde .com ifadesi var mi?
website6=website.find('.com')
print(website6)

#7 'icerik' kelimesini 50 karaktere yerlestir ve kenarlara ** koy
kelime='icerik'
kelime=kelime.center(50,'*')
print(kelime)

#8 kurs karakter dizisindeki bosluk karakterini '-' ile degistirin.
kurs3=kurs.replace(' ','-')
print(kurs3)

#9 'Hello World' kelimesindeki 'world' kelimesi yerine 'there' kelimesini koy.
kelime2='Hello World'
kelime2=kelime2.replace('World','There')
print(kelime2)









