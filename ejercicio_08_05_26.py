
#def amigos(num1, num2):
#    suma = 0
#    for i in range(1, num1):
#        if num1 % i == 0:
#            suma = suma + i
#    if suma == num2:
#        suma = 0
#        for i in range(1, num2):
#            if num2 % i == 0:
#                suma = suma + i
#        if suma == num1:
#           return True
#    return False
#print(amigos(220, 284))


#1.-Desarrolle una funcion que retorne el factorial de un numero

def factorial(num):
    
    contador = 1
    resultado = 1
    
    while contador <= num:
        resultado = resultado * contador
        contador = contador + 1
        
    return resultado

numero = int(input("ingrese un numero: "))
print("el factorial es:", factorial(numero))


#2.- Desarrolle una funcion que reciba dos listas y retorne una lista con la suma cruzada.
#Opción con for

def suma_cruz(lista1, lista2):
    resultado = []
    
    for i in range (len(lista1)):
        suma = lista1[i] + lista2[i]
        resultado.append(suma)
        
    return resultado

lista1 = [2, 4, 6, 8, 10 ]
lista2 = [10, 20, 30, 40, 50]

print(suma_cruz(lista1, lista2))
