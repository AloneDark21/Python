# Dunder(double under score) methodlari
# pythonda bir class tanimladigimiz zaman Dunder methodlar da o class için python tarafindan otomatik olarak tanimlanir

class Ucus() :
    havayolu = "THY" 

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu_sayisi, bilet_ucreti) : 
        self.kod = kod                                              
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu_sayisi = yolcu_sayisi
        self.bilet_ucreti = bilet_ucreti

    def __repr__(self) :
            return "{} kodlu {} -> {} seferi, sistemde olusturulmustur.".format(
                self.kod,
                self.kalkis,
                self.varis
                )
    
    def anons_yap(self) : 
        return "Degerli yolcularimiz hepiniz hosgeldiniz {} sefer sayili {} -> {} ucusumus {} dakika surecektir.".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure
        )  
    def kalan_koltuk_sayisi(self) :
        return self.kapasite - self.yolcu_sayisi
    
    def bilet_satisi(self, satilan_bilet_sayisi) :
        
        if self.yolcu_sayisi + satilan_bilet_sayisi <= self.kapasite :
            self.yolcu_sayisi += satilan_bilet_sayisi
            self.kalan_koltuk_sayisi()
            print("{} adet bilet satilmistir, kalan koltuk sayisi : {}".format(satilan_bilet_sayisi, self.kalan_koltuk_sayisi()))
        else :
            if self.kalan_koltuk_sayisi() == 0 :
                print("Seferde Bos Koltuk Bulunmamaktadir.")
            else : 
                print("Kalan koltuk sayisindan fazla bilet alamazsiniz. Kalan koltuk sayisi : ",self.kalan_koltuk_sayisi())  

    def bilet_iptali(self, iptal_edilen_bilet_sayisi) :
        if self.yolcu_sayisi >= iptal_edilen_bilet_sayisi : 
            self.yolcu_sayisi -= iptal_edilen_bilet_sayisi
            print("{} adet bilet iptal edilmiştir, kalan koltuk sayisi : {}".format(iptal_edilen_bilet_sayisi, self.kalan_koltuk_sayisi()))
        else :
           print("Toplam yolcu sayisindan fazla bilet iptal edemezsiniz.")   

ucus1 = Ucus("TK101", "BOD", "ANK", 40, 200, 150, 700)

# Represent (__repr__()) methodu kullanimi 
# class imizin icerisinde Represent methodunu olusturduk 
# __repr__() methodu kullanmadan direk print(ucus1) komutunu calistirirsak ucus1 objesinin memoryde tutuldugu yeri yazdirir
# __repr__() methodu kullandigimiz zaman ise print(ucus1) komutunu cagirdigimizda class ta olusturdugumuz __repr__() methodunda yapilacak islemi yapar

print(ucus1) # burda iste __repr__() methodunu cagiriyor

# __dir__() methodu ile olusturdugumuz objeye ve classa ait tüm attributeleri, fonksiyonlari ve dunder methotlarini yazdirdik
print("\nOlusturdugumuz Class ve Objeye ait tum attribute, fonksiyonlar ve Dunder methotlari : \n",ucus1.__dir__())
