# pass komutu döngüde bulundugumuz adımı geçmek için kullanılır

for sayi in range(5,20) : # 5 ile 20 arasındaki tek sayilari yazdırdık  
    if sayi%2 == 0 :
        pass # burda if koşulu sağlanırsa pas geçerek else geçer 
    else :
        print(sayi)
