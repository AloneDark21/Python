"""
1.kullanim Yapisi
while <kosul sagliyorsa> :
    <istenileni yap>

2.Kullanim Yapisi
while <kosul sagliyorsa> :
    <istenileni yap>
else :
    <yukaridaki kosul saglamazsa buradaki islemi yap>

"""

x = 0
while x < 10 :
    print("{} degeri 10 dan kucuktur".format(x))
    x += 1

# sonsuz göngü baslatmak icin 
    """
    while True :
        <istenilenleri yap>

    """

# else ile kullanımı
x = 0
while x < 10 :
    print("{} degeri 10 dan kucuktur".format(x))
    x += 1
else :
    print("{} sayisi 10 dan kucuk degildir".format(x))    
