# math module kullanimi

import math # math kütüphanesini import ettik
# en fazla kullanılan fonksiyonlari kullancagiz burda

# normalde round() komutu en yakin ondaliga yuvarlama islemleri için kullanilirken
# ceil ve floor komutlari alt veya uste yuvarlam islemleri için kullanilir

# ceil komutu bir ust sayiya yuavrlama islemi yapar

sayi = 8.3
print(math.ceil(sayi)) # burda sayimiz 8.3 iken ceil() komutu ile bir ust sayi olan 9 a yuvarlandi   

print(math.floor(sayi)) # burda ise floor komutu ile sayiyi bir alt olan sayiya yani 8 e yuvarlama ialemi yaptik

# faktöriyel hesabı yapmak için factorial() komutu kullanırız
print(math.factorial(5)) # burda 5 sayisinin faktoriyelini aldik

# uss almak icin pow() komutunu kullanırız
print(math.pow(3,4))
