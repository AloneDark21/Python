def uygulama() :
    sayi = input("bir sayi giriniz : ")
    sorgu = input("Girilen sayi tek midir cift midir sorgula (cift/ tek) : ")

    if sorgu == "cift" :
        if int(sayi) % 2 == 0 :
            return "Evet {} sayisi cifttir".format(sayi)
        else :
            return "Hayir {} sayisi cift değildir".format(sayi) 
    elif sorgu == "tek":   
        if int(sayi) % 2 == 1 :
            return "Evet {} sayisi tektir".format(sayi)
        else :
            return "Hayir {} sayisi tek değildir".format(sayi)  
        
print(uygulama())    
