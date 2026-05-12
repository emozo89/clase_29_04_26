#2.- Desarrolle una funcion que reciba dos listas y retorne una lista con la suma cruzada.
#Opción con while

def suma_cruzada(lista1, lista2):

    resultado = []
    i = 0

    while i < len(lista1):

        suma = lista1[i] + lista2[i]
        resultado.append(suma)
        i = i + 1
    return resultado

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

print(suma_cruzada(lista1, lista2))