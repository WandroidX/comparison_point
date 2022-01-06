import os


def list_music(ruta_de_musica = 'c:\\users\\crist\\music'):
    musicas = [musica for musica in os.listdir(ruta_de_musica) if musica.endswith('.mp3') ]
    return musicas



