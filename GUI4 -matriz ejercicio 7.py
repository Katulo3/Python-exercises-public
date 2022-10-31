# matriz inicial
matriz: list = [[1, 5, 1], [2, 1, 2], [3, 0, 1], [1, 4, 4]]

# suma0 = sum((matriz_a)[0][0:8])
# suma1 = sum((matriz_a)[1][0:8])
# suma2 = sum((matriz_a)[2][0:8])
# suma3 = sum((matriz_a)[3][0:8])
# Matriz final- forma 1
# matriz_b = [[1, 5, 1, suma0],
#             [2, 1, 2, suma1],
#             [3, 0, 1, suma2],
#             [1, 4, 4, suma3]
#  ]

# forma 2
matriz[0] += [(sum(matriz[0]))]
matriz[1] += [(sum(matriz[1]))]
matriz[2] += [(sum(matriz[2]))]
matriz[3] += [(sum(matriz[3]))]

print("El resultado es: " + str(matriz))
print(type(matriz))
