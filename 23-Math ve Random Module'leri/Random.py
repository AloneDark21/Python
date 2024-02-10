# random rastgele sayı uretmek icin kullandigimiz fonksiyondur

import random # random kutuphanesini import ettik

x = random.random() # bu sekilde kullanimda 0 ile 1 arasında rastgele sayı uretir
print(x)

y = random.randint(5,20) # randint() kullandigimizda verdigimiz aralikta rastgele int tipinde sayilar uretir
print(y)

print("Liste : ",[*range(10)])
# range ile 0 dan 10 a kadar olan sayılardan liste olusturduk
# choice() komutu liste elemalarından bir tanesini rastgele secmek icin kullanılır
print("Secilen Eleman : ",random.choice([*range(10)])) 

# sample() komutu kullanımı 
# bu komut ile listemizden belirlediğimiz sayıda elamanı rastgele olarak secmeye yarar

my_list = random.sample(range(10), k = 5) # bu komut 0 dan 10 kadar olan sayılardan rastgele 5 tanesini sec demektir
print("Rastgele Secile 5 Eleman : ",my_list)

# shuffle() komutu kullanimi 
# shuffle komutu var olan liste elamanlarini kendi içerisinde karistirmak için kullanilir
my_list2 = [*range(15)]
print("Normal Liste : ",my_list2)
random.shuffle(my_list2)
print("Karistirilmis Liste : ",my_list2)
