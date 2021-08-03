def cifrado_cesar(pregunta, desplazamientos):
    abc ='abcdefghijklmnñopqrstuvwxyz'
    pregunta_lower = pregunta.lower() #string con el mensaje
    n = desplazamientos #numero de desplazamientos
    resultado = "" #String con el mensaje cifrado
    for letter in pregunta_lower: #letra in o
        if letter == " ":
            resultado += " "
        else:
            suma = abc.find(letter) + desplazamientos
            modulo = int(suma % len(abc))
            resultado += str(abc[modulo])
    return(resultado)




def codigo_cifrado(desplazamientos): #se crea  la chuleta con los desplazamientos.
    a = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z"
    b = cifrado_cesar(a, desplazamientos)
    b = b.upper()
    print(f"\n\n{b}\n▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼\n{a}")



