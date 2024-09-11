isim='alper'
print('isim bilgisi {}'.format(isim)) #string veriyi yazdirir
soyisim='aksakal'
print('isim bilgisi{}{}'.format(isim,soyisim)) #birden fazla string veriyi yazdirir
a='naz'
b='tuncer'

print('isim bilgisi{1}{0}'.format(a,b)) #string veriyi istenilen sirada yazdirir
print('isim bilgisi{0}{1}'.format(a,b))

sayi=2/3

print('sonuc{r:1.3}'.format(r=sayi)) #r:1.3 teki 3 virgülden sonraki karakter sayisini gosterir

c='veri1'
d='veri2'

print(f'veriler 1.veri {c}, 2.veri {d}') #daha pratik bir yol verileri direkt olarak yazdirir.