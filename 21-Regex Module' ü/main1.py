# regex module'ü
import re 

cumle = "Kemalettin Şaşmaz Türk, Ortadoğu Teknik Üniversitesi,Türk"
patern = "Türk"

"""for eslesme in re.finditer(patern, cumle) : 
    print(eslesme.span(), eslesme.group())"""
    
# Bu modülde bu fonksiyonları kullanrak bir yazı içerisinde bir kelimenin veya bir harfin kaç defa ve nerelerde geçtiğini bulmak için kullandık

# dinamik kullanımı aşagidaki gibidir

# \d rakam aramak için kullanilir, Ornek : base42 - base\d\d
# \w karakter aramak için kullanilir, Ornek : R2-D2 - \w\w\w\w\w  , hem karakter hem harf aramak içinde kullanılabilir
# \s bosluk aramakiçin kullanilir , Ornek : Ping Pong - Ping\sPong

# \D rakam değil, Ornek : base - \D\D\D\D
# \W karakter değil, Ornek : R2D2 - \W\W\W\W
# \S boşluk değil, Ornek : PingPong - \S\S\S\S\S\S\S\S

# cumlede geçen telefon numarasini bulmak için aşagidaki islemi yapabiliriz
cumle1 = "Selam, benim telefon numaram 0535-8886622"
patern1 =  r"\d\d\d\d-\d\d\d\d\d\d\d" # bu uzun yazılmış hali bunları kısa halde de kullanabiliriz

patern2 = r"\d{3,4}-\d{7}" # kisa kullanim sekli 

re.search(patern2, cumle1) # burda zaten ne yapıldigi gorunuyor cumle icinde paterni ara (search)

# Ornek - 1
cumle2 = "En sevdiğim kanal base42, bas3, ba5, b8, 9"
patern3 = r"\s\w{5,}" # burdaki filtrede de once space(s) bosluk daha sonra 5 ya da daha fazla karakter filtreme işlemi yapar

# bu for dongusunda yaptıgımız filtreye uygun eslesmeleri tum cumlede arfayıp ekran yazma islemini yapıyoruz
"""for eslesme in re.finditer(patern3, cumle2) :
    print(eslesme.span(), eslesme.group())"""
    
# Ornek - 2 yukarıdaki cumle2 yi kulanacagiz    
patern4 = r"\d?" # burda soru isareti sayı mı değil mi diye bakıyor \d ile de her karaktere ayrı ayrı bakar sayı ise yazar   

"""for eslesme in re.finditer(patern4, cumle2) :
    print(eslesme.span(), eslesme.group())
   """ 
# Ornek - 3     
patern5 = r"\d+" # burda da \d sayı aramak, + da bir veya daha fazla sayı aramak için kullanılır

"""for eslesme in re.finditer(patern5, cumle2) :
    print(eslesme.span(), eslesme.group())"""
    
# Ornek - 4  
cumle2 = "En sevdiğim kanal base42, bas3, ba5, b8, 9"   
patern6 = r"\w*\d+" # burda da * w dan sonra kullanmısız yani 0 ya da daha fazla karakterden sonra sayı gelmesi senaryosuna bakıp ekrana yazdıracagiz
# cumle2 deki base42, bas3, ba5, b8, 9 eslesmelerini ekrana yazdirir
# cunku 0 veya daha fazla karakter sonra gelen sayı eslesmesine bakıyoruz 
for eslesme in re.finditer(patern6, cumle2) :
    print(eslesme.span(), eslesme.group())   
