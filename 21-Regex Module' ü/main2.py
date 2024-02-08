"""
bu projede de regex sembollerinin kullanimindan bahsedeceğiz

" | " sembolu veya anlaminda kullanilir
" ^ " baslar anlaminda kullanilir
" $ " biter anlaminda kullanilir
" . " herhangi bir şey anlaminda kullanilir
" \ " kaçma anlaminda kullanilir atifta bulunacagimiz karakter için kullaniriz

birazdan ornekte hepsini anlayacağiz

"""
import re

def mesaj_hissi_bul(mesaj) :
    hisler = []
    
    pozitif_patern = r"(merhaba|ask|sevgi|dost|kardes| :\)+ )"
    negatif_patern = r"(lan|aptal|yeter|birak|cekil|git)"
    
    heyecanli_patern = r"! | [!|?]{2,}$" 
    sakin_patern= r"^[Tabi|Hayhay]"
    
    emin_patern = r"[K|k]esin|[T|t]abi|[E|e]lbet"
    kararsiz_patern = r"[B|b]elki|[S|s]anirim"
    
    if re.search(pozitif_patern, mesaj) :
        hisler.append("Pozitif")
    if re.search(negatif_patern, mesaj) :
        hisler.append("Negatif")
    if re.search(heyecanli_patern, mesaj) :
        hisler.append("Heyecanli")
    if re.search(sakin_patern, mesaj) :
        hisler.append("Sakin")
    if re.search(emin_patern, mesaj) :
        hisler.append("Emin")
    if re.search(kararsiz_patern, mesaj) :
        hisler.append("Kararsiz") 
        
    return hisler               


mesaj1 = "Naber abi? :)             "     
mesaj2 = "Tabikiii ki buyrun        "
mesaj3 = "Saçmalamayi birak artik!  "
mesaj4 = "Belki yarindan da yakin..."
mesaj5 = "Elbet birgün bulusacagiz  "

mesajlar = [mesaj1, mesaj2, mesaj3, mesaj4, mesaj5]
for kelime in mesajlar : 
    print(kelime, "\t", mesaj_hissi_bul(kelime))        
