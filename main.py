#PROGRAMA PRINCIPAL

import modulovalidacion
import modulocifrado 

print("Bienvenido. El siguiente menú lo ayudará a validar y encriptar, según necesite.") 
print("\n") 
print("____________________________________") 
print("ELIJA UNA DE LAS SIGUIENTES OPCIONES") 
print("1.VALIDAR UNA ENTRADA.\n2.CIFRAR UNA ENTRADA") 
print("Entienda que para cifrar se utilizara el Cifrado de Cesar") 
print("____________________________________") 

while True: 
    opcion=int(input("Ingrese una opcion: ")) 
    if opcion==1: 
        print("QUE DESEA VALIDAR\na.DATO DE TIPO ENTERO\nb.DATO DE TIPO FLOAT\nc.DATO DE TIPO COMPLEX\nd.DATO DE TIPO LIST")
        nueva_opcion=str(input("Su opcion: "))
        if nueva_opcion=="a":
            modulovalidacion.valInt(4)
            modulovalidacion.valInt(4.0)
            modulovalidacion.valInt(4,(4,10))
            modulovalidacion.valInt(4,[3,9])
            modulovalidacion.valInt(4,[4,10])
            modulovalidacion.valInt(4,[10,4])
            modulovalidacion.valInt(4,5)
            break
        elif nueva_opcion=="b":
            modulovalidacion.valFloat(4.0)
            modulovalidacion.valFloat(4)
            modulovalidacion.valFloat(4.4,(4.4,10))
            modulovalidacion.valFloat(4.4,(4,10))
            modulovalidacion.valFloat(4.1,[4.1,9.05])
            modulovalidacion.valFloat(4.2,[4,10])
            modulovalidacion.valFloat(4.4,[10,4])
            modulovalidacion.valFloat(4.1,5)
        elif nueva_opcion=="c": 
            modulovalidacion.valComplex(3+4j)
            modulovalidacion.valComplex(4.0)
            modulovalidacion.valComplex(3+4j,(5,10))
            modulovalidacion.valComplex(3+4j,[5,10])
            modulovalidacion.valComplex(3+4j,[4,10])
            modulovalidacion.valComplex(3+4j,[10,4])
            modulovalidacion.valComplex(3+4j,5) 
        elif nueva_opcion=="d":
            modulovalidacion.valList([1,2,3,4])
            modulovalidacion.valList([1,2,3,4],[1,2,3,4],"value")
            modulovalidacion.valList([1,2,3,4],5,"len")
            modulovalidacion.valList([1,2,3,4],[1,2,7,5],"value")
            modulovalidacion.valList([1,2,3,4],2,"len")
            modulovalidacion.valList([1,2,3,4],5.0,"len")
            modulovalidacion.valList([1,2,3,4],4.0,6)
        else: 
            print("Ingrese, por favor, una opcion valida") 
        break
    if opcion==2: 
        palabra = str(input("Ingrese una palabra: "))
        clave = int(input("Ingrese una clave de cifrado: "))
        print("ELIJA UNA OPCION\nA.Cifrar\nB.Descifrar")
        menu1=str(input("Su opcion: "))
        if menu1 == "A":
            modulocifrado.cifrar(palabra,clave) 
        elif menu1== "B":
            modulocifrado.descifrar(palabra,clave) 
        else: 
            print("Ingrese, por favor, una opcion valida") 
        break
    else: print("Ingrese, por favor, una opcion valida. Para realizar esta accion, reinicie el programa") 
