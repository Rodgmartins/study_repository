def countingSort(lista):

    max_value = max(lista)

    count = [0] * (max_value + 1)

    for num in lista:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    output = [0] * len(lista)
    for num in reversed(lista):
        output[count[num] -1] = num
        count[num] -= 1
    return output

#Testando o codigo

lista = [4, 2, 2, 8, 3, 3, 1]
sorted_lista = countingSort(lista)
print(sorted_lista)