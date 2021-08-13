from array import *

lista = array('i', [])

for i in range(4):
    numero = int(input("Digite um número: "))
    lista.append(numero)

med = sum(lista) / len(lista)

print("A média é igual a:", med)

if med > 0:
    print("Média positiva")

elif med < 0:
    print("Média negativa")
    
else:
    print("Média neutra") 

