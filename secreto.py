print("-----------------JUEGO DEL NUMERO SECRETO----------------")

secreto = 104
jugador = 0

while secreto != jugador:
    jugador = int(input("Escribe el numero secreto: "))
    if jugador > secreto:
        print("Tu numero es mayor al secreto")
    elif jugador < secreto:
        print("Tu numero es menor al secreto")
    else:
        print("Felicitaciones mi amor encontraste el numero eso merece un chikitingo")
