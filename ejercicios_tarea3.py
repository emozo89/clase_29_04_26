#3.-Poblar de forma automatica una lista de tamaño 10 con los
#1eros numeros primos (divisibles por 1 y por si mismos)
#la lista debe quedar así: [2,3,5,7,11,13,17,19,23,29]
#debe ser automatico, porque si pidiera los 1er 100 o 1000
#debe agregarlos a la lista

lista = []
i = 0
es_primo = True
no_primo = False

while i < 10:
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    i = i + 1

for i in range(len(lista)):
    if lista [i] == 1:
        print(lista[i], "no es primo")
    else:
        es_primo = True

    for j in range(2, lista[i]):

        if lista[i] % j == 0:
            es_primo = False
            break
        
    if es_primo:
        print(lista[i], "es primo")
    else:
        print(lista[i], "no es primo")