contraseña = ["wandroid", "god"]
usrPass = input("digite la primera contraseña:\n")
if usrPass in contraseña:
    print("primera contraseña es correcta")
    usrPass2 = input("digite la segunda contraseña:\n")
    if usrPass2 in contraseña:
        print("felicidades. puedes pasar")
    else:
        print(
"""
no puedes pasar
has puesto la contraseña incorrecta"""
    )    

else:
    print(
"""
no puedes pasar
has puesto la contraseña incorrecta"""
    )
