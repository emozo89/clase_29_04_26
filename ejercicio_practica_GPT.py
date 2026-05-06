#desarrolle un programa que permita ingresar 7 numeros enteros hasta completar 7 numeros positivos
#al finalizar, imprimir:
# - cantidad de numeros pares
# - cantidad de numeros impares
#Nota!: - numeros negativos no se consideran
#       - si el usuario ingresa un número negativo mostrar ERROR y solicitar nuevamente

print ("Bienvenido al programa de conteo numerico")
contador = 0
contador1 = 0
contador2 = 0


while contador < 7:
    num = int(input("Ingrese un numero: "))

    if num > 0:
        contador = contador + 1
        if num % 2 == 0:
            contador1 = contador1 + 1
        else:
            contador2 = contador2 + 1
    else:
        print("Numero invalido!, reingresar")
print(f"Cantidad de numeros pares: {contador1}, cantidad de numeros impares: {contador2}")