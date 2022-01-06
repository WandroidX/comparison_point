# exceptions raised if the 
class IsnFloat(Exception):
    pass

class NoNumbersAfterDot(Exception):
    pass

class NegativeNumber(Exception):
    pass

class IsnInteger(Exception):
    pass

class IsZeroOrLower(Exception):
    pass

        
class RoundTo:


    # funcion iniciadora
    def __init__(self,flt):

        if type(flt) is float:
            self.flt = flt

        else:
            raise IsnFloat()
            
    # esta funcion se ejecuta si se convierte la clase a string con la funcion str
    # def __str__(self):
        # return str(self.flt)

    # def __add__(self,flt, other_flt):
        # return flt + other_flt


    # encuentra el primer cinco en el argumento "flt" y le suma uno y borra los demás numeros
    def to_five(self):
        flt = self.flt
        flt=str(flt).split('.')
        flt[1]=list(flt[1])

        for five in range(len(flt[1])):

            if int(flt[1][five])>=5:
                if five==0:
                    flt[0]= int(flt[0])
                    return flt[0]+1

                else:
                    flt[1][five]=str(int(flt[1][five])+1)
                    flt[1][five+1:]=''
                    decimales='.'+''.join(flt[1])
                    return float(flt[0]+decimales)





    def x_decimals(self, digit_amount):

        if digit_amount<=0:
            raise IsZeroOrLower()
        
        elif isinstance(digit_amount,int):

            flt = self.flt
            flt=str(flt).split('.')
            flt[1]=list(flt[1])

            if len(flt[1])>digit_amount:
                decimales = '.'+''.join(flt[1][0:digit_amount])
                return float(flt[0]+decimales)

            else: 
                return float(flt[0]+'.'+''.join(flt[1]))



        else:
            raise IsnInteger()




    def to_int(self):
        flt = self.flt
        flt = str(flt).split('.')

        return int(flt[0])




    




