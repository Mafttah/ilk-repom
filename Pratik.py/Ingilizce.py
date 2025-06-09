from googletrans import Translator

# Translator nesnesi oluştur
translator = Translator()

# Örnek metin
metin = "Merhaba dünya"

# İngilizce'ye çevir
ceviri = translator.translate(metin, dest='en')

print("Orijinal:", metin)
print("Çeviri:", ceviri.text)