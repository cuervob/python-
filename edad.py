#libreria
import datetime

#entrada
nombre = input("Escribe tu nombre: ")
an = float(input("Año de nacimiento: "))
ac = float(input("Año actual: "))
año_actual_2 = datetime.date.today().year
mesactual = datetime.date.today().month

#proceso
edad = (ac-an)
edad2 = (año_actual_2-an)
mes= mesactual
añoactual= datetime.date.today().year

#salida
print("La edad de", nombre, " = ", edad)
print("la edad es= ", edad2)
print("mes=", mes, "año actual con libreria =", añoactual)
