#ENTRADA DE DATOS difinir/crear/declarar/ variable
nombre = input("Alumno = ")
c1 = float(input("Calificación1: "))
c2 = float(input("Calificación2: "))
c3 = float(input("Calificación3: "))

#PROCESO 
promedio = (c1+c2+c3)/3

#salida de datos
print("El promedio de", nombre, " = ", round(promedio,2))
