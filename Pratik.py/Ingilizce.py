from googletrans import Translator
translator = Translator()
mesaj1 = translator.translate("Hello", dest="fr")
print(mesaj1)