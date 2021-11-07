import webbrowser, re, webbrowser

translator="translate.google.com/?hl=es&sl=en&tl=es&text="

navlan=re.compile(r'hl=\w\w*')
inplan=re.compile(r'sl=(\w\w)*')
outlan=re.compile(r'tl=(\w\w)*')
text=re.compile(r'(text=(\w)*)')
spaces=re.compile(r'\s')


lang=input("idioma de entrada:\n")
langout=input("idioma de salida:\n")
trad=input("texto a traducir:\n")


translator=navlan.sub('hl=es',translator)
translator=inplan.sub('sl='+lang, translator)
translator=outlan.sub('tl='+langout,translator)
translator=text.sub('text='+trad,translator)
translator=spaces.sub('%20',translator)

webbrowser.open(translator)

