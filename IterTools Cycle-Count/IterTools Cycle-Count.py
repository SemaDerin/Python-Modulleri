import itertools as itt
#ıtertoolsun iter kelimesi iterasyondan gelir.
#Şimdi itertooolsun CYCLE ve COUNT donksiyonlarina bakalım:


#CYCLE

data= ["A","B","C","D"]

for i in data:
    print(i)

#İtertoolsun CYCLE fonksiyonu döngünün sonsuza kadar dönmesini sağlar:
#Synyax ı şu şekilde :

c_data= itt.cycle(data)  #C_data nın  data verisinin itertoolsun.cycle methodunun içine verilmiş hali old.

#Önce bir tipini görüntüleyelim:
#print(type(c_data))  #<class 'itertools.cycle'>


#c_datayı döngüye sokarsak:

c_data= itt.cycle(data)
for i in c_data:    #Sonsuz bir abcd döngüsü:
    print(i)




#COUNT

#Elimizde data yoksa range methodu kullanırız.


for i in range(1, 10):
    print(i)


c1= itt.count(10,5)     #10 dan başlar ve beşer artar
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))    #10,15,20,25


