import ComplexVector
from ComplexVector import *
import libcplx
import matplotlib.pyplot as plot
import numpy as np

# Función auxiliar
def accion(mat, vec):
    if len(mat[0]) == len(vec):
        m = [[0 for i in range(len(vec[0]))] for j in range(len(mat))]
        for row in range(len(mat)):
            for column in range(len(vec[0])):
                for aux in range(len(mat[0])):
                    m[row][column] = round(m[row][column] + (mat[row][aux] * vec[aux][column]), 3)
        return m

# Función auxiliar
def mod(c):
    ans = (c[0] ** 2 + c[1] ** 2) ** 0.5
    return round(ans, 3)


# Punto 1
def canicas(mat, vec, t):

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]:
                mat[i][j] = 1
            else:
                mat[i][j] = 0
    ans = vec
    for i in range(t):
        ans = accion(mat, ans)
    return ans

# Punto 2
def sistemaProbabilistico(mat, vec, times):
    for i in range(times):
        vec = accion(mat, vec)
    return vec

# Punto 3
def sistemaProbabilisticoCuantico(mat, vec, times, ):
    ans = vec
    for i in range(times):
        ans = ComplexVector.action(mat, ans)
    for i in range(len(ans)):
        ans[i][0] = round(libcplx.modulocplx(ans[i][0]) ** 2, 3)
    return ans


def multipleSlit(mat, vec, times):
    return sistemaProbabilistico(mat, vec, times)

# Punto 4
def grafico(prob):
     estados = [x for x in range(len(prob))]
    fig, ax = plt.subplots()
    ax.set_ylabel('Probabilidades')
    ax.set_xlabel('Estados')
    ax.set_title('Sistema Cuantico')
    plt.bar(estados, prob)
    plt.savefig('probabilities.png')
    plt.show()
