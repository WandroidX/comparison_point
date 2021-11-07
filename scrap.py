import requests

#requests.get() descarga una web
solicitud=requests.get('http://www.sromero.org/wiki/linux/aplicaciones/manual_vim')

print(solicitud.text)
