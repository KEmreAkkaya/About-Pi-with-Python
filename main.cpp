e = 0
hesapla = 1
altdizi = []
for k in range(0,100):
    altdizi.append(0)

print("Altdizi uzunluğunuz:",len(altdizi))
print("Alt dizinin elemanları:",altdizi[0:100])

x = 0
y = 6
z = 0
min = 0
max = 0



dizi= [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4,
             1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9,
             7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3,
             4, 2, 1, 1, 7]
print("Dizi nin elemanları:",dizi[0:len(dizi)])
for i in range(0,len(dizi)):

    if (i % 6 == 0):
        for z in range(x,y):
            hesapla*=dizi[z]
            altdizi[z]=hesapla  #altdizi

        x=x+6
        y=y+6
    if( y > len(dizi)):
        break
   
    e=e+1
    hesapla=1

for i in range(0,e,1):
    if (altdizi[i] < min):
        min=altdizi[i]



    if (altdizi[i] > max):
        max=altdizi[i]


print("min degeri",min)
print("max degeri",max)

