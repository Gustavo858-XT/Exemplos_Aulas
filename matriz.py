matriz = [
    [3,4,7,8],
    [1,3,6,2],
    [6,9,7,8],
    [7,5,0,8],
]
lista = matriz[0] # Retorna a primeira lista [3,4,7,8]
print(lista)
print(f"O elemento da linha 1 e coluna 2 = {matriz[1][2]}")
# Primeiro indice pega a linha e o segundo a coluna
print(f"O elemento da linha 2 e coluna 1 = {matriz[2][1]}")
# Modificar os valores de uma matriz 
matriz[1][2] = 10
print(matriz)