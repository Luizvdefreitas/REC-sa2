from array import *

lista = array('i', [])

for i in range(21):
    numero = int(input("Digite um número: "))
    lista.append(numero)

med = sum(lista) / len(lista)

print('Média é igual a %.2f' %  med)


print("maior número é: ", max(lista))
print("menor número é: ", min(lista))