
def frecuencia(values=0):

    if values==0:
        datos=[]
        cantidad=input("cuantos datos quieres agregar?")
        while cantidad.isdigit()!=True:
            cantidad=input("cuantos datos quieres agregar?")
        for x in range(0,int(cantidad)):
            entrada=input("valor: ")
            datos.append(int(entrada))    
    else:
        datos=values

    fa=[]
    array=[]
    fi=[]
    fifa=[]
    fr=[]



    datos.sort()
        
    for r in range(0,len(datos)):
        datos[r]=int(datos[r])


    for w in range(0,len(datos)):

        try:
            wa=datos[w]
            wao=array.index(wa)

        except ValueError: 
            array.append(wa)
            cuenta= datos.count(wa)
            fa+=str(cuenta)

    for za in range(0,len(fa)):
        fa[za]= int(fa[za]) 

    for z in range(0,len(fa)):
        suma=sum(fa[0:z+1])
        fi.append(suma)

    for q in range(0,len(fa)):
        relativa=fa[q]/len(datos)
        fr.append(relativa)

    for d in range(0,len(fa)):
        fixfa=fi[d]*fa[d]
        fifa.append(fixfa)

    print("\tdatos\tfa\tfi\tfr\tfa * FI".upper())

    for y in range(0,len(array)):
            print("\n")
            print("\t%s\t%s\t%s\t%s\t%s" % (array[y],fa[y],fi[y],fr[y],fifa[y])) 


    mediana=len(datos)-1
    if str(mediana).isdecimal()==True:
        mediana=mediana/2
        medi=0
    else:
        mediana=mediana-0.5
        medi=mediana+1
    print("\tTOTAL\t%s\t%s\t%s\t%s" % (sum(fa),sum(fi),sum(fr),sum(fifa))) 
    print("\n\nmedia: %s"% (sum(datos)/len(datos)))
    if medi!=0:

        print("mediana: %s, %s" % (datos[int(mediana)],datos[int(medi)]))
    else:
        print("mediana: %s"% (datos[int(mediana)])) 
