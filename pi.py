
e = 0 #for döngüsünde degerine kadar dönecek
hesapla = 1 # çarpım sonucu tutulacak altdizi[] nin çarpılması bu ifadeyle gerçekleşiyor.
altdizi = []  # altdizi listesi tanımlandı.

#Tüm altdizi degerine 0 degeri ver.
for k in range(0,16):
    altdizi.append(0)
#Altdizi uzunluğunu yazdır.
print("Altdizi uzunluğunuz:",len(altdizi))
print("Alt dizinin elemanları:",altdizi[0:100])

x = 0    # x her bir aralığın bağlangıç degeri .
y = 6    # y her bir aralğını son degeri. for dönügüsü x ve y degerine göre çalışacak.
z = 0    # for döngüsü için ilk deger atamsı yaptım.
min = 0
max = 0
f = 0

#dizi listesi ,pi sayisinin noktadan sonraki tüm degerini tutan liste
dizi= [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4,
             1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9,
             7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3,
             4, 2, 1, 1, 7]
print("Dizi nin elemanları:",dizi[0:len(dizi)])


for i in range(0,len(dizi)):

    if (i % 6 == 0):

        for z in range(x,y):
            hesapla*=dizi[z]
            altdizi[f]=hesapla  #altdizi ye ata

        x=x+6
        y=y+6
        f=f+1
        #tüm alt dizi eklenmeleri print olarak gözüksün.
        print("altdizi=", altdizi[0:100])
    #eger y de tasma varsa döngüyü kır.
    if( y > len(dizi)):
        break

    e=e+1
    hesapla=1

# karşılaştırma (min-max) için for döngüsü
for i in range(0,f,1):
    if (altdizi[i] < min):
        min=altdizi[i]



    if (altdizi[i] > max):
        max=altdizi[i]

#çıktı olarak min ve max i yazdir.
print("min degeri",min)
print("max degeri",max)
