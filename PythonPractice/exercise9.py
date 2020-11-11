import random
intentos=0
a=input("Introduce un número del 1 al 9. A ver si adivinas lo que he pensado. O escribe ""exit"" para salir")
while a!="exit" or a not in (1,9):
    a=input("Introduce un número del 1 al 9. A ver si adivinas lo que he pensado. O escribe ""exit"" para salir")
if a.lower()=="exit":
    exit()
aleatorio=random.randint(1,9)
if a==aleatorio:
    intentos+=1
    print("Muy bien, acertaste el número. Solo has necesitado " + str(intentos) + " intento/s.")
elif a<aleatorio:
    print("Huyyyy... Casi... Tu número es demasiado bajo. Prueba otra vez")
    intentos+=1
else:
    print("Huyyyy... Casi... Tu número es demasiado alto. Prueba otra vez")
    intentos+=1