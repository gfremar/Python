cadena=input("introduce una cadena de texto: ")
a=[]
b=[]
for letra in cadena:
    if letra != " ":
        a.append(letra)
i=len(a)
while i>0:
    b.append(a[i-1])
    i-=1
if a == b:
    print("Esta cadena es un palindromo")
else:
    print("Esta cadena no es un palindromo")