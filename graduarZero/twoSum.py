def twoSum(lista, target):
    lista_comp = {}

    for i, num in enumerate(lista):
        soma = target - num
        if soma in lista_comp:
            return [lista_comp[soma],i]
        lista_comp[num] = i
    return None

# Exemplo de uso:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]