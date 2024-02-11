"""
Decorator kullanim sekli 

@decorator
def func.....

"""
# degisken olarak fonksiyon

def deneme() : 
    print("abc")
    
f = deneme # deneme fonksiyonunu f degiskenine attik
f() # f degiskenini cagirdik   
 

# fonksiyon içinde fonksiyon
def deneme2 () :
    print("Deneme fonksiyonu çalişiyor")
    
    def test () :
        return "test fonksiyonu çalisiyor"
    print(test())
    
deneme2()    

# test fonksiyonunu fonksiyonda ekrana yazdırmadan nasıl yazdırabiliriz
def deneme3 () :
    print("Deneme fonksiyonu çalişiyor")
    
    def test () :
        return "test fonksiyonu çalisiyor"
    return test
    
f = deneme3()
print(f())

# Decoratorler
# arguman olarak fonksiyon gonderme
def deneme4():
    return "Deneme4 fonksiyonu calisiyor"

def deneme5(k):
    print("deneme5 fonksiyonu calisiyor")            
    
    print(k())

deneme5(deneme4)    

# decorator kullanimi
def deco(f):
    
    def wrapper() :
        print("baslangic")
        
        f()
        
        print("bitis")
        
    return wrapper    

@deco # burda decoratoru kullandik
def yazdir() :
    print("yazdir")
    
yazdir()
# decorator her fonksiyon uygulanmaz 
# argüman alan fonksiyonlara decorator uygulayamayız

# ornek
""" 
@deco # burda decorator uygulanmaz ama bunu onune gecebiliriz
def toplama(a, b) :
    print(a+b)
    
toplama(5, 7)    
"""

# arguman alan fonksiyonlarda decorator kullanimi
def deco2(f):
    
    def wrapper(*args) :# *args kullanımı arguman olarak istedigimizi gonderebiliriz sayısı belli degil
        print("baslangic")
        
        f(*args)
        
        print("bitis")
        
    return wrapper    
@deco2
def toplama(a, b) :
    print(a+b)
    
toplama(5, 7)

# arguman alan decorator
def deco3(msg1, msg2):
    
    def arakatman(f) : 
        def wrapper(*args) :
            print(msg1)
        
            f(*args)
        
            print(msg2)
        
        return wrapper 
    return arakatman
 
@deco3("ilk", "Sonuc")
def toplama2(a, b) :
    print(a+b)
    
toplama2(5, 7)

