# burda sadece Counter kütüphanesiyle ugrasacagiz
#Counter sayaç anlamına gelir

from collections import Counter # collections kutuphanesinde Counter objesini import ettik
import random

# 4 tane liste olusturduk rastgele
list1 = random.sample(range(10), k = 4)
list2 = random.sample(range(10), k = 4)
list3 = random.sample(range(10), k = 4)
list4 = random.sample(range(10), k = 4)

liste_list = [list1, list2, list3, list4] # burda tum listeleri bir listeye attik 
list_top = list1 + list2 + list3 + list4 # burda tum liste elemanlarini toplu bir sekilde gormek için hepsini topladik

print("\n",list_top) # toplam listeyi yazdirdik 
print("\n",liste_list) # tum listeleri liste halinde yazdirdik

print("\n")
# for kullanarakta buı listeleri farklı bir sekilde yazmayi denedik
for index, liste in enumerate(liste_list) : 
    print("{}. liste \t {}".format(index+1, liste))
    
print("\n",Counter(list_top) ) # burda counter kullandik 
# counter kullanarak listedeki elemanların hangisinden kaç tane varsa onlari yazdirdi

# mesela Counter ile string bir ifade de geçen her harfin kaç defa kullanildigini bulalim
print("\n",Counter("lgsoilhfsioljlj"))

# mesela burda bi sarki sozune Counter uygulayalim
sarki = """
Yine bana gel
Karanlik sokaklar içinden koşarak
yine bana gel
Korku yok gözümde 
"""
# yukaridaki kullanim sekli pythonun bize sundugu kolayliklardandir
# çok satırlı bir yaziyi """ """ bu sekilde tırnak içerisine alarak bire değişkene atayabiliriz

print(sarki) # burda sarki degiskenini olusturdugumuz sekilde ekrana basariz

print("\nHarflere ve Karakterlere Counter Uyguladik : \n",Counter(sarki))# bu sekilde sarki ya direk counter uygularsak harf ve karakter bazında sayim yapar
# kelime bazında da sayim yapabiliriz
# split() komutu ile sarki degiskenimizdeki tum kelimeleri ayrı ayrı ele alıp counter uygulayalim

print("\nKelimelere Counter Uyguladik : \n",Counter(sarki.split())) 

# Counter ayni harflerden biri buyuk biri kucuk ise bunlari farkli harf olarak algilar 
# mesela sarki sozunde gecen Yine kelimesinin 3. satirda kucuk harfle baslamis counter bunlari farklı kelimeler olarak algiliyor
# bunun onune gecebilmek icin tum harfleri ya buyuk ya da kucuk yapalim
# tum harfleri kucuk yaparak Counter uygulayalım
# tum harfleri kucuk yapmak icin lower() komutunu kullaniriz
print("\nTum Harfleri Kucuk Yaptiktan Sonra Counter Uygulama : \n",Counter(sarki.lower().split()))

# Counter ile kullanılan bir başka komut ise most_common() komutudur
# most_common komutu en sık karsilasilan anlamina gelir
# bir listeye uyguladigimizda listede en fazla tekrar eden kelimelri, harfleri, karakterleri bulabiliriz

print("\n most_common Kullanimi : \n",Counter(sarki.lower().split()).most_common(3))# burda most_common(3) dedik sarki sozleri icerisinde en fazla tekrar eden 3 kelimeyi bulmak için kullandik
# most_common() parantez iceisine istedigimiz parametreyi verebiliriz. Ornek : 1 , 2 ,3 ....
