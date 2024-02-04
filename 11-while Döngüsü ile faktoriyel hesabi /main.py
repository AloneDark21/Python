# girilen sayisinin faktoriyelini bulacagiz

sayi = 5
temp = sayi
sonuc = 1

while temp>0 :
    sonuc = sonuc*temp
    temp -= 1

print("{} sayisinin faktoriyeli : {}".format(sayi,sonuc))
