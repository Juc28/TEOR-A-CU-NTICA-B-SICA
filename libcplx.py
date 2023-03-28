#Autor : Erika Juliana Castro Romero
import math

def sumacplx(c1,c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    resultado = (real,img)
    return resultado

def restaplx(c1,c2):
    real = c1[0] - c2[0]
    img = c1[1] - c2[1]
    resultado = (real,img)
    return resultado

def multcplx(c1,c2):
    real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    img = (c1[0]*c2[1])+(c1[1]*c2[0])
    resultado = (real,img)
    return resultado

def divicplx(c1,c2):
    real = ((c1[0]*c2[0]) + (c1[1]*c2[1]))/((c2[0]^2)+(c2[1]^2))
    img = ((c2[0]*c1[1]) - (c1[0]*c2[1]))/((c2[0]^2)+(c2[1]^2))
    resultado = (round(real, 3), round(img, 3))
    return resultado

def modulocplx(c):
    modu = math.sqrt(c[0]**2+c[1]**2)
    return round(modu,3)

def conjugadocplx(c):
    return (c[0], -c[1])

def deCartesianoApolar(c):
    p = modulocplx(c)
    theta = math.atan(c[1] / c[0])
    respuesta = (round(p, 3), round(theta, 3))
    return respuesta

def dePolaraCartesiano(c):
    respuesta = (round(c[0] * math.cos(c[1]), 3), round(c[0] * math.sin(c[1]), 3))
    return respuesta

def fasecplx(c):
    fase = math.atan(c[1] / c[0])
    return round(fase, 3)
