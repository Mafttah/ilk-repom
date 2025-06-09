from googletrans import Translator
translator=Translator()
tr=translator.translate("Hello","Good morning","Good Afternoon","Good Evening", dest= 'fr')
print("tr.text")
