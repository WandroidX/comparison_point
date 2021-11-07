import re
text="hola we, este es la fecha: 30-08-2021.\n la fecha de mañana será la siguiente: 31-08-2021. en una semana, la fecha será 06-09-2021"
rex=re.compile(r'\d\d-\d\d-\d\d\d\d')
search=rex.findall(text)


print("hay %s resultados para su busqueda:\n" %(len(search)))
for x in range(0,len(search)):
    print(search[x])
