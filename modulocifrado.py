#MODULO 2 

#CIFRADO 

palabra = ""
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def descifrar(palabra, clave): 
    texto = ""
    for caracter in palabra.lower():
        if caracter in letras:
            indice = letras.index(caracter)
            nuevo_indice = (indice + clave) % len(letras)
            texto += letras[nuevo_indice]
    print(texto)

def cifrar(palabra, clave):
    texto = ""
    for caracter in palabra.lower():
        if caracter in letras:
            indice = letras.index(caracter)
            nuevo_indice = (indice - clave) % len(letras)
            texto += letras[nuevo_indice]
    print(texto)

