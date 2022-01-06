import re, sys

re_posicion = re.compile(r'(\(.*\))')
signos_de_igualdad = re.compile(r'(.=.)')
comas = re.compile(',*')


y = 'hola crack=hola=2=iioirjei=a'
x = signos_de_igualdad.findall(y)
x = list(x)
if x[0] != ' ':
    x[0] = ' '
if x[2] != ' ':
    x[2] = ' '

x = ''.join(x)
print(x)



