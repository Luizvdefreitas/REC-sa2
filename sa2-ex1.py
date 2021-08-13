#Atividade numero 1
L = [5, 7, 2, 9, 4, 1, 3]

# a) tamanho da lista;
tamanho = len(L)

print("A lista possui", tamanho, "números")

# b) maior valor da lista;
maior = max(L)

print("O maior número é:", maior)

# c) menor valor da lista;
menor = min(L)

print("O menor número é:", menor)

# d) soma de todos os elementos da lista;
soma = sum(L)

print("A soma de todos os números é igual a:",soma)


# e) lista em ordem crescente;
L.sort()
print("Ordem crescente:",L)

# f) lista em ordem decrescente.

L.sort(reverse=True)
print("Ordem descrescente:",L)