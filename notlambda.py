
lista = ['hola', 'we', 'soy', 'wandroid']

five_big = [x.replace(y, 'x') for x in lista for y in x if y=='a' or y=='o']

print(five_big)
