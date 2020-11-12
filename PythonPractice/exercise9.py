import random
intentos=0
aleatorio=random.randint(1,9)
a=input("Introduce un número del 1 al 9. A ver si adivinas lo que he pensado. O escribe \"exit\" para salir: ")
while a.lower()!="exit" and int(a) not in range(1,10):
    a=input("Introduce un número del 1 al 9. A ver si adivinas lo que he pensado. O escribe \"exit\" para salir: ")
if a.lower()=="exit":
    exit()
while True:
    if int(a)==aleatorio:
        intentos+=1
        print("Muy bien, acertaste el número. Solo has necesitado " + str(intentos) + " intento/s.")
        intentos=0
        aleatorio=random.randint(1,9)
    elif int(a)<aleatorio:
        print("Huyyyy... Casi... Tu número es demasiado bajo. Prueba otra vez")
        intentos+=1
    else:
        print("Huyyyy... Casi... Tu número es demasiado alto. Prueba otra vez")
        intentos+=1
    a=input("Introduce un número del 1 al 9. A ver si adivinas lo que he pensado. O escribe \"exit\" para salir: ")
    while a.lower()!="exit" and int(a) not in range(1,10):
        a=input("Introduce un número del 1 al 9. A ver si adivinas lo que he pensado. O escribe \"exit\" para salir: ")
    if a.lower()=="exit":
        exit()