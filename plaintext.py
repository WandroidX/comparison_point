texto="c:\\Users\\wandroid\\desktop\\prueba.txt"


# abrir el archivo y hacer una lista con los parrafos
leer=open(texto)
print(leer.readlines())
leer.close()

#abir el archivo y editarlo, sustituyendo lo que ya está con lo que se escriba
edit=open(texto, "w")
edit.write("this is what I wrote with 'write function'")
edit.close()

append=open(texto, "a")
append.write("this is the added with 'write function'")
append.close()

# abrir el archivo de texto e imprimirlo tal cual está escrito
reading=open(texto)
print(reading.read())
reading.close()
