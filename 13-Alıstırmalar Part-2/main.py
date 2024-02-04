kullanici1 = {
    "Ad" : "Kerem",
    "Soyad" : "Karaçoban",
    "Uzmanlik" : ["Backend", "Data Sinces"] 
}
kullanici2 = {
    "Ad" : "Melis",
    "Soyad" : "Çakan",
    "Uzmanlik" : ["Frontend"] 
}
kullanici3 = {
    "Ad" : "Duru",
    "Soyad" : "Isik",
    "Uzmanlik" : ["Backend"] 
}
# yukarıdaki bilgileri kullanarak aşagidaki soruları yanıtlayınız

# soru-1 Melis Çakan in uzmanlik alanini yazdırın
print("********* SORU-1 **********")
print("Melis Çakan in uzmanlik alani : ")
print(kullanici2.get("Uzmanlik"))
print(kullanici2["Uzmanlik"])

# soru-2 uzmanlik alani Backend olan kullanicilari yazdır
print("\n********* SORU-2 **********")
print("Uzmanlik alaninda Backend olan kullanicilar : ")

kullanici_listesi = [kullanici1, kullanici2, kullanici3]
for kullanici in kullanici_listesi :
    if "Backend" in kullanici["Uzmanlik"] :
        print(kullanici)

# soru-3 Duru Çakan Frontend ögrendi, uzmanlık bilgilerini güncelleyiniz
print("\n********* SORU-3 **********")
print("Kullanici uzmanlik alanina Frontend eklendi : ")
kullanici3["Uzmanlik"].append("Frontend")
print(kullanici3)

# soru-4 birden fazla uzmanlık alanı olan kullanıcıları listeleyiniz
print("\n********* SORU-4 **********")
print("Birden fazla uzmanlik alani olan kullanicilar : ")
for kullanici in kullanici_listesi :
    if len(kullanici["Uzmanlik"]) > 1 :
        print(kullanici)

# soru-5 asagidaki yas listesini zip kullanarak kullanıcılar listesi ile ilişkilendirip yasi 30 dan kucuk olan kullanıcıları yazdırın
print("\n********* SORU-5 **********")
print("Yasi 30 dan kucuk olan kullanicilar : ")
kullanici_yas_list = [30, 24, 27]

for kullanici, yas in zip(kullanici_listesi,kullanici_yas_list) :
    if  yas < 30 :
        print(kullanici, "Yasi : {}".format(yas))
