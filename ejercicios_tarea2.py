#2.-Ordenar de manera ascendente una lista de tamaño 10
#previamente poblada con numeros (no se puede usar el metodo sort)

numeros = []
i = 0

while i < 10:
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
    i = i + 1

#ordanamiento

for i in range(len(numeros)):
    
    for j in range(len(numeros) -1-i):
        
        if numeros[j] > numeros[j + 1]:
            
            aux = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = aux
            
print(numeros)
