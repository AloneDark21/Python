
str1 = "Kerem Çakir"

# i harfini index kullanmadan döndür
print(str1[9])

# i harfinin konumunu index komutu kullanrak bulalım 
print(str1.index("i"))

# upper() ve lower() fonksiyonlarının kullanimi
print(str1.upper())
print(str1.lower())

# splint() komutunu başka bir parametre ile kullan
print(str1.split(sep="e", maxsplit=2)) # e harlerinde stringi ayır maxsplit 2 defa ayırmak için kullanıldı

# list ve set kullanımı
liste = [1, "a", 2, 3, True, 4, 5, "True", "1"]

# listenin son elemanını nasıl buluruz 
print(liste[-1])

# listenin 2. ve 4. elemanlarını içeren yeni bir liste oluştur
print(liste[2:6:3])

# listeyi metot kullanarak ters çevirme
liste.reverse()
print(liste)

# listeyi metot kullanmadan ters çevirme
print(liste[::-1])

# iç içe liste kullanımı
iç_içe_liste = [1, 2, 3,[4,5]]

# listede 5 eleamnına nasıl ulaşabiliriz
print(iç_içe_liste[3][1])
print(iç_içe_liste[-1][-1])
print(iç_içe_liste[-1][1])
print(iç_içe_liste[3][-1])

# iç içe listedeki son elemanı çıkartıp yeni bir listeye ekleme
yeni_liste = iç_içe_liste.pop()
print(yeni_liste)

# pop() komutu kullanmayarak listeden 3 elemanını nasıl çıkartırız
iç_içe_liste = [1, 2, 3,[4,5]]

new_list = iç_içe_liste[:2] + [iç_içe_liste[-1]]
print(new_list)

# dictionary kullanımı
# dictionary ve liste arasındaki fark dictionaryde sıranın önemi yoktur, çok boyutlu elemanlardır. listeler koleksiyondur
# dictionary de key ve value anahatar kelimeleri kullanılır

my_dict = {
    "Isim" : "Kerem",
    "Yas" : 23,
    "Lokasyon" : {"Yasadigi_sehir": "Ankara", "Dogdugu_sehie":"Diyarbakir"}
}

# dictionaryde 23 degerine nasıl ulaşırım
print(my_dict.get("Yas"))
print(my_dict["Yas"])

# isim anahtarına karsılık gelen degeri kendi isminizle degistirin
my_dict["Isim"] = "Sila"
print(my_dict)

# my_dict değişkenindeki Ankara degerine nasıl ulaşırım
print(my_dict["Lokasyon"]["Yasadigi_sehir"])

# my_dict degiskeninde tüm anahtar(key) ve kelimelere(values) ulaşma
print(my_dict.keys())
print(my_dict.values())

# tuple ile liste arasındaki fark tuple immutable yani degisime acık değildir

