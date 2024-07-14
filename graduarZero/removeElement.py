#Código Inicial:
def removeElement(lista, valor):
    listaOutput =[]
    for i in lista:
        if valor in lista:
            lista.remove(valor)
            listaOutput.append(lista)
    return listaOutput

#Teste do código:
lista = [3,2,2,3]
valor = 3
print(removeElement(lista, valor)) #Output: [[2, 2], [2, 2]]


#Código corrigido e melhorado:
def removeElement2(lista, valor):
    listaOutput2 = []
    for i in lista:
        if i != valor:
            listaOutput2.append(i)
    return listaOutput2

#teste do codigo removeElement2:
lista = [1, 2, 3, 4, 2, 5, 2]
valor = 2
print(removeElement2(lista, valor)) #Output: [1, 3, 4, 5]