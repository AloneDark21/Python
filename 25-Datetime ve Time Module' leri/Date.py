# baslangicta datatime.date gün kısmıyla ilgilenecez

from datetime import date

bugun = date.today() #bugunun tarihini yazdırdık
print(bugun)

# kendimiz bir tarih olusturmak istersek asagidaki gibi yapabiliriz
manuel_olusturdugum_tarih = date(2020, 10, 20)
print(manuel_olusturdugum_tarih)
print(bugun - manuel_olusturdugum_tarih) # tarihler arasındaki fark

# year, month, day olarak tarihi hucrelere bolup manuel olarak erisim saglamak
print(bugun.day)
print(bugun.month)
print(bugun.year)

# haftalık degere isocalender() komutu ile ulasırız
print(date.isocalendar(bugun))

print(date.isocalendar(bugun)[0])# tarihin yıl kısmına ulasırız
print(date.isocalendar(bugun)[1])# tarihin hafta kısmına ulasabiliriz
print(date.isocalendar(bugun)[2])# haftanın hangi gunude oldugumuza ulasabiliriz

# hafta bilgisine ulasmanın bir diger komutu ise weekday() komutudur
print(date.weekday(bugun))

# tarih bilgisini daha detayli bir sekilde ekrana basmak icin ctime() komutu kullanilir
print(date.ctime(bugun))
