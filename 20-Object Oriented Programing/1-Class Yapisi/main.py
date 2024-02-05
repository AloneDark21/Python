"""
class olusturma 

class <Class Ismi>():                            ***Class isminin buyuk harfle baslamasi tavsiye edilir 
    
    <class attribute>                            ***class a ait olan genel elemanlari icerir

    def __init__(self,<attribute>):              ***init, instantiation yani orneklendirmenin kisaltmasidir
        self.<instance attribute> = attribute    ***instance attribute lar, olusturulan objeye ozgudur
        .
        .
        .

    def <method>(self, <param>) :                ***methotlar class lara ozgu fonksiyonlardir
        .
        .
        .
        return ......
"""

# class yapisinde attribute kullanimi
from sympy import variations


class Ucus1() :
    havayolu = "THY" # class a ait attrribute dir
    
ucus1 = Ucus1() # classtaki attributeleri kullanmak icin ucus1 olusturduk
ucus1.havayolu # burdada olusturdugumuz ucus1 ile class taki attributeleri kullandik
print(ucus1.havayolu) # bu kullanimla THY yi ekrana yazdiriyoruz

# class ta __init__ kullanimi asagida gosterilmistir
# bir obje olusturdugumuz zaman init fonksiyonu içindeki class a ait olan ozellikleri kullanrak objeyi olusturmak icin kullanilir
class Ucus2() :
    havayolu = "THY" # class a ait attributedir 

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu_sayisi, bilet_ucreti) : # ucusa ait ozellikleri olusturduk, self ifadesi class yapisinde tanimlidir.
        self.kod = kod                                              # burdaki ozellikler olusturulacak objeye ozgu ozelliklerdir
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu_sayisi = yolcu_sayisi
        self.bilet_ucreti = bilet_ucreti
        
ucus2 = Ucus2("TK123", "ANK", "IST", 60, 300, 50, 1000) # class ozelliklerini kullanarak ucus2 objemizi olusturduk, bu sekilde classa ait ozelliklere ulasabiliriz
print(ucus2.kod)
print(ucus2.kalkis+" -> "+ucus2.varis)

ucus3 = Ucus2("TK101", "BOD", "ANK", 40, 200, 30, 700)
print(ucus3.kod)
print(ucus3.kalkis+" -> "+ucus3.varis)

# class ta method ve attribute kullanimi asagidaki gibidir
class Ucus4() :
    havayolu = "THY" # class a ait attributedir 

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu_sayisi, bilet_ucreti) : # ucusa ait ozellikleri olusturduk, self ifadesi class yapisinde tanimlidir.
        self.kod = kod                                              # burdaki ozellikler olusturulacak objeye ozgu ozelliklerdir
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu_sayisi = yolcu_sayisi
        self.bilet_ucreti = bilet_ucreti
    
    def anons_yap(self) : 
        return "Degerli yolcularimiz hepiniz hosgeldiniz {} sefer sayili {} -> {} ucusumus {} dakika surecektir.".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure
        )  
    
ucus4 = Ucus4("TK101", "BOD", "ANK", 40, 200, 30, 700)

print(ucus3.kod)
print(ucus3.kalkis+" -> "+ucus3.varis)
print(ucus4.anons_yap()) # burda class ta olusturdugumuz metodu cagirdik methotlarda olusturdugumuz her obje ozgudur
