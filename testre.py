import re

x="hola, esto es una prueba. la contraseña es: 2x5cb2"
y=re.compile(r'\d\a\d\a\a\d')
w=y.search(x)

print(w)
