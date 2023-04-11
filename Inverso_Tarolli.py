import math
import numpy as np
import random

#INVERSO DA MATRIZ
def inversao_raiz(x):
    inversa = 1/math.sqrt(x)
    return inversa
  
  x=random.randint(1, 10)
  print(inversao_raiz(x))

#RESOLUÇÃO TAROLLI COM NumPy
# Define uma matriz simétrica positiva definida A
A = np.array([[10, 2, 3], [2, 15, 4], [3, 4, 20]])

# Define um vetor b
b = np.array([5, 7, 9])

# Resolve o problema de Tarolli usando a função solve da biblioteca NumPy
x = np.linalg.solve(A, b)

print(x)
