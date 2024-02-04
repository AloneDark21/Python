# bir fonksiyon olusturun, 2 parametre alsın(uss ve taban), üss alma islemi yapsın ve sonucu return olarak döndürsün

def uss_alma(a,b) :
    return a**b
taban = input("Taban degerini giriniz : ")
uss = input("Uss degerini giriniz : ")

print("{} ^ {} : {}".format(taban,uss,uss_alma(int(taban),int(uss))))
