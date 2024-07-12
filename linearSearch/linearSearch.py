def linearSearch(list, key):
    for i in list:
        if list[i] == key:
            return f"O número {list[i]} encontra-se na posição {i} da lista"
    else:
        return -1

#Teste do código:

list = [2, 3, 4, 10, 40]
key = 10
print(linearSearch(list, key))

list = []
key = 15
print(linearSearch(list, key))

arr = [100, 200, 100, 300, 400]
key = 100
print(linearSearch(list, key))