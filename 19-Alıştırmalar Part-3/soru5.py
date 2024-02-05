# sadece sayı tipinde bir listemiz olacak bu listedeki elemanlardan 6 sıfır atılıp döndürülecek
# fonksiyon kullanılacak ve tek parametre alacak

# sadece fonksiyon kullanilarak yapilan islem
my_list = [1000000, 45000000,12000000,5000000]
new_list = []

def sifirlari_sil(my_list) :
    for i in my_list :
        new_list.append(int(i/1000000))

    print("Sadece fonskiyon kullanilarak olusturulan liste : ",new_list) 

sifirlari_sil(my_list)

# map ve fonksiyon kullanilarak yapılan islem
def alti_sifir_at(x) :
    return int(x / 1000000)

sifir_atilmis_list = [*map(alti_sifir_at, my_list)]
print("\nmap komutu ve fonksiyon kullanilarak yapilan liste : ",sifir_atilmis_list)

# map ve lambda kulanimi fonksiyon kullanmadan
sifir_atilmis_list2 = [*map(lambda x : int(x/1000000), my_list)]
print("\nmap ve lambda kullanilarak yapilan liste : ",sifir_atilmis_list2)

