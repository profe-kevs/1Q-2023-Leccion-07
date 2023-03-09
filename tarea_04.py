import math

def euler(x, y, a, b):
    primer_resultado = (x - a)**2
    segundo_resultado = (y - b)**2
    total = math.sqrt(primer_resultado + segundo_resultado)
    return total

def juego(x, y):

    puntos = 0
    r = euler(x, y, 0, 0)

    if r > 10:
        puntos = 0
    elif 5 < r <= 10:
        puntos = 1
    elif 1 < r <= 5:
        puntos = 5
    else:
        puntos = 10
    
    return puntos
    

resultado = juego(3, 3)

print("Usted ganó:", resultado)
