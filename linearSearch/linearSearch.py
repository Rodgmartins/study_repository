def linearSearch(lista, key):
    for i in range(len(lista)):
        if lista[i] == key:
            return f"O número {lista[i]} encontra-se na posição {i} da lista"
    else:
        return -1


#Teste do código 1:
lista1 = [2, 3, 4, 10, 40]
key1 = 10
print(linearSearch(lista1, key1))
#Teste do código 2:
lista2 = []
key2 = 15
print(linearSearch(lista2, key2))
#Teste do código 3:
lista3 = [200, 400, 600, 800, 0]
key3 = 100
print(linearSearch(lista3, key3))