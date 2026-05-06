#Ejercicio: Desarrolle un programa que permita ingresar 5 numeros y al finalizar
#retorne cuantos numeros pares ingreso el usuario.
#nota: solo se deben considerar los numeros positivos.

print("Bienvenido al programa de conteo numerico")

num = int(input("ingrese un numero: "))
contador = 0

for num in range(0, 6, 1):
    if num % 2 == 0 and num > 0:
        contador = contador + 1
        print("El numero de numeros pares ingresados es: ", contador)
    else:
        print("El numero ingresado no es par o es negativo")