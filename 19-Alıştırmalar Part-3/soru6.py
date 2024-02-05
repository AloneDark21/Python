# fonksiyon kullanin, fonksiyonda kullanicidan saat ve dakika degerlerini alarak döndürün
# kullanici girdisi onaylama islemi

def zaman_veris_al() :
    saat = input("saati giriniz : ")
    if saat.isdigit() :
        saat = int(saat)
        if (saat >= 0 and saat <= 23) :
            dakika = input("dakikayi giriniz : ")
            if dakika.isdigit() :
                dakika = int(dakika)
                if (dakika >= 0 and dakika <= 59) :
                    return "Girilen saat {}:{} ".format(saat,dakika)
                else :
                    print("Girilen dakika araligi yanlis")
            else :
                print("Girilen dakika yanlis veri tipinde")
        else :
             print("Girilen saat araligi yanlis")
    else :
         print("Girilen saat yanlis veri tipinde")         

print(zaman_veris_al())         
