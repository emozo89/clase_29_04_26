#ESTRUCURAS DE DATOS - investigar tuplas, diccionarios, conjuntos
#INVESTIGAR - vectores, arreglos, matrices


#listas
#de esta forma obtenemos el elemento dentro de la lista, el indice es el numero que representa la posicion del elemento dentro de la lista, el indice inicia en 0
#numeros = [2, 5, 1, 4]

#print(f"Elemento índice 2 -> {numeros[2]}")

#          0  1  2  3  4
#numeros = [2, 5, 1, 4, 7]
#print(f"Elemento índice 2 -> {numeros[2]}")

# print("Recorrer con ciclo for")
# for num in numeros:
#    if num % 2 == 0:
#       print(f"{num} es par")

#    print(num)

#Recorrer con while
#print("Elementos de la lista ->", len(numeros))
#print("Recorrer con ciclo while")
#i = 0
#while i < len(numeros):
#   num = numeros[i]
#   if num % 2 == 0:
#      print(f"{num} es par y está en el índice {i}")

#  print(num)
#   i = i + 1

#print(numeros)

#Métodos de una lista
edades = []
edades.append(48)
edades.append(27)
edades.append(26)
edades.append(28)
edades.append(29)
edades.append(30)
print(edades)
#Insertar en el índice 2 el elemento 36
edades.insert(2, 36)
print(edades)
#Elimina elemento 28 de la lista
#edades.remove(28)
del edades[4]
print(edades)
elemento_cero = edades.pop(0)
print("Se eliminó el elemento del índice cero, su valor era -> ", elemento_cero)
print(edades)

#Modificar un elemento
edades[2] = 1
print(edades)