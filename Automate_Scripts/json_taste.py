import json

musica = {}
musica['snk'] = []


musica['snk'].append({
    'nombre' : 'shingeki no kioyin', 
    'escritor' : 'hayime isayama',
    'compositor de audio': 'hiroyuki sawano',
    'temporadas' : 3})

musica['snk'].append({
    'ya': 'estoy hasta la verga', 
    'joder' : 'esto es una mierda'

})

with open('prueba.json', 'w') as prueba:
    json.dump(musica, prueba, indent=3) 

    
with open('prueba.json' ) as prueba:
    x = json.load(prueba)
    print(x)

