#Tqdm methodunun kullanımı:

#Önce Kütüphaneleri İmport etmekle işe başlayalım:

from time import sleep
from tqdm import tqdm

for i in tqdm(range(10)):   #tqdm methodu progessbar oluşturmak için döngüyle beraber kullanılan bir modüldür.
    sleep(0.5)
    

#from tqdm import tqdm,trange

for i in trange(10):    #trange tqdm içerisinde kısaltmak için kullanılmış bir methoddur.
     sleep(0.5)


for i in tqdm(range(10), unit= " website", colour= "#00ff00", desc= "Website işleniyor"):
    sleep(0.9)   #tqdm içerisinde tanımlı bazı özellikler vardır. CNTRL+CLCK (tqdm)


websites= ["http://www.trendyol.com", "http://www.bebuweb.com","http://gittigidiyor.com"]

bar= tqdm(websites ,unit = " website", colour = "#00ff00")
for i in bar:
    bar.set_description("Http isteği atılıyor {}".format(i))
    sleep(2)


with tqdm(total=50) as bar:
    for i in range(5):
        sleep(0.5)    #Bar ayarını manuel olarak düzenleyebiliriz.
        bar.update(2)

