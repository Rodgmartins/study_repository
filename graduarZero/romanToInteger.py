def transformToInteger(num_romano: str) -> int:
    #Lista de simbolos romanos
    listaSymbol = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }

    N = len(num_romano) #Descobre qts caracteres tem a string
    i = N-1
    output = 0
    while i >= 0: #Enquanto i for maior ou igual a zero, rode este command
        #Se i for menor que o indice válido AND valor atual é menor que o proximo valor:
        if i < N-1 and listaSymbol[num_romano[i]] < listaSymbol[num_romano[i+1]]:
            #Subtrai o valor do num_romano atual.
            output -= listaSymbol[num_romano[i]]
        else: #Adiciona o valor de num_romano atual
            output += listaSymbol[num_romano[i]]
        i -= 1 # Exclui o valor de "i" para ir para o proximo valor de num_romano
    return output

#Testando código:
#teste1
num_romano = "MCMXCIV"
print(transformToInteger(num_romano))
#teste2
num_romano2 = "LVIII"
print(transformToInteger(num_romano2))

#Consegui fazer o desafio com a ajuda deste video: https://www.youtube.com/watch?v=zCqaFVYoPBw