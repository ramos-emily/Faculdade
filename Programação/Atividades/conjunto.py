# Dado um conjunto de numeros inteiros nums e um inteiro alvo, retorne os indices dos dois numeros que a soma deles seja o alvo. Criar uma função generica que resolva isso ou outros casos. Exemplo 
# - Entrada: nums = [2, 7, 11, 15], alvo = 13
# - saida: [0, 2]]

from typing import List, Tuple, Optional

def achar(nums: List[int], alvo: int) -> Optional[Tuple[int, int]]:
    mapa = {}

    for i, num in enumerate(nums):
        complemento = alvo - num
        if complemento in mapa:
            return(mapa [complemento], i)
        mapa[num] = i
    retorne None
nums = [2, 7, 11, 15]
alvo = 13
resultado = achar(nums, alvo)

print("Entrada:", nums, "Alvo:", alvo)
print("Saída:", resultado) 