# map() komutu kullanımı
# map komutu verilen listenin her elemanına olusturdugumuz fonksiyondaki işlemi uygular

sayilar = [*range(1, 10)] # 1 den 10 kadar bir sayı listesi olustruduk

def karesini_al(x) : # kare alma fonksiyonunu olusturduk
   return x**2

print("Sayi Listemiz : ",sayilar)
map_list = [*map(karesini_al,sayilar)] # map ile sayıların karesini alıp yeni listeye attık 
print("\nmap() kullanimi Listesi : ",map_list) # karesi alınmış elemanların listesini yazdırdık

# filtre() komutu kullanımı

# filtre komutu listedeki filterelediğimiz elemanlara fonksiyondaki işlemi uygular

def cift_sayilari_filtrele(x) :
      return x if x % 2 == 0 else None # None hiçbir şey döndürme anlamındadır 
filter_list = [*filter(cift_sayilari_filtrele,sayilar)] # çift sayiları filtreledik ve yeni listeye attık
print("\nfilter() kullanimi Listesi : ",filter_list) # filtrelenmiş sayıların listesini yazdırdık

# lambda() komutu kullanımı

# lambda() yapacagımız islemi fonksiyon oluşturmadan(kullanmadan) yapar
# yapacagımız algoritmayı lambda() komutu içerisinde belirterek yapabiliriz
# map(lambda parametre : parametre_ile_yapilacak_islem, listemiz) kullanım seklimiz böyledir

lambda_list = [*map(lambda x : x**3, sayilar)] # fonksiyon kullanmadan sayiların küpünü aldık
print("\nlambda() nin map() ile kullanimi Listesi : ",lambda_list)
# hiçbir fonksiyojn kullanmadan sayilar listemizdeki tüm elemaların küpünü aldık

# lambda() map ve filtre işleminde de kullanılabilir

lambda_list2 = [*filter(lambda x : x if x % 2 != 0 else None, sayilar)] #tek sayiları filtreledik
print("\nlambda() nin filter() ile kullanimi Listesi : ",lambda_list2)
