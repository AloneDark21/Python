# .sort() komutu listeyi kucukten buyuge dogru sıralar
# bir fonksiyon olusturacaksiniz tek parametre alacak(sadece sayılardan oluşan liste tipinde) ve en buyuk iki sayıyı döndürecek biçimde olsun

def en_buyuk_iki_sayiyi_bul(my_list) :
    my_list.sort()
    print(my_list)
    return my_list[-1], my_list[-2]


my_list = [1,8,4,7,9,15,11,19]
en_buyuk_birinci , en_buyuk_ikinci = en_buyuk_iki_sayiyi_bul(my_list)

print("Dizideki en buyuk ilk iki sayi : ")
print(en_buyuk_birinci, en_buyuk_ikinci)
