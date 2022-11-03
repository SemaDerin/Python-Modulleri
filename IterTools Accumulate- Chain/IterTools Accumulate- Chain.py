import itertools as itt
#IterToolsun Accumulate ve Chain Fonksiyonlarını Göreceğiz:.:....

#Accumulate döngü içerisine soktuğu datadanın elemanlarını birbirinin üzerine yığarak ilerler:


data=[ 1,3,5,10]
a1= itt.accumulate(data)
#önce a1 in tipini görelim:

print(type(a1)) #<class 'itertools.accumulate'> Accumulate old. aşağıda list(a1) şeklinde bastırdık.(listeye çevirmek gerek)


print(list(a1))   #[1,4,9,19]

#Acummulate iki paremetre alır: Birincisi verisi ikincisi işlem özeti lambda (çıkarma da yaptırabilirz)

data2=[78,45,96,21]
a2=itt.accumulate(data2,(lambda p1,p2 : p1-p2))
print(list(a2))

#Aynı şekilde bölüm veya çarma da yapmak mümkündür:
#Bölme
data3=[256,128,64,32]
a3 = itt.accumulate(data3,(lambda b1,b2,: b1/b2))
print(list(a3))

#Çarpma

data4= [2,4,7,9]
a4=itt.accumulate(data3,(lambda c1,c2: c1*c2))
print(list(a4))

#CHAIN

#Chain fonksiyonu döngüye sokabileceğimiz her şeyi birleştirme imkanı  sağlar:

p1 = ["A","B","C","D"]
p2= [1, 2, 3, 4]
r1= itt.chain(p1,p2) #Büyük diziler olduğunda chain kullanmak daha iyidir.
print(list(r1))