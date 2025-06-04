#Degiskenler ve de Ver Tipleri
adiSoyadi = "Bora Saglam"                   #string
yas = 21                                    #integer
sehir = "Balikesir"                         #string
universite_adi = "Northumbria University"   #string
ielts_score = 6.5                           #float
ogrenci_mi = True                           #boolean

#Naming Standarts:
# 1. snake_case -> kucuk harf tercih ediliyor. Kelimelerin alti _ (underscroll) ile birbirinden ayrilir. 
#adi_soyadi
#kullanici_kodu_ver
#carpma_sonucu
#bolme_sonucu

# 2. camelCase -> Birlesik kelimelerin ilk harfi kucuk sonraki kelimelerin ilk harfleri buyuk.
#adiSoyadi
#kullaniciKodunuVer

# 3. PascalCase -> Her kelime buyuk harf ile baslar

# Prhthon da en cok tercih edilen genelikle naming snake_case tir.

#Veri Tipleri
#Tip    Açıklama    Örnek
#int    Tam sayı    1, 99, -5
#float  Ondalıklı sayı  3.14, -0.5, 2.0
#str    Metin (string)  "İnci", 'Python'
#bool   Mantıksal (True / False)    True, False


isletme_adi = "Milano Agac Akplama A.S."

mesaj = input("Mesajinizi girin: ")
print("")
print("----------------------------------------------")
print(mesaj, " ielts_score tipi : ",type(ielts_score))
print(mesaj, " yas tipi         : ",type(yas))
print("----------------------------------------------")
print("")

print("")
print("Version : v1.1")
print("Author  : Bora Saglam")
print("Date    : 2025-06-03")
print("Copyright (c) 2025 Bora Saglam")
print("Bu programda degiskenler ve veri tipleri anlatilmistir.")
# Burayı sildim.
print("")
# Program sonlandiriliyor...