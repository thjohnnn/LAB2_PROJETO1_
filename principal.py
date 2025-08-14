import random
from statistics import mean

def sorteia_sete_e_media():
    numeros = [random.randint(0, 100) for _ in range(7)] 
    return numeros, mean(numeros)


print(cumprimento("João Pedro Paravidino"))
nums, media = sorteia_sete_e_media()
print("Números sorteados:", nums)
print("Média:", round(media, 2))