# burda classta method olusturup bu methodla class yapısında değişiklik yapabilmek
# ucus ile ilgili bilet satisi, bilet iptali ve kalan koltuk sayilarini bulmak için methodlar olusturacagiz

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

# kalan koltuk sayisini ogrenmek icin kalan_koltuk_sayisi() methodunu cagirmaliyiz
kalan_koltuk_sayisi = ucus1.kalan_koltuk_sayisi()
print("Kalan Koltuk Sayisi : ",kalan_koltuk_sayisi)

# bilet almak icin bilet_satisi() methodunu cagirmamiz gereklidir
ucus1.bilet_satisi(20)

#bilet iptali icin bilet_iptali() methodunu cagirmaliyiz
ucus1.bilet_iptali(50)
