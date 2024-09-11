# ogrencilerin numaralarina gore sozluk olusturulur. 
# 1.yöntem

ogrenciler={}

ogrenciNo1=input("ogrenci numarasi: ")
ogrenciIsim1=input("ogrenci adi: ")
ogrenciSoyisim1=input("ogrenci soyismi: ")
ogrenciTelefon1=input("ogrenci telefonu: ")

ogrenciler[ogrenciNo1]={
    'isim':ogrenciIsim1, 'soyisim':ogrenciSoyisim1,'telefon':ogrenciTelefon1
}

print(ogrenciler)

#2.yöntem

ogrenciler2={}

ogrenciNo2=input("ogrenci numarasi: ")
ogrenciIsim2=input("ogrenci adi: ")
ogrenciSoyisim2=input("ogrenci soyismi: ")
ogrenciTelefon2=input("ogrenci telefonu: ")

ogrenciler2.update({
    ogrenciNo2:{
        'isim':ogrenciIsim2,'soyisim':ogrenciSoyisim2,'ogrenci telefonu':ogrenciTelefon2
    }
})
print(ogrenciler2)

#uygulama// kullanicidan arac ozelliklerini alip sozluk icine atiniz.

aracBilgileri={}
aracModeli=input("arac modelini giriniz: ")
aracYasi=input("arac yasini giriniz: ")
aracKm=input("arac km sini giriniz: ")

aracBilgileri.update({
    aracModeli:{"arac modeli:":aracModeli,"arac yasi:":aracYasi,"arac km si:":aracKm}
})

print(aracBilgileri)


