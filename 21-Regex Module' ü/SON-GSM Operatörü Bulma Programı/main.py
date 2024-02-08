"""
54 ile baslayan vodafone 
501, 505, 506 ile baslayan avea
53 ile baslayan turkcell

"""
import re

def gsm_operatoru_bul(tel_no) : 
    patern = r"(\d{3})-(\d{7})"
    eslesme = re.search(patern, tel_no)
    
    if eslesme :
        gsm_kod = eslesme.groups()[0]
        print("GSM Kodu : ",gsm_kod)
        if gsm_kod.startswith("54") : # burda startSwith() metodu verimiz içerisine yazdıgımız parametre ile baslıyor mu onu kontrol ediyor
            return "Vodafone"
        elif gsm_kod.startswith("501") or gsm_kod.startswith("505") or gsm_kod.startswith("506") :
            return "AVEA"
        elif gsm_kod.startswith("53") :
            return "Turkcell"
        else : 
            return "GSM Operatoru Bulunamadi."
    else :
        return "Eslesme Bulunamadi."
    
tel_no = "0505-5234200"
print("GSM Operatoru : ",gsm_operatoru_bul(tel_no))    
