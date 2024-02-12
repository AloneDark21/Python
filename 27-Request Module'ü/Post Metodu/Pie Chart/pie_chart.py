#  bu uygulamada post komutu ve messi mi ronaldo mu ayrımını yapcagiz

""" POST TALEBİ """
import requests

# asagidaki bilgileri yazdigimiz linkten aldik
grafik_URL = "https://image-charts.com/chart"
payload = {
    "chs" : "700x190", # buyukluk
    "chd" : "t:60,40", # oran
    "cht" : "p3", # pasta grafigi
    "chl" : "Hello|World", # hello ve world olarak orantılanacak
    "chan" : None,
    "chf" : "ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1"
}

response = requests.post(grafik_URL, data=payload)
print(response.status_code) # statu kodumuza baktık 200 ise dogrudur

print(type(response.content)) # burda aldigimiz veri bytes tipindedir bunu görsele çevirmek için asagidaki iki kutuphaneyi ekleyecegiz

# kutuphanelrimizi ekledik
from PIL import Image
from io import BytesIO

image  = Image.open(BytesIO(response.content)) # bytes olan verileri fotografa cevirdik
print(image.show()) # cevirdigimiz fotografi ekrana yazdirdik




