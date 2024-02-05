# rastgele degerler içeren bir liste olusturacaksınız ve bu listedeki string degerleri sadece filter ve lambda gibi komutlarla yapınız
# fonksiyon kullanarak yapınız ve str degerlerini return ediniz
# bu fonksiyon liste tipinde tek degisken alacak

# sadece fonksiyon kullanarak yapma
my_list = [1, "a", 3, 6, "f", "c", 9, "z"]
str_list = []
def str_filtrele2(my_list) :
    for x in my_list :
        if type(x) == str :
            str_list.append(x)
        else :
            pass
    print("Fonksiyon kullanilarak yapilan liste : ",str_list)

str_filtrele2(my_list)

# filter ve fonksiyon kullanarak yapma
def str_filtrele(x) :
    return x if type(x) == str else None        
filter_list2 = [*filter(str_filtrele,my_list)]  
print("\nfilter ve fonksiyon kullanilarak olusturulan liste : ",filter_list2)

# filter ve lambda kullanılarak olusturdugumuz liste fonksiyon kullanmadan
filter_list = [*filter(lambda x : x if type(x) == str else None, my_list)]
print("\nfilter ve lambda komutlari kullanarak olusturulan liste : ",filter_list)
