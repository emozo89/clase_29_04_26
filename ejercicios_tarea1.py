#1.-Desarrolle un programa que permita ingresar 10 numeros al usuario
#al finalizar desplegar los elementos y en que posicion de la lista
#estan los mayores al promedio

numeros = []
i = 0

while i < 10:
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
    i = i + 1

suma = 0

for numero in numeros:
    suma = suma + numero
    
promedio = suma / len(numeros)

for i in range (len(numeros)):
    
        if numeros[i] > promedio:
            print(numeros[i], "esta en posicion", i)
            




