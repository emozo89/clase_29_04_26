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
            
            
#3.-Poblar de forma automatica una lista de tamaño 10 con los
#1eros numeros primos (divisibles por 1 y por si mismos)
#la lista debe quedar así: [2,3,5,7,11,13,17,19,23,29]
#debe ser automatico, porque si pidiera los 1er 100 o 1000
#debe agregarlos a la lista



