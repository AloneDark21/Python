# try ve Except yapıları kodumuzda hata varsa o hataların önüne geçip sistemin devamm etmesi için kullanılır 

# round() komutu verdiğimiz degeri en yakın ondalık sayıya yuvarlamak için kullnılır
# print(round(1.7)) # 2 ye yuvarlar
# print(round(13.4)) # 13 e yuvarlar

# asagidaki fonksiyonu çalıştırmak istersek hata verir
# çünkü input ile veri aldıgımızda bu veriler ilk basta string olarak alınır
# round sadece sayısal islemleri yapar
# bu yüzden tip dönüsümü yapmamız gerekiyor
"""
def tam_sayiya_cevir() : 
    girdi = input("Bir ondalikli sayi giriniz : ")
    print("Yuvarlama islemi sonucu : ",(round(girdi)))

tam_sayiya_cevir()    

"""
# girdinin tip dönüşümü yapılmış hali asagidaki gibidir
"""
def tam_sayiya_cevir() : 
    girdi = input("Bir ondalikli sayi giriniz : ")
    print("Yuvarlama islemi sonucu : ",(round(float(girdi))))

tam_sayiya_cevir() 

"""
# Try kullanımı ve except kullanimi
# Try kodumuzda olusabilecek hataların test edildiği bloktur eger testi gecerse hata önlenirse excepte girmez hata önlenmezse excepte girer
# excepte oluşan hatayla iligili yaptırdıgımız işlemleri yapar kodun patlamasına engeldir kod hata vermeden çalışır 
# burda try ve except kullanmadıgımızda string bir deger girmemiz durumunda kod hata verir. 
# try ve except blokları koddaki hatayı engellmek için kullanılır
"""
def tam_sayiya_cevir() : 
    girdi = input("Bir ondalikli sayi giriniz : ")
    try : 
        girdi = float(girdi)
        print("Yuvarlama işlemi sonrasi girdi : {}".format(round(girdi)))

    except :
        print("{} girdisi ondalik tipe cevrilmiyor".format(girdi))

tam_sayiya_cevir() 

"""
# finally komutu kullanımı
# finaly komutu try ve excepteki aşamalar ne olursa olsun girilen bloktur
def tam_sayiya_cevir() : 
    girdi = input("Bir ondalikli sayi giriniz : ")
    status = ""
    try : 
        girdi = float(girdi)
        print("Yuvarlama işlemi sonrasi girdi : {}".format(round(girdi)))
        status = "Basarili"
    except :
        print("{} girdisi ondalik tipe cevrilemiyor".format(girdi))
        status = "Basarisiz"
    finally :
        print("Tam sayiya yuvarlama islemi {}.".format(status)) 

tam_sayiya_cevir() 
