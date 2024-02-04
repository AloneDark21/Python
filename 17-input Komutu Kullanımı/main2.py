# burda kullanıcı girdisini onaylayan sistem olusturduk
# girdi dogrusu ise sistem sonlanır 
# hatalı giriş hakkınız 3 tür. 3 hatalı giriş yaparsanız sistem kilitlenir
def sayi_girdisi_kontrol() :
    girdi = input("Bir sayi giriniz : ")

    if girdi.isdigit() :
        print("Teşekkürler Girdiniz int tipindedir")
    else :
        print("Lutfen int tipinde deger deger giriniz")

#sayi_girdisi_kontrol()


def sayi_girdisi_kontrol_dongu() : 
    girdi = input("Bir sayi giriniz : ")
    hatali_giris_hakki = 3

    while not girdi.isdigit() : 
        hatali_giris_hakki -= 1
        print("Kalan giris hakkiniz : ",hatali_giris_hakki)
        if hatali_giris_hakki == 0 :
            print("Cok fazla hatali giris yaptiniz sistem kilitlendi.")
            break
        print("Lutfen int tipinde deger giriniz")
        girdi = input("Bir sayi giriniz : ")
    else :
        print("Teşekkürler Girdiniz int tipindedir")  

sayi_girdisi_kontrol_dongu()
