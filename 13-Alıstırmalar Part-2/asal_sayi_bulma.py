# verilen sayinin asal olup olmadıgını bulalım
# en kucuk asal sayı 2 dir degerleri bu durumu göz onunda bulundurarak veriniz
sayi = 41
temp = 2

while temp < sayi/2 :
    if sayi%temp == 0 :
        print("{} asal sayi degildir.".format(sayi))
        break
    else : 
         temp += 1
else :
        print("{} asal sayidir.".format(sayi))    
