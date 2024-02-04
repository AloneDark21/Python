# continue komutu bir döngü içinde istediğimiz adımı atlamak için kullanılır

for sayi in range(5,20) : # 5 ile 20 arasındaki tek sayilari yazdırdık  
    if sayi%2 == 0 :
        continue
    else :
        print(sayi)
