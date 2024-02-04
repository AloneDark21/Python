"""
1- TypeError (tip hatasi)
print(5 + "a") 
üstteki yazdirma işleminde verilen hata TypeError: unsupported operand type(s) for +: 'int' and 'str'
int bir deger ile string bir ifade toplanmaz 

2- IndexError (index hatasi)
liste = [] bu listeden print(liste[4]) 4. indexteki degeri istersek index error hatasi verir

3- KeyError (anahtar kelime hatasi)
 
vatandas = {
    "Ad" : "Esma",
    "TC_NO" : 12361
}

print(vatandas["PASS_NO"]) 
burda KeyError hatasi aliriz çünkü vatandas dictionary sinde PASS_NO diye bir key yoktur

"""

# TypeError hatasını nasıl karsılarız
print("\nTypeError hatasi karsilama : ")
try :
    print(5 + "a") # normalde kodu çalıştırdığımızda burda hata verir # type: ignore
except IndexError : # bu sekilde daha fazla except tanımlayabiliriz, except hata_tipi : burda try calışmazsa hata tipi hangisiyse o blokta çalışır
    print("girilen verilerle islem yapilmiyor")
except :
    print("kod düzgün calismiyor")   

# IndexError hatasını nasıl karsılarız
print("\nIndexError hatasi karsilama : ")
liste = []    
try :
    liste[-1] # normalde kodu çalıştırdığımızda burda hata verir
except IndexError : # bu sekilde daha fazla except tanımlayabiliriz, except hata_tipi : burda try calışmazsa hata tipi hangisiyse o blokta çalışır
    print("Indexlemeye calistiginiz durum listede bulunmuyor.")
except :
    print("kod düzgün calismiyor")     

# KeyError hatasi karsilama  
print("\nKeyError hatasi karsilama : ")  
vatandas = {
    "Ad" : "Esma",
    "TC_NO" : 12361
}

try :
    vatandas["PASS_NO"]
except IndexError :
    print("Indexlemeye calistiginiz durum listede bulunmuyor.")
except KeyError :
    print("Aradiginiz anahtar degeri dictionaryde mecvut degil")
except :
    print("Kod Düzgün Çalismiyor")    

# bu sekilde kodların hata vermeden çalışmasının önüne geçtik
