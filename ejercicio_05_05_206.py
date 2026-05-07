#Ejercicio: Desarrolle un programa que permita ingresar 5 numeros y al finalizar
#retorne cuantos numeros pares ingreso el usuario.
#nota: solo se deben considerar los numeros positivos.

print("Bienvenido al programa de conteo numérico")
positivos = 0
pares = 0
ciclos = 5

while positivos < ciclos:
    num = int(input("Ingrese un numero: "))
    
    if num > 0:
        positivos = positivos + 1
        if num % 2 == 0:
            pares = pares + 1
    else:
        print("Error!")
print(f"De los 5 ingresos, {pares} fueron numeros pares")