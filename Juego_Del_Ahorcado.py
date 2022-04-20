from ast import While
from random import choice

#Creo una lista contenedora de palabras las cuales serán las que el usuario intentará adivinar
marcasDeAutos = ["ford", "nissa", "mazda", "toyota", "bmw", "ferrari", "audi", "porsche", "volkswagen","chery", "daewoo", "hyundai","cadillac", "chevrolet", "dodge", "jeep", "tesla", "bugatti", "peugeot", "renault", "fiat", "lamborghini", "maserati", "pagani","honda", "acura", "mitsubishi","suzuki", "bentley", "jaguar", "rolls-royce"]
ciudades = ["san-francisco", "amsterdam", "manchester", "copenhague", "nueva-york", "praga", "tel-aviv", "tokio"," los-angeles", "chicago","londres", "barcelona", "madrid", "melbourne", "shanghai", "hong-kong", "milan", "singapur", "miami", "dubai", "beijing", "paris", "budapest", "sao-paulo", "roma", "moscu","Bangkok",""]
paises = ["francia", "mexico", "estados-unidos", "italia", "alemania","turquia", "emiratos-arabes", "grecia", "rusia", "rumania", "malasia", "portugal", "japon", "indonesia", "sudafrica", "puerto-rico", "costa-rica", "ucrania", "belgica", "corea-del-sur", "australia", "colombia", "venezuela", "argentina", "peru","brasil", "uruguay", "paraguay", "bolivia", "ecuador", "chile", "el-salvador","guatemala","catar","luxemburgo", "vietnam","nueva-zelanda","panama", "jamaica", "austria"]
colores = ["negro", "azul", "marron", "gris","verde", "naranja", "rosa", "morado", "rojo", "blanco", "amarillo", "turquesa", "beige", "magenta", "lila", "violeta", "lavanda", "salmon", "fucsia", "ocre","granate", "dorado", "plateado"]
planetas = ["mercurio", "venus","tierra","marte", "jupiter", "saturno", "urano", "neptuno", "pluton"]

#se elige aleatoriamente una palabra random de la lista
autosRandom = choice(marcasDeAutos)
ciudadesRandom = choice(ciudades)
paisesRandom = choice(paises)
coloresRandom = choice(colores)
planetasRandom = choice(planetas)

#Creando el bucle de lo que seria el juego y la interfaz donde estará la información (Como jugar, vidas, palabra a adivinar, numero de letras, etc.)
letrasAdivinadas = []
vidas = 6

print("#" * 140)
print()
print("""\t\t\t\t\t***** JUEGO DEL AHORCADO. *****
INFO: Tendrás que adivinar una Palabra letra por letra, cada vez que falles se te restará una vida de las 6 en total que tienes.\n  QUE NO SE TE ACABEN!!
""")
print("#" * 140)
print("""\tCATEGORIAS:
1.- Marcas de Autos.
2.- Ciudades.
3.- Paises.
4.- Colores.
5.- Planetas.

NOTA: Para escoger las categorias debe usar sus numeros correspondientes.
""")
print("#" * 140)

try:    
    opcion = int(input("Con cual categoria desea jugar? "))
except ValueError:
    print("ERROR! Debe ingresar un 'NÚMERO' de acuerdo a la categoria...")

while True:
    if opcion == 1:
        print("Ha Escogido: Marcas de Autos")
        palabraRandom = "".join(autosRandom)
        break
    elif opcion == 2:
        print("Ha Escogido: Ciudades")
        palabraRandom = "".join(ciudadesRandom)
        break
    elif opcion == 3:
        print("Ha Escogido: Paises")
        palabraRandom = "".join(paisesRandom)
        break
    elif opcion == 4:
        print("Ha Escogido: Colores")
        palabraRandom = "".join(coloresRandom)
        break
    elif opcion == 5:
        print("Ha Escogido: Planetas")
        palabraRandom = "".join(planetasRandom)
        break
        

while True:
    respuesta = input('Adivine una letra de la Palabra o escriba "SALIR": ').lower()

    if respuesta == "salir":
        print("Gracias por jugar!")
        break
    elif respuesta != 1 and respuesta.isnumeric():
        print("ERROR! Debe ingresar letras.")
    else:
        
        if respuesta in letrasAdivinadas:
            print("Ya haz ingresado esa letra... -_- \nIntenta con otra!!")
        else:
            letrasAdivinadas.append(respuesta)

            if respuesta in palabraRandom:
                print("Felicidades!! Haz ADIVINADO una letra :D")
            else:
                vidas -= 1
                print("INCORRECTO!!")
                print(f"-1 Vida: {vidas} en total.")     
    
    if vidas == 0:
        print("""Haz perdido TODAS tus vidas! D:\n\tGAME OVER...""")
        break

    progreso = ""
    conteoDeLetras = 0

    for i in palabraRandom:
        if i in letrasAdivinadas:
            progreso += i
        else:
            progreso += "_"
            conteoDeLetras += 1
    
    print(progreso)

    if conteoDeLetras == 0:
        print("FELICIDADES!! Lo adivinaste CORRECTAMENTE! :D\nHAZ GANADO!!!")
        print(f"La palabra era: {palabraRandom}")
        break
        