from googletrans import Translator
translator = Translator()
mesaj = "text"
mesaj1 = translator.translate("Hello", dest="fr")
print(mesaj1.mesaj)