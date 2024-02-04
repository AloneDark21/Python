# fonksiyonalrın birbirleriyle olan ilişkisi
# bir fonksiyon içerisinde diğer bir fonksiyonu cagirabiliriz

def buyuk_sayi_dondur(a,b) :
    if a > b :
       return a
    elif a < b:
       return b

def metin_yazdir(a,b) :
   buyuk_sayi = buyuk_sayi_dondur(a,b)
   sablon_metin = "{} daha büyüktür ".format(buyuk_sayi)
   print(sablon_metin)

metin_yazdir(15,35) 
# burda metin_yazdir fonksiyonuna sayilarımızı gönderdik
# metin_yazdir fonksiyonu kendi içerisinde buyuk_sayi_dondur fonksiyonuna bu sayıları gönderdi
# buyuk_sayi_dondur fonksiyonuda buyuk olan sayiyi metin_yazdir fonksiyonuna göndererek metini ekrana yazdırır 

print("\n")
# fonksiyonlar birden fazla sonuc döndürebilir
# split() komutuna herhangi bir argüman vermezsek verieln ifadeyi bosluklardan ayırır
def isim_soyisim_ayirma(isim_soyisim) : 
   isim = isim_soyisim.split()[0]
   soyisim = isim_soyisim.split()[1]
   return isim , soyisim

print(isim_soyisim_ayirma("Kerem Kara"))
ad , soyad = isim_soyisim_ayirma("Kerem Kara") # burda fonkiyondan gelen degerlere ayrı ayrıda ulasabiliriz
print(ad)
print(soyad)

# split() kullanarak ayırma yaptıgımız gibi verileri birleştirmekte mümkündür
# verieri " ".join([veri1, veri2]) bu sekilde birlestiririz
# burda çift tırnak içerisine ne yazarsak iki veri arasına onu koyar
# .join komutu sadece 2 veriyi birleştirmek için kullanılır 2 den fazla veri gönderirsek hata verir

def isim_soyisim_birlestir(isim, soyisim) :
   return " ".join([isim , soyisim])

print("Birlestirilmis Hali : ",isim_soyisim_birlestir("Sude", "Koç"))

# 2 den fazla veriyi birlestirmek için de *args komutunu kullanırız

def isim_soyisim_birlestir2(*args) : # *args burda liste yapısı görevini görüyor 
   return " ".join(args)

print("2 den fazla verinin birlestirilmis hali : ",isim_soyisim_birlestir2("Kerem","Kara", "Caymaz"))
        
# **kwargs argümanı kullanımı
# **kwargs ve *args argümanları genellikle veri sayısının belli olmadıgı yerlerde kullanılır
# **kwargs bir anahtar kelime görevini görür eger gönderilen listede belirlenen anahtar kelimeye karşılık varsa istenieln islemi yapar
# dictionary lerdeki key görevine karşılık geliyor yani

def meslek_yazdir(**kwargs) :
    if "Meslek" in kwargs : # "Meslek" burda bizim key verimizdir 
      print(kwargs["Meslek"])
    else :
       print("Meslek Bilgisi Mevut Degil.")

meslek_yazdir(Ad = "Mehmet", Soyad = "Çoban", Meslek = "Mühendis", Yas = 32)
# burda eger fonksiyona meslek bilgisini göndermeseydik ekrana meslek bilgisi mevcut degil yazdırırdı
# "Meslek" verisini  gönderdiğimizde **kwargs ta kontrol ediyoruz
# bu key("Meslek") degerine karşılık bir value degeri varsa gerekli işlemleri yaparız
