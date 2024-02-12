""" RADAR CHART GRAFİGİ OLUSTURMA"""

import requests
from PIL import Image
from io import BytesIO

grafik_URL = "https://image-charts.com/chart"

paload = {
    "chco" : "3092de", # grafigin rengi
    "chd" : "t:81,65,50,67,59,81", # grafikte isaretlenecek degerler
    "chl" : "hiz|sut|pas|top_surus|defans|fizik" ,
    "chdl" : "Falcao", # label
    "chdlp" : "b", 
    "chs" : "480x480",# buyukluk 
    "cht" : "r", # radar chart
    "chtt" : "Futbolcu Ozellikleri" # grafige verdigimiz isim(baslık)
}

response = requests.post(grafik_URL, data= paload)
print(response.status_code)

image = Image.open(BytesIO(response.content))
print(image.show())