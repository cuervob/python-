#biblioteca
import math

#entrada
a=float(input("Valor de a:"))
b=float(input("valor de b:"))
c=float(input("Valor de c:"))

#proceso
x1=((-b)+math.sqrt(b**2-(4*a*c)))/(2*a)
x2=((-b)-math.sqrt(b**2-(4*a*c)))/(2*a)

#salida
print("X1= ",round(x1,3), "X2= ",round(x2,3))
