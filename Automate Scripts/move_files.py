import shutil, re, os

def sort_music():


    n_moved=0
    files_print=[]
    files_folder=[]

    for folder, subfolder, archivos in os.walk('c:\\'):


        try:
            os.chdir(folder)
            music=re.compile(r'y2mate.com - ')
            mp3=re.compile(r'.mp3')
            part=re.compile(r'.part')
            mp3x2=re.compile(r'.mp3.mp3')
            repetido=re.compile(r'\(\d\)')
            downloaded=[]
            moved=[]

            for canciones in range(0,len(archivos)):
                repeated=repetido.search(archivos[canciones])
                if not music.search(archivos[canciones])==None:
                    if repeated!=None:
                        to_quit=repetido.sub('',archivos[canciones])
                        ocurrencias=0

                        for musicas in range(0,len(archivos)):
                            if to_quit==archivos[musicas]:
                                ocurrencias==ocurrencias+1

                        if ocurrencias>1:
                            os.remove(folder+'\\\\'+archivos[canciones]) 
                            continue

                            


                    if part.search(archivos[canciones])==None and mp3x2.search(archivos[canciones])==None:
                        downloaded.append(archivos[canciones])
                        
                    else:
                        os.remove(folder+'\\\\'+archivos[canciones])



            for canciones in range(0,len(downloaded)):
                moved.append(music.sub('',downloaded[canciones] ))
                files_print.append(music.sub('',downloaded[canciones] ))
                files_folder.append(folder)
                shutil.move(downloaded[canciones],'c:\\users\\crist\\music\\'+moved[canciones])
                n_moved=n_moved+1



        except PermissionError:
            continue


    if n_moved!=0:
        print('se han movido los siguientes %s archivos:' % (str(n_moved)))
        for x in range(0,len(files_print)):
            print('%s desde (%s)'%(files_print[x], files_folder[x]))

    return files_print 





