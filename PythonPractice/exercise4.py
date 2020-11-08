num=int(input("Introduce un número para buscar sus divisores: "))
total=range(1,num+1)
divisores=[]
for posi in total:
    if num % posi == 0:
        divisores.append(posi)
print("Los divisores de " + str(num) + " son: ")
for divisor in divisores:
    print(str(divisor) + " ")
if len(divisores) == 2:
    print(str(num) + " es un número primo")