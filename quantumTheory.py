import libcplx as com
import ComplexVector as vm
import numpy as np

# SIMULE EL PRIMER SISTEMA CUÁNTICO DESCRITO EN LA SECCIÓN 4.1.
# PUNTO 1
def prob_position(ket, position):
    num = com.mod(ket[position]) ** 2
    deno = vm.vector_norm(ket) ** 2
    return round(num/deno, 3)


def bra(ket):
    for num in ket:
        if isinstance(num, list):
            num[1] *= -1
        else:
            num *= -1
    return ket

# PUNTO 2(SECCIÓN 4.1.) y 1 (SECCIÓN 4.)
def transition(ket1, ket2):
    braket2 = bra(vm.transpose(ket2)[0])
    norm1 = vm.vector_norm(vm.transpose(ket1)[0])
    norm2 = vm.vector_norm(vm.transpose(ket2)[0])
    norm = norm1 * norm2
    aux = vm.transpose(ket1)
    prob = vm.dot_product(braket2, vm.transpose(ket1)[0])
    ans = com.mult([1/norm, 0], prob)
    return ans

#COMPLETE LOS RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4.
# PUNTO 2
def media(observable, ket):
    bra_ket = bra(ket)
    res1 = vm.action(observable, ket)
    res2 = vm.dot_product(res1, bra_ket)
    return res2


# PUNTO 2
def variance(observable, ket):
    braket = bra(ket)
    miu = media(observable, ket)
    ident_miu = [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
    for i in range(len(observable)):
        for j in range(len(observable[i])):
            if i == j:
                ident_miu[i][j] = vm.additive_inverse_mat(miu)
    ident_miu = vm.add_mat(ident_miu, observable)
    sqobs = vm.mult_mat(ident_miu, ident_miu)
    ans1 = vm.action(sqobs, ket)
    ans2 = vm.dot_product(ans1, braket)
    return ans2

# PUNTO 3
def eigenValuVect(matrix):
    evalues, evectors = np.linalg.eig(matrix)
    values = []
    vectors = []
    for i in range(len(evalues)):
        values += [(evalues[i].real, evalues[i].imag)]
    for i in range(len(evectors)):
        vector = []
        for j in range(len(evectors[0])):
            vector += [(evectors[i][j].real, evectors[i][j].imag)]
        vectors += [vector]
    return values, vectors


# REALICE LOS SIGUIENTES PROBLEMAS E INCLUYALOS COMO EJEMPLOS
# 4.3.1
def ex1():
    vector = [[[1, 0]], [[0, 0]]]
    observable = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    observation = vm.action(observable, vector)
    values, vectors = eigenValuVect(observable)
    print('Observation result: ', observation)
    print('EigenValues: ', values)
    print('EigenVectors: ', vectors)


# 4.3.2
def ex2():
    vector = [[[1, 0]], [[0, 0]]]
    observable = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    values, vectors = eigenValuVect(observable)
    for i in range(len(vectors)):
        print(transition(vector, vectors[i]))


# 4.4.1
def ex3():
    matrix1 = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    matrix2 = [[[(2**(1/2))/2, 0], [(2**(1/2))/2, 0]], [[(2**(1/2))/2, 0], [-(2**(1/2))/2, 0]]]
    if vm.is_unitary(matrix1) and vm.is_unitary(matrix2):
        print(vm.is_unitary(vm.mult_mat(matrix1, matrix2)))


# Si se quiere ver la solución de los puntos se borra los  """
"""
def main():
print('EJEMPLO 4.3.1')
ex1()
print()
print('EJEMPLO 4.3.2')
ex2()
print()
print('EJEMPLO 4.4.1')
ex3()
"""