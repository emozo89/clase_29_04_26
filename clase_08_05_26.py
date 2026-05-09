num = int(input("Ing. número :"))

def es_primo(numero):
   divisibles = 0

   for x in range(1, numero + 1):
      if numero % x == 0:
         divisibles = divisibles + 1

   if divisibles == 2:
      return True
   else:
      return False
   

def los_primeros_numeros_primos(cuantos):
   contar_primo = 0
   n = 1
   while contar_primo < cuantos:
      if es_primo(n):
          print(f"{contar_primo} -> {n} es primo")
          contar_primo = contar_primo + 1

      n = n + 1


