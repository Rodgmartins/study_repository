def bubbleSort(lista):
    for n in range(len(lista),0,-1): #Leitura da lista
        shift = False # Inicia a variavél com valor "false"
        for i in range(0, n-1): #Inicia a ordenação de itens
            if lista[i] > lista[i+1]: #Verifica se o num anterior é maior que o prox
                lista[i], lista[i+1] = lista[i+1], lista[i] #altera a posiçao de itens da lista
                shift = True #Altera o valor em caso positivo p/ rodar apenas o 2 for
        if not shift:
            break #Se o valor voltar a ser "false", interrompe o codigo

#Pequeno teste do codigo
lista = [6, 3, 1, 2, 4, 5, 8, 7, 10, 9]
bubbleSort(lista)
print(lista)