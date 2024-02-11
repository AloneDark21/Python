# bu ornekte decorator ile sure olcumlemesi yapacagiz

import time

def sure_olc(f) : 
    
    def wrapper(*args) : 
        
        baslangic = time.time()
        print("Baslangic Zamani : \t", baslangic)
        
        f(*args)
        
        bitis = time.time()
        print("Bitis Zamani : \t",bitis)
        print("Gecen Zaman : \t",bitis-baslangic)
        
    return wrapper    

@sure_olc
def faktoriyel(sayi) :
    toplam = 1
    
    while sayi > 1:
        toplam *= sayi
        sayi -= 1
    
    print(toplam)    
    
    
faktoriyel(300)    
    
    
