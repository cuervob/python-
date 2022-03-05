#IMPORTAR LA LIBRERIA math: funciones matematicas
#sintaxis
import math

#entrada de datos
#definir o crear o declarar variable
number1 = 10
number2 = 2

#proceso (calculos u operaciones matematicas y logicas)
suma = number1 + number2
resta = number1 - number2
multiplicación = number1 * number2
division = number1 / number2 
potencia1 = number1 ** number2
potencia2 = pow(number1,number2)
cuadrado = number1 ** 2
cubo= pow(number1, 3)
raiz_cuadrada1 = pow(number1, 1/2)
raiz_cuadrada2 = math. sqrt(number1)
raiz_cubica = pow(number2, 1/3)
modulo_residuo = number1 % number2



#salida de datos
print("La suma =", suma,)
print("la suma =", suma, "\nla resta=", resta)
print("La suma =" + str(suma)) #concatenar (unir textos)
#convertir el numero a texto para usar concatenar que es el simbolo de +
print(f"LA SUMA = {suma}")

print("LA SUMA =", suma, "LA RESTA =", resta,)
print("LA SUMA =", suma, "LA RESTA =", resta, "LA MULTIPLICACION =", multiplicación, "LA DIVISION =", division)
print("LA SUMA =", suma, "\nLA RESTA =", resta, "\nLA MULTIPLICACION =", multiplicación, "\nLA DIVISION =", division,)
print("La potencia=", potencia1, "la raiz cuadrada=", raiz_cuadrada1, "la raiz cubica=", raiz_cubica, "el residuo=", modulo_residuo)
