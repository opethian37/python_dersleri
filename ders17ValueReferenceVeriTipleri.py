#value veri tipleri -> string,float,integer

x=5
y=15

x=y
y=10 #y degeri degisse bile x hala ayni

print(x,y)

#reference veri tipleri -> list 

a=["elma","armut"]
b=["elma","armut"]

a=b #ikisi de ayni adrese konumlandiriliyor bu nedenle herhangi birinde bir degisiklik yapildiginde hepsi etkileniyor.

b[0]="uzum" #her iki listede de deger degisti

print(a,b)

