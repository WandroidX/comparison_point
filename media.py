import random 
from tabla import frecuencia

cantidad_ejercicios=input("cuantos ejercicios quieres?\n")
cantidad_ejercicios=int(cantidad_ejercicios)

for media in range(0,cantidad_ejercicios):
    cantidad_datos=random.randint(15,40)
    lista=[]
    for datos in range(0,cantidad_datos):
        lista.append(random.randint(1,20))

frecuencia(lista)
print(lista)
