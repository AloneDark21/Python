# zip kullanımı
# zip iki farklı listeyi birbirleriyle ilişkilendirir
# eger listelerin eleman sayilari esit degil ise eleman sayısı az olan listyeye göre zipleme yapar

kullanici = ["Kerem", "Melis", "Asli"]
yas = [23, 21, 24]

for kullanicilar in zip(kullanici,yas) :
    print(kullanicilar)

# zip yaptıgımızda iki listenin elemanlarına ayrı ayrı da ulasabiliriz 
    kullanici_numarasi = 0
for kullanici, yas in zip(kullanici,yas) :
    print("{}. Kullanicinin Adi : {}\tYasi : {}".format(kullanici_numarasi+1,kullanici,yas))   

# \t 1 tab bosluk bırakmak için, \n ise bir alt satıra gecmek icin kulanılır    
