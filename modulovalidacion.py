#MÓDULO 1

#VALIDACIÓN

def valInt (valor,lista=None): #validacion de enteros
    if isinstance(valor, int) and lista==None:
        print(True)
        return True
    elif isinstance(valor, float) or isinstance(valor, complex): 
        print(False)
        return False
    elif isinstance(valor,int) and isinstance(lista,list): 
        if lista[0]<lista[1]:
            if valor>=lista[0] and valor<=lista[1]:
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            print("ValueError")
            return ValueError
    elif isinstance(valor,int) and isinstance(lista,tuple):
        if valor>lista[0] and valor<lista[1]:
            print(True)
            return True
        else:
            print(False)
            return False
    elif isinstance(valor,int) and isinstance(lista,int):
        print("TypeError")
        return TypeError
def valFloat (valor,lista=None): #validacion de flotantes
    if isinstance(valor, float) and lista==None:
        print(True)
        return True
    elif isinstance(valor, int) or isinstance(valor, complex): 
        print(False)
        return False
    elif isinstance(valor,float) and isinstance(lista,list): 
        if lista[0]<lista[1]:
            if valor>=lista[0] and valor<=lista[1]:
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            print("ValueError")
            return ValueError
    elif isinstance(valor,float) and isinstance(lista,tuple):
        if valor>lista[0] and valor<lista[1]:
            print(True)
            return True
        else:
            print(False)
            return False
    elif isinstance(valor,float) and isinstance(lista,int):
        print("TypeError")
        return TypeError
def valComplex (valor,lista=None): #validación de complejos
    if isinstance(valor,complex) and lista==None:
        print(True)
        return True 
    elif isinstance(valor, int) or isinstance(valor, float): 
        print(False)
        return False
    elif isinstance(valor,complex) and isinstance(lista,list): 
        if lista[0]<lista[1]:
            if (valor.real**2+valor.imag**2)**(1/2)>lista[0] and (valor.real**2+valor.imag**2)**(1/2)<lista[1]:
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            print("ValueError")
            return ValueError 
    elif isinstance(valor,complex) and isinstance(lista,tuple):
        if (valor.real**2+valor.imag**2)**(1/2)>lista[0] and (valor.real**2+valor.imag**2)**(1/2)<lista[1]:
                print(True)
                return True
        else:
                print(False)
                return False
    elif isinstance(valor,complex) and isinstance(lista,int):
        print("TypeError")
        return TypeError
def valList(l1,l2=0,ins=''): #validación de listas
    if isinstance(l1,list) and l2==0 and ins=="":
        print(True)
        return True
    elif ins=='value' and (isinstance(l1,list) and isinstance(l2,list)) and (l1==l2):
        print(True)
        return True
    elif ins=="len" and (isinstance(l1,list) and isinstance(l2,int)) and (len(l1)==l2):
        print(True)
        return True
    elif isinstance(l1,int) or isinstance(l1,float) or isinstance(l1,complex) or isinstance(l1,tuple):
        print(False)
        return False
    elif ins=='value' and (isinstance(l1,list) and isinstance(l2,list)) and (l1!=l2):
        print(False)
        return False
    elif ins=="len" and (isinstance(l1,list) and isinstance(l2,int)) and (len(l1)!=l2):
        print(False)
        return False
    elif (isinstance(l2,str) or isinstance(l2,list) or isinstance(l2,float)) or (isinstance(ins,int) or isinstance(ins,float) or isinstance(ins,list) ):
        print("TypeError")
        return TypeError
    elif (isinstance(l2,str) or isinstance(l2,int) or isinstance(l2,float)) or (isinstance(ins,int) or isinstance(ins,float) or isinstance(ins,list) ):
        print("TypeError")
        return TypeError


