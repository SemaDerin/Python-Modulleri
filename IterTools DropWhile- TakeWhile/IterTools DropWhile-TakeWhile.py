import itertools as itt

#Dropwhile ve Takewhile methodları:

#Dropwhile kendisine verilen liste içinde döner ve dönerken yine içine tanımlı olan fonksiyon sonucunda false
#olan ilk değerden itibaren listenin geri kalan kısmını bulur. Kısaca ilk hatayı ayıklar.

data= [7,8,9,14,12,6,3,2,1,5,9,3]

r1 = itt.dropwhile(lambda  x: x>3 , data)  #x in 3 ten küçük olduğu değerden itibaren ekrana basar.
print(list(r1))



r2 = itt.takewhile(lambda y: y>3 ,data) #y nin 3 ten büyük olan tüm durumlarını yazdırırken küçük ya da eşit olduğu
                                        # anda durur.
print(list(r2))


#Takewhile ile dropwhile ın toplamı bize döngünün kendisini verir.
#dropwhile ilk sırada false göre boş değer döndürür.

data2= [5,4,7,9,3,6,7]
r3= itt.takewhile(lambda z: z<4, data2)
print(list(r3))



paswords= [ "123sd", "123ll","123gs","124al","123is"]

def p_filtesi(var):
    return "123" in var



r6 = itt.dropwhile( p_filtesi , paswords)
print(list(r6))




ogr_no=["18102","18103","18107", "20100","18145","18121"]

def ogr_no_f(num):
    return "181" in num


r7= itt.takewhile(ogr_no_f, ogr_no )
print(list(r7))