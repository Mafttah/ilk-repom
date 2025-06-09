from googletrans import Translator
translator = Translator()
mesaj = "text"
result = translator.translate("Hello", dest="fr")
print(result.mesaj)