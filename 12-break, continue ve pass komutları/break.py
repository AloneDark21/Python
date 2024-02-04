# break komutunu içinde bulundugumuz döngüden çıkmak için kullanırız

harfler = ["a", "b", "c", "d", "e"]

for index, harf in enumerate(harfler) :
    if harf == "c":
        print("{} harfi {} numarali indextedir".format(harf,index))
        break
    
