#  burda da time ile ilgilenecegiz

from datetime import time
import datetime

# bir zaman olusturma icin time() komutunu kullanırız
zaman = time(6, 11, 1) # verdigimiz parametreler saat, dakika, saniye : 06:11:01 yazdiracaktir
print(zaman)

# saat, dakika, saniye degerlerine manuel olarakta ulasabiliriz

print(zaman.hour)
print(zaman.minute)
print(zaman.second)

# hem tarih hemde zamanı aynı anda almak için datetime() komutu kullanılır
dt = datetime.datetime(2024, 2, 11, 8, 30, 45)
print(dt)

# zaman ve dakikada oldugu gibi burda da datetime degerlerine ayrı ayrı ulasabiliriz
print(dt.date())
print(dt.day)
print(dt.ctime())# bu komut ile tarih ve saat bilgisine ekrana duzgun bir sekilde basabiliriz

# time ile gercek zamanı almak
# yukarıda datetime içerisinden time modulunu import etmiştik bu modul ile gerçek zamanı bulamayiz
# gercek zamani bulmak icin direkt olarak time ' ı import etmeliyiz

import time # time ' ı import ettik

print(time.ctime())# time.ctime() ile sistemin suanki zamanina ulasabilriz

baslangic_zamani = time.time()
print("Baslama Zamani : ",baslangic_zamani)
time.sleep(5) # time.sleep() komutu ile sistemi istedigmiz sure kadar uyutabiliriz
bitis_zamani = time.time()
print("Bitis Zamani : ",bitis_zamani)
time.sleep(5)

print("Çalisma Suresi : ",bitis_zamani - baslangic_zamani)

