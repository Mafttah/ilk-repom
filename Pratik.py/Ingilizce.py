from googletrans import Translator

# Translator nesnesi oluştur
translator = Translator()

ceviri = translator.translate("Bonjour")
print("Algılanan dil:", ceviri.src)
print("Çeviri (EN):", ceviri.text)