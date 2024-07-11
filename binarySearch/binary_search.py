def pesquisaBinario(nums, menor, maior, item):
    if menor <= maior:
        medio = (menor+maior)//2
        if nums[medio] == item:
            return medio
        elif item < nums[medio]:
            return pesquisaBinario(nums, menor, medio-1, item)
        else:
            return pesquisaBinario(nums, medio+1, maior, item)
    else:
        return -1