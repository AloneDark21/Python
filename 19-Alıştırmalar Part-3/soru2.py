# bir fonksiyon olusturun, 2 parametre alsın üss alma islemi yapsın ve sonucu return olarak döndürsün
# ** kullanmadan for döngüsü kullanılarak yapılacak

def uss_alma(a,b) :
    sonuc = 1
    for i in range(b) :
        sonuc = sonuc * a
    return sonuc

taban = input("Taban degerini giriniz : ")
uss = input("uss degerini giriniz : ")
print("{} ^ {} = {}".format(taban,uss,uss_alma(int(taban),int(uss))))
