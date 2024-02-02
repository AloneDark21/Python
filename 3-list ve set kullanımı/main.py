
liste = ['a','b','c','d','f','a','e'] #listeler köşeli parantez ile tanimlanir
print(liste)

 
liste.pop() #içine index değeri vermezsek listedeki son veriyi siler 
liste.pop(3) #verilen indexteki veriyi listeden siler

liste.append('g') #listenin sonuna girilen veriyi ekler


sayilar = [1, 5, 9, 3, 8, 2, 2, 6, 15, 0, 4]
print("\nListe = ",sayilar)

print("\nListedeki eleman sayisi = " , len(sayilar)) #liste uzunlugunu bulur

sayilar.sort() #listeyi kucukten buyuge dogru sıralar
print("\nsort() fonksiyonu ile liste = ",sayilar)

sayilar.reverse() #listeyi buyukten kucuge dogru sıralar 
print("\nreverse() fonksiyonu ile liste = ",sayilar)

print("\nset() fonksiyonu ile liste = ",set(sayilar)) #set() listedeki tekrar eden sayıları teke indirir ve listeyi düzenler
