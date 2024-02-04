"""
kullanim sekli

if <kosul saglanirsa> :
    <burda istenileni yap>
elif <üstteki kosul saglanmazsa bu saglanirsa> : 
    <burda istenileni yap>
else : 
    <yukaridaki hiçbir kosul saglamazsa burda istenielni yap>

"""

# opratör kullanımı
# == , < , > , or , and , <= , >= operatörler
yas = 35

if yas < 18 : 
    print("Yasiniz uygun degil")
else :
    print("Yasiniz uygundur")

# listelerle kullanimi 
liste = ["a", "b", "c"]
harf = "d"

if harf in liste :
    print("İstenilen harf listede bulunuyor")
else :
    print("Harf listede bulunmuyor")
    liste.append(harf)
    print("Harf listeye eklendi. Güncel liste : {}".format(liste))

# and ve or ile kullanimi
harf = "a"    
if harf in liste and harf in liste[0]:
    print("İstenilen harf listede bulunuyor ve ilk elemandir.")
elif harf in liste :
    print("istenilen harf lisytede bulunuyor ama ilk sirada değildir")    
else :
    print("Harf listede bulunmuyor")
    liste.append(harf)
    print("Harf listeye eklendi. Güncel liste : {}".format(liste))
