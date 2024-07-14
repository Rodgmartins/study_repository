def findLargestElements(lista):
    if len(lista) < 3:
        print("A lista precisa conter pelo menos 3 valores.")
        return

    primeiro = segundo = terceiro = float('-inf')

    for num in lista:
        if num > primeiro:
            terceiro = segundo
            segundo = primeiro
            primeiro = num
        elif num > segundo:
            terceiro = segundo
            segundo = num
        elif num > terceiro:
            terceiro = num

    print(f"Os três maiores números são:{primeiro},{segundo},{terceiro}")


lista = [10, 4, 3, 50, 23, 90]
findLargestElements(lista)