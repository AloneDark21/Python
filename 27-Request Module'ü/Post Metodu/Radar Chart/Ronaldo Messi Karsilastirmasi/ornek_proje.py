"""
bu projede post ve get komutu kullanarak ronaldo ve messinin verilerini internetten çekip grafige aktarma islemi yapacagiz
 
"""

import requests
from PIL import Image
from io import BytesIO


class futbolcu() :
    def __init__(self, isim, hiz, sut ,pas, top_surme, defans, fizik) :
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas 
        self.top_surme = top_surme
        self.defans = defans
        self.fizik = fizik

    def yetenek_hazirla(self) :# join() komutu basına koydugumuz isareti veya argumanı birlestirilen dizelerin arasına koyar 
        return ",".join([# join() komutu ile basa koydugumuz gonderdigimiz ozellikleri birlestirip tek bir dize haline getirmek için kullanilir
            str(self.hiz) , # bu komut ile gelen verileri stringe donusturduk
            str(self.sut) ,
            str(self.pas) ,
            str(self.top_surme) ,
            str(self.defans) ,
            str(self.fizik) ,
            str(self.hiz)
        ])
         
    def yetenek_gorselleştir(self) :
        grafik_URL = "https://image-charts.com/chart"
        payload = {
            "chco" : "3092de", # grafik rengi
            "chd" : "t:"+ self.yetenek_hazirla(), # oyunculara ait ozellikler
            "chdl" : self.isim, # oyuncularin ismi
            "chs" : "480x480", # grafigin buyuklugu
            "cht" : "r", # radar grafigi
            "chtt" : "Futbolcu Ozellikleri", # grafik basligi
            "chl" : "hiz|sut|pas|top_surus|defans|fizik", # grafik uzerinde bulunacak olan ozellik isimleri
            "chxl" : "0:|0|20|40|60|80|100", # grafikte alinacak degerler 0 dan 100 e
            "chxt" : "x", # x ekseni tanimladik
            "chxr" : "0,0.0,100.0", # max ve min degeri
            "chm" : "B,AAAAAABB,0,0,0" # grafikteki renk kodu
        }
        response = requests.post(grafik_URL,data= payload)
        image = Image.open(BytesIO(response.content))
        image.show()
    
    def yetenek_kiyaslama_goster(self, hedef_futbolcu) :
        grafik_URL = "https://image-charts.com/chart"
        payload = {
            "chco" : "3092de,027182", 
            "chd" : "t:"+ self.yetenek_hazirla() + "|" + hedef_futbolcu.yetenek_hazirla(), 
            "chdl" : self.isim + "|" + hedef_futbolcu.isim,
            "chs" : "480x480", 
            "cht" : "r", 
            "chtt" : "Futbolcu Ozellikleri", 
            "chl" : "hiz|sut|pas|top_surus|defans|fizik",
            "chxl" : "0:|0|20|40|60|80|100", 
            "chxt" : "x", 
            "chxr" : "0,0.0,100.0",
            "chm" : "B,AAAAAABB,0,0,0" +"|" +"B,0073CFBB,1,0,0"
        }
        response = requests.post(grafik_URL,data= payload)
        image = Image.open(BytesIO(response.content))
        image.show()
     
    """ Messinin Ozelliklerini Aldigimiz Link""" 
    def messinin_ozellikleri (self) : 
        messi_URL = "https://cdn.mos.cms.futurecdn.net/r9KJrrXW3XTAFXavR8bvaC-1024-80.jpg.webp"
        response = requests.get(messi_URL)
        print(response.status_code)
        image_messi = Image.open(BytesIO(response.content))
        print(image_messi.show())   
        
    """ Ronaldonun Ozelliklerini Aldigimiz Link""" 
    def ronaldonun_ozellikleri (self) : 
        ronaldo_URL = "https://cdn.mos.cms.futurecdn.net/h93YS6AZRWjwy2hiETSEyC-1200-80.jpg.webp"
        response = requests.get(ronaldo_URL)
        print(response.status_code)
        image_ronaldo = Image.open(BytesIO(response.content))
        print(image_ronaldo.show())       
    

       
messi = futbolcu("Messi", 85, 82 ,91, 95, 38, 65)
ronaldo = futbolcu("Ronaldo", 89, 93, 81, 89,35, 77)         

ronaldo.yetenek_kiyaslama_goster(messi) # ronaldonun messiye göre kıyaslanma grafigi
messi.yetenek_kiyaslama_goster(ronaldo) # messinin ronaldoya göre kıyaslama grafigi
#messi.yetenek_gorselleştir() # messinin radar grafigini cizdirir
#ronaldo.yetenek_gorselleştir() # ronaldonun radar grafigini cizdirir 
#messi.messinin_ozellikleri() messinin ozellik fotografini yazdirir
#ronaldo.ronaldonun_ozellikleri() ronaldonun ozellik fotografini yazdirir 




      