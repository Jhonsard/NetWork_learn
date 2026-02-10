def Validat_enter(argfunction):
    '''
    Decorateur de validation
    '''
    def nouvelle_actiion(self, *args, **kwargs):
        if any(arg < 0 for arg in args):
            print("les arguments ne peuvent etre negatives")
            return
        return argfunction(self, *args, **kwargs)
    return nouvelle_actiion

class Calculatrice:
    @Validat_enter
    def additionner(self, a,b):
        return a+b

    @Validat_enter
    def soustraire (self, a, b):
        return a-b
    
machine = Calculatrice()

m1 = machine.additionner(-1, 12)
m2 = machine.soustraire(5, 10)

print(m1)
print(m2)