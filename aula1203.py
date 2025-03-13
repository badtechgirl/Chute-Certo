import numpy as np

# 1. Converta os elementos do array [3, 5, 9, 16, 25] para float.
array1 = np.array([3, 5, 9, 16, 25], dtype=float)
print(array1)

# 2. Dado o array [1.2, -3.6, 8.99999, 16.1], converta os seus elementos para int.
array2 = np.array([1.2, -3.6, 8.99999, 16.1], dtype=int)
print(array2)

# 3. Crie uma matriz 3x9 contendo apenas elementos com valor zero.
matriz3 = np.zeros((3, 9))
print(matriz3)

# 4. Crie uma matriz 6x7 de números inteiros contendo elementos com valor 1.
matriz4 = np.ones((6, 7), dtype=int)
print(matriz4)

# 5. Crie uma matriz identidade de tamanho 4.
matriz5 = np.eye(4)
print(matriz5)

# 6. Crie um array de números aleatórios entre 0 e 1 de tamanho 5.
array6 = np.random.rand(5)
print(array6)

# 7. Crie uma matriz 3x6 contendo números aleatórios de 0 a 5 (0, 1, 2, 3, 4, 5).
matriz7 = np.random.randint(0, 6, size=(3, 6))
print(matriz7)

# Considere a seguinte matriz para os exercícios 8 a 11:
matriz_ex = np.array([[4, 6, 8], [-4, 3, 2], [22, -15, 12]])

# 8. Informe o código para exibir o valor máximo da matriz.
print(matriz_ex.max())

# 9. Qual o código para exibir o valor mínimo da matriz?
print(matriz_ex.min())

# 10. Como fazer para imprimir na tela a soma dos elementos da matriz?
print(matriz_ex.sum())

# 11. Escreva o código necessário para exibir a média dos elementos da matriz.
print(matriz_ex.mean())

# Considere o seguinte array para os exercícios 12 a 16.
array_ex = np.array([13, -2, 6, 8, 23, 15, 3, 90, 4, 10, 56, 12])

# 12. Exibir o 4º elemento do array.
print(array_ex[3])

# 13. Exibir os 3 últimos elementos do array.
print(array_ex[-3:])

# 14. Exibir os elementos a partir da posição 2.
print(array_ex[2:])

# 15. Exibir um array entre o 2º e o 6º elementos. O 6º elemento deve estar presente.
print(array_ex[1:6])

# 16. Escreva o código que resulta na exibição do seguinte array: [23 15 3 90]
print(array_ex[4:8])

# Considere a seguinte matriz para os exercícios de 17 a 20
matriz_ex2 = np.array([[1, 3, 16, -25, 14], [2, 0, 10, 5, 17], [19, 4, 8, 15, 13], [7, 12, -5, 14, 0]])

# 17. Escreva o código para exibir a 3ª linha da matriz.
print(matriz_ex2[2])

# 18. Escreva o código para exibir a 4ª coluna
print(matriz_ex2[:, 3])

# 19. Escreva o código para exibir o elemento de valor 10.
print(matriz_ex2[1, 2])

# 20. Escreva o código que resulta na seguinte matriz:
# [[0 10 5]
#  [4 8 15]]
print(matriz_ex2[1:3, 1:4])

# Dada a seguinte matriz:
matriz_ex3 = np.array([[2, -1, 15, 24], [-3, 18, 4, 25], [9, 10, -13, 7]])

# Crie uma nova matriz, atribuindo o valor 1 para os números ímpares, e 2, para os números pares, 
# utilizando a biblioteca numpy.
matriz_nova = np.where(matriz_ex3 % 2 == 0, 2, 1)
print(matriz_nova)