"""
Fonksiyon yapisi

def <fonksiyon_ismi>(<argümanlar>) : # snaek case
    .....

    <bu kod ne işe yarar>            # docstring

    .....

    .....                            # return / print   

"""
# def tanıtmak anlamına gelir 
# fonksiyona isim verirken fonksiyonun işleyişi ile ilgili isimler kullanılmasi daha faydali olacaktır

def bes_bastir() : # fonksiyonu olusturduk
    print(5)

bes_bastir() # fonksiyonun çalışması için fonksiyon olusturulduktan sonra çagırmamız gerekli 

# return ve print farkı : fonksiyonda ekrana bisey yazdırmak icin print , geriye bir deger döndürmek için return kullanırız
def bes_dondur() :
    return 5 # return kullandık fonksiyon 5 degerini fonksiyonu çagırdıgımız yere geri döndürecektir

a = bes_dondur() # fonksiyondan 5 degeri geldi ve a değişkenine atatık burda print ve return farkı net bir şekilde orataya çıkmaktadır
print(a)

# fonksiyonlarda argümanlar
def sayi_dondur(sayi) :
    return sayi

print(sayi_dondur(20)) # fonksiyona 20 sayisini gönderdik fonksiyon bu sayisi tekrar gönderip ekrana yazdırmamızı sagladı

def sayi_dondur(sayi = 50) : # default parametreler
    return sayi

print(sayi_dondur()) # fonksiyona deger göndermememize ragmen parametre almış bu tür patrametrelere default parametereler denir


# ornek

def buyk_sayi_dondur(a,b) :
    if a > b :
        return a
    elif b > a :
        return b
    
print(buyk_sayi_dondur(30,15)) # fonksiyona 2 deger gönderiyoruz fonksiyonda bize buyuk olan degeri geri döndürüyor
