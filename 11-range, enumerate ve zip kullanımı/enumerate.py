# enumerate bir listedeki elemanları index degerleriyle beraber yazdırır

harfler = ["a", "b", "c", "d"]

for harf in enumerate(harfler) : # kullanmak istedigimiz yere yazıp kullanabiliriz
    print(harf)

# index degerlerine ve elemanlara ayrı ayrı da ulaşabiliriz    
for index, harf in enumerate(harfler) :
    print("{}. Harf : {}".format(index+1,harf))   
