"""
kullanim yapisi

for <degisken> in <iterable> :
    <burda istenileni yap>

"""
yorum_yapanlar = ["Kerem Çakir", "Sila Tutal", "Ahmet Kara", "Asli Koç", "Alparslan Degirmenci"]

# liste elemanlarini ekrana yazdırdık
for kullanici in yorum_yapanlar :
    print(kullanici)

# Sıra numarasiyla ekrana yazdirdik
kullanici_sayisi = 0

for kullanici in yorum_yapanlar :
    kullanici_sayisi += 1
    print("{}. kullanici : {}".format(kullanici_sayisi,kullanici))

# split() metodu kullanarak ekrana yazalım
kullanici_sayisi = 0    

for kullanici in yorum_yapanlar :
    kullanici_sayisi += 1
    ad = kullanici.split()[0]
    soyad = kullanici.split()[1]
    print("\n{}. kullanicinin \nAdi : {}\nSoyadi : {}".format(kullanici_sayisi,ad,soyad))

# asagida moderatorler olacak ve moderatörler moderatör_list e kullanicilar kullanici_list e eklenecektir
moderator_list = []
kullanici_list = []
moderatör1 = "Asli Koç"
moderatör2 = "Alparslan Degirmenci"

for kullanici in yorum_yapanlar :
    if kullanici in yorum_yapanlar and (kullanici == moderatör1 or kullanici == moderatör2) :
        moderator_list.append(kullanici)
    else :
        kullanici_list.append(kullanici)
    
print("Moderatör Listesi : {}".format(moderator_list))
print("Kullanici Listesi : {}".format(kullanici_list))    
