# request paketi GET metodu ile sunucudan veri alma

import requests 
belgeler_URL = "https://data.police.uk/api/forces"
print(requests.get(belgeler_URL))
response = requests.get(belgeler_URL)

# 200 statü kodu islemin basarili bir sekilde gerçeklersmisitri demektir
# 400 statü kodu aradigimiz sayfanin bulunmadigi hatasidir

print(response.status_code) # statu kodumuzu bu sekilde de ogernebiliriz

print(response.url) # sunucu adresini ogrenmek icin bu komut kullanilir

#print(response.text) # text ozelligi icerigi okumak icin kullanilir

#print("\n",response.json()) #json() komutu ile de icerigi yazdırabiliriz

# parametre kulanarak veri alma
#https://data.police.uk/api/crime-categories?date=2011-08 # parametre oldugunu linkimizden anlıyoruz
# linkte ? ' den sonra date yazılmış sadece bir parametre alıyor demektir. Birden fazla parametre de alabilir

suc_kategorileri_URL = "https://data.police.uk/api/crime-categories"
payload = {"date" : "2023-08"} # parametremiz
response = requests.get(suc_kategorileri_URL, params = payload)
print(response)
print(response.status_code)
print(response.url)
#print(response.json())

# birden fazla parametre kullanimi
# https://data.police.uk/api/crimes-at-location?date=2017-02&location_id=884227
# linkimizde ? ' den sonra date ve location_id olmak uzere 2 parametre vardır
payload2 = { # burda tarih opsiyoneldir eklemesekte olabilir
    "category" : "all_crime",
    "force" : "city_of_london",
    "date" : "2023-01"
}

suc_URL = "https://data.police.uk/api/crimes-at-location"
response2 = requests.get(suc_URL,params=payload2)
print(response2.url)
print(response.json())
  