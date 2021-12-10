#Dado o seguinte PVI:
#y'(x)=5,8sen(y(x)x)
#y(2,1)=5
#encontre o tamanho do primeiro passo se aplicarmos um método de Euler Adaptativo. 
#Tome o passo (h) inicial igual a 0,47 e use uma tolerância (tol) de 0,0003. 

from math import sin

def adaptative_euler(x0, y0, h, tol, f):
    y_full = y0 + h * f(x0,y0)
    y_half = y0 + h/2.0 * f(x0,y0)
    error = 2*abs(y_full - y_half)
    while (error > tol):
        y_full = y0 + h * f(x0,y0)
        y_half = y0 + h/2 * f(x0,y0)
        error = 2*abs(y_full - y_half)
        if error > tol:
            h /= 2.0
        else:
            x0 += h
            y0 = y_half
        
    return h

def f(x, y):
    return 5.8*sin(x*y)

tol = 0.0003
x0 = 2.1
y0 = 5
h = 0.47

print('{0:.20f}'.format(adaptative_euler(x0, y0, h, tol, f)))
