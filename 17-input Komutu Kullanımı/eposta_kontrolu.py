# girilen epostanin hatalimi dogru mu oldugunu bulan program

def eposta_kontrolu() :
    eposta = "ahmet01@edu.tr"
    girdi_epostasi = input("Lutfen eposta adresinizi giriniz : ")
    hatali_giris_hakki = 3

    while not girdi_epostasi == eposta :
        hatali_giris_hakki -= 1

        if hatali_giris_hakki == 0 :
            print("Giris hakkiniz kalmadi 1 saat sonra tekrar deneyiniz.")
            break
        print("Epostaniz hatalidir lutfen tekrar deneyiniz ")
        print("Kalan giris hakki sayiniz : ",hatali_giris_hakki)
        girdi_epostasi = input("Lutfen gecerli bir eposta adresi giriniz : ")
    else :
        print("Giriş işlemi basarili.") 

eposta_kontrolu()    
