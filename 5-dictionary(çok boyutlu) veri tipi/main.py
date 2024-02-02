#dictionary veri tipi çok boyutlu verileri tutar
#çok boyutlu tekil objelerdir

dict1 = {"isim": "Kerem",
         "yas": 23,
         "lokasyon": "Ankara"}
print("\n1.Lokasyon : ",dict1)

#iç içe dictionarylerde olusturulabilir asagidaki gibi dict2 ve lokasyon 
dict2 = {"isim": "Kerem",
         "yas": 23,
         "lokasyon": {
             "dogdugu_sehir": "Diyarbakir",
             "yasadigi_sehir": "Ankara" 
         }
}
print("\n2.Lokasyon : ",dict2)

print("\nAdi : ",dict2["isim"])
print("\nYas : ",dict1["yas"]) #dictionary içerisinde istediğimiz veriye bakmak için kullandıgımız yapi
print("\nDogum Yeri : ",dict2["lokasyon"]["dogdugu_sehir"]) #iç içe dictionarylerde istedigimiz veriye ulasmak için kullandıgımız yapi

#veriye bir diger ulasim seklimiz get() fonksiyonu kullanmaktir
isim = dict2.get("isim")
print("\nAd : ",isim)

#iç içe lokayonlarda veriye get() fonksiyonu ile ulaşma seklimşiz
yasadigi_sehir = dict2.get("lokasyon").get("yasadigi_sehir")
print("\nYasadigi Sehir : ",yasadigi_sehir)

#keys() fonksiyonu lokasyondaki anahtar verilerini getirir
print(dict2.keys())

#values() fonksiyonu lokasyondaki anahtar verilerine karsi gelen verileri getirir
print(dict2.values()) 

#items() fonksiyonu lokasyondaki verileri satır satır yazma işlemini yapar
print(dict2.items())
