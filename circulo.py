#importar cualquier libreria que se vaya a utilizar
import math

#entrada de datos
diametro = float(input("diametro: "))
radio = float(input("radio: "))

#proceso
perimetro = (math.pi*diametro)
area = (math.pi*(radio**2))

#salida
print("El perimetro es = ", round(perimetro,2), "El area es = ", round(area,2))