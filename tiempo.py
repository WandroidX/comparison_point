import time


def tiempo(seconds,regresar_todo=0):
    if seconds < 60:
        return "estos segundos equivalen a" + str(seconds) + " segundos"
    elif seconds >= 60:
        minutos = seconds / 60
        if regresar_todo!=0 and minutos:
            print("estos segundos equivalen a " + str(minutos) + " minutos")
        if seconds >= 3600:
            horas = seconds / 3600
            if regresar_todo!=0 and horas:
                print("estos segundos equivalen a " + str(horas) + " horas")
            if seconds >= 86400:
                dias = seconds / 86400
                if regresar_todo!=0 and dias:
                    print("estos segundos equivalen a " + str(dias) + " dias")
                if dias >= 365:
                    años = dias / 365
                    if regresar_todo!=0 and años:
                        print("estos segundos equivalen a " + str(años) + " años")
                    if años >= 100:
                        siglos = años / 100
                        if regresar_todo!=0 and siglos:
                            print("estos segundos equivalen a " + str(siglos) + " siglos")
                        if siglos >= 10:
                            milenios = siglos / 10
                            if regresar_todo!=0 and milenios:
                                print("estos segundos equivalen a " + str(milenios) + " milenios")
                            return "estos segundos equivalen a "+ str(milenios) + " milenios"
                        return "estos segundos equivalen a " + str(siglos) + " siglos"
                    return "estos segundos equivalen a " + str(años) + " años"
                return "estos segundos equivalen a " + str(dias) + " dias"
            return "estos segundos equivalen a " + str(horas) + " horas"
        return "estos segundos equivalen a " + str(minutos) + " minutos"



        
print(tiempo(1000000000000000000000000000, 1))
