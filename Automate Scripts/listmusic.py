import os, re, shutil


def list_music():
    os.chdir('c:\\users\\crist\\music')
    files=os.listdir()
    if files!=[]:
        repeated=re.compile('\\(\\d\\)')
        mp3=re.compile(r'.mp3')
        part=re.compile(r'.part')
        mp3x2=re.compile(r'.mp3.mp3')
        quality=re.compile(r'\(MP3_\d{3}K\)')
    

        music=[]
        for file in files:
            if os.path.isfile(file)==True and mp3.search(file)!=None:
                repetido=repeated.search(file)

                if repetido!=None:
                    to_quit=repeated.sub('',file)
                    ocurrencias=0

                    for musicas in range(0,len(files)):
                        if to_quit==file:
                            ocurrencias==ocurrencias+1

                        if ocurrencias>1:
                            os.remove(file)
                            continue

                            

                if part.search(file)!=None or mp3x2.search(file)!=None:
                    os.remove(file)

                if quality.search(file)!=None:

                    file=shutil.move(file,quality.sub('', file))
                    
                music.append(file)


        return music
            

    else:
        print('doesnt exist musics in the folder')


