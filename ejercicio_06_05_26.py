#desarrolle un programa que permita poblar una lista de tamaño 50 con numeros 0 y 1, 
#luego recorra la lista

num = []
for n in range(50):
    num.append(n % 2)
print(num)

#modo profesor
numeros = []
for i in range(0, 50, 1):
   numeros.append(i % 2)

print(numeros)