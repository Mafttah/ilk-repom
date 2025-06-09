from googletrans import Translator

trans = Translator()
t = trans.translate('Hello', src= 'en', dest='fr')
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')