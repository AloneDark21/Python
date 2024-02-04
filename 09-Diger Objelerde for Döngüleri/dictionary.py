# dictionary lerde for döngüsü kullanimi

kullanici = {
    "Ad" : "Kerem",
    "Soyad" : "Ataş"
}
kullanici.items()

print("Kullanicinin :")
for k, v in kullanici.items() :
    print("Key : Value = {} : {}".format(k,v))

# sadece anahtar(key) elemanalrına da ulasabiliriz
print("\nKeys : ")
for k in kullanici.keys():
    print(k)    

# sadece value degerlerine de ulasabiliriz
print("\nValues : ")
for v in kullanici.values() :
    print(v)    
