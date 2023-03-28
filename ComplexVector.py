import libcplx
from libcplx import *
def sumVec(v1,v2):
    resultado = []
    if(len(v1) == len(v2)):
        for i in range(len(v2)):
            resultado = v1[i] + v2[i]
    return resultado

def restaVec(v1,v2):
    if (len(v1) == len(v2)):
        for i in range(len(v1)):
            v1[i] = restaplx(v1[i], v2[i])
        return v1

def inversavec(v):
    ans_vector = []
    for i in range(len(v)):
        ans_vector.append(libcplx.multcplx(v[i], [-1, 0]))
    return ans_vector

def vectoPorEscalar(es,vec):
    for i in range(len(vec)):
        vec[i] = multcplx(es, vec[i])
    return vec

def adicionMat(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = sumacplx(m1[i][j], m2[i][j])
    return m1

def inversaMat(m):
    ans = []
    for i in range(len(m)):
        ans.append([])
        for j in range(len(m[i])):
            ans[i].append(libcplx.multcplx(m[i][j], [-1, 0]))
    return ans


def matrizPorEscalar(es,m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = multcplx(es, m[i][j])
    return m

def transpuesta(m):
    temp = [[0 for i in range(len(m))] for j in range(len(m[0]))]
    for i in range(len(m[0])):
        for j in range(len(m)):
            temp[i][j] = m[j][i]
    return temp

def conjugada(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = conjugadocplx(m[i][j])
    return m

def adjunta(m):
    return conjugada(transpuesta(m))

def productoMat(m1,m2):
    if (len(m1[0]) == len(m2)):
        new = [[[0, 0] for i in range(len(m2[0]))] for j in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                piv = [0, 0]
                for k in range(len(m2)):
                    mul = multcplx(m1[i][k], m2[k][j])
                    piv = sumacplx(mul, piv)
                new[i][j] = piv
        return new

def accion(m,v):
    if (len(v) == len(m[0])):
        new = [[0, 0] for i in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                piv = multcplx(m[i][j], v[j])
                new[i] = sumacplx(new[i], piv)
        return new


def action(m, v):

    return productoMat(m, v)

def productoInternVec(v1,v2):
    new = [0, 0]
    for i in range(len(v1)):
        new = sumacplx(new, multcplx(v1[i], v2[i]))
    return new

def normaVec(v):
    return abs(productoInternVec(v, v)[0]) ** (1 / 2)

def distaciaVec(v1,v2):
    return normaVec(restaVec(v1, v2))



def matrizUnitaria(m):
    if len(m) == len(m[0]):
        id = [[[0, 0] for j in range(len(m[0]))] for i in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i == j:
                    id[i][j] = [1, 0]
        aux = adjunta(m)
        product = productoMat(aux, m)
        ans = True
        for i in range(len(m)):
            for j in range(len(m)):
                if product[i][j] != id[i][j]:
                    ans = False
        if ans:
            return True
        else:
            return False
    else:
        return False

def matrizHermitiana(m):
    return m == adjunta(m)

def productoTensor(m1,m2):
    tem = []
    if (type(m1[0][0]) is int) and (type(m2[0][0]) is int):
        for i in range(len(m1)):
            for j in range(len(m2)):
                tem.append(multcplx(m1[i], m2[j]))
        return tem
    elif (len(m1) == len(m1[0])) and (len(m2) == len(m2[0])):
        for i in range(len(m1)):
            for j in range(len(m2)):
                piv = []
                for k in range(len(m1[0])):
                    piv += vectoPorEscalar(m1[i][k][:], m2[j][:])
                tem.append(piv)
        return tem
