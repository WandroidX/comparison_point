lista = ["que es la droga", "tipos de computadora"]
search = input("que deseas buscar?\n")
for x in lista:
    if search in x:
        print(x)
        continue
