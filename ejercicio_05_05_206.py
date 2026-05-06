#Ejercicio: Desarrolle un programa que permita ingresar 5 numeros y al finalizar
#retorne cuantos numeros pares ingreso el usuario.
#nota: solo se deben considerar los numeros positivos.

print("Bienvenido al programa de conteo numérico")
contador = 0
contador2 = 0
ciclos = 5

while contador < ciclos:
    num = int(input("Ingrese un numero: "))
    
    if num > 0:
        contador = contador + 1
        if num % 2 == 0:
            contador2 = contador2 + 1
    else:
        print("Error!")
print(f"De los 5 ingresos, {contador2} fueron numeros pares")
