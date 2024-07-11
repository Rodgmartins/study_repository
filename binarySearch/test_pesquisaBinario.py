from binary_search import pesquisaBinario
def teste_pesquisaBinario():
    # Teste 1: Item presente na lista
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 6
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == 5, f"Erro no teste 1: esperado 5, obteve {resultado}"

    # Teste 2: Item ausente na lista
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 11
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == -1, f"Erro no teste 2: esperado -1, obteve {resultado}"

    # Teste 3: Lista vazia
    nums = []
    item = 1
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == -1, f"Erro no teste 3: esperado -1, obteve {resultado}"

    # Teste 4: Lista com um único elemento (item presente)
    nums = [1]
    item = 1
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == 0, f"Erro no teste 4 (presente): esperado 0, obteve {resultado}"

    # Teste 4: Lista com um único elemento (item ausente)
    nums = [1]
    item = 2
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == -1, f"Erro no teste 4 (ausente): esperado -1, obteve {resultado}"

    # Teste 5: Lista com elementos repetidos
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]
    item = 4
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado in [3, 4, 5], f"Erro no teste 5: esperado 3, 4 ou 5, obteve {resultado}"

    print("Todos os testes passaram!")

# Executando os testes
teste_pesquisaBinario()