str = "Kerem"
print(str)
print(str[3:]) #başlangıç ve bitiş değerine göre yazar
print(str[2]) #istenilen indisteki değeri yazar
print(str[::2]) #başlangı, bitiş ve atlama değeri verilir
print(len(str)) #verilen stringin uzunlugunu bulur
print(str + " ANKARA") #ekleme, bağlama yapma
print(str.upper()) #tüm ifadeleri buyuk yapar
print(str.lower()) #tum ifadeleri kucuk yapar
print(str.split()) #verdiğimiz değişkene göre string de ayırma yapar
print(str.split(sep = "i", maxsplit=2)) # burda i lerde ayırma yaptık 2 defa yapar
