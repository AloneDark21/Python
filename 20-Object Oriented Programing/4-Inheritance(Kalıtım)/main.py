# inheritance(kalitim), super(ana) class, sub(alt) class, obje yaratmak ve statik deger yerine dinamik deger kullanma islemlerini yapacagiz

# super(ana) class olarak Seyahat classini olusturduk
class Seyehat() :
    def __init__(self, kalkis, varis,saat) :
        self.kalkis = kalkis
        self.varis = varis
        self.saat = saat

    def anaons(self) :
        return "{} -> {} Seyahatine Hosgeldiniz.".format(self.kalkis, self.varis) 
    
    def sefer_bilgileri(self):
           print("Kalkis : {}\nVaris : {}\nSaat : {}".format(self.kalkis,self.varis, self.saat))

# sub(alt) class olarak Otobus classini olusturduk    
class Otobus(Seyehat) :
    def __init__(self, kalkis, varis, otobus_tipi,saat) : #kalkis varis noktalarini burda olusturursak ststik tanimlamis olusur  
        super().__init__(kalkis, varis, saat)
        self.otobus_tipi = otobus_tipi

    def otobus_bilgileri(self):
        print("Otobus Tipi : {}".format(self.otobus_tipi))    

# burdada Tren sub(alt) classimizi olusturduk bu sekilde super class ile ilgili istedigimiz kadar sub(alt) class olusturabiliriz
class Tren(Seyehat):
    def __init__(self, kalkis, varis, tren_tipi, saat):
        super().__init__(kalkis, varis, saat)
        self.tren_tipi = tren_tipi

    def tren_bilgileri(self):
        print(f"Tren Tipi : {self.tren_tipi}")   
    

otobus = Otobus("ANK", "BOD", "Turistik Otobus", "15:00") # otobus class ina it attributeleri burda tanimlarsak dinamik olarak tanimlamis oluruz
print(otobus.anaons())
otobus.sefer_bilgileri()
otobus.otobus_bilgileri()
#print(otobus.anaons()) # burada anons methodu Seyahat classina ait iken inheritance sayesinde super(ana) classtaki methot ve attributeleri kullanabiliyoruz 

print("\n")
tren = Tren("DYB", "IST", "Hizli Tren","19:00") # tren classimizin attributelerini burda dinamik olarak tanimladik
print(tren.anaons())
tren.sefer_bilgileri()
tren.tren_bilgileri()
