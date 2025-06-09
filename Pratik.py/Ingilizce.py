from googletrans import Translator
translator=Translator("str")
translation = translator.translate("Hello","Good morning","Good Afternoon","Good Evening", dest= "fr")
print("translation")
