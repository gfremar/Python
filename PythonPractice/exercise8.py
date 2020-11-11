print("Vamos a jugar a piedra papel o tijera")
seguir=True
opciones=["q","piedra","papel","tijera"]
continuar=["s","n"]
while seguir:
    player1=input("Jugador 1, introduce tu jugada (q para salir): ").lower()
    while player1 not in opciones:
        player1=input("Jugador 1, entrada incorrecta, prueba otra vez: ").lower()
    if player1==opciones[0]:
        print("Saliendo...")
        exit()
    player2=input("Jugador 2, introduce tu jugada (q para salir): ").lower()
    while player2 not in opciones:
        player2=input("Jugador 2, entrada incorrecta, prueba otra vez: ").lower()
    if player2==opciones[0]:
        print("Saliendo...")
        exit()
    print("El jugador 1 ha elegido ", player1)
    print("El jugador 2 ha elegido " + player2)
    if player1==player2:
        print("Empate. Seguid jugando")
    elif player1==opciones[1]:
        if player2==opciones[2]:
            print("El papel envuelve a la piedra. Vence el jugador 2")
        else:
            print("La piedra rompe la tijera. Vence el jugador 1")
    elif player1==opciones[2]:
        if player2==opciones[1]:
            print("El papel envuelve a la piedra. Vence el jugador 1")
        else:
            print("La tijera corta el papel. Vence el jugador 2")       
    else:
        if player2==opciones[1]:
            print("La piedra rompe la tijera. Vence el jugador 2")
        else:
            print("La tijera corta el papel. Vence el jugador 1")     
    juego=input("¿Quereis seguir jugando? (S/N): ").lower()
    while juego not in continuar:
        juego=input("¿Quereis seguir jugando? (S/N): ").lower()
    if juego==continuar[1]:
        print("Saliendo...")
        seguir=False

