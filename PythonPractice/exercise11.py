num=int(input("Introduce un número para comprobar si es primo: "))
def esprimo(num):
    total=range(1,num+1)
    divisores=[]
    for posi in total:
        if num % posi == 0:
            divisores.append(posi)
    if len(divisores) == 2:
        return(str(num) + " es un número primo")
    else:
        return(str(num) + " no es un número primo")
print(esprimo(num))