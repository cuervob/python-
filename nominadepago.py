#entrada 
salario = float(input("Salario por dia: "))
mes = 31

#proceso
pagobase = (salario*mes)
ivatrasladado = (pagobase*0.16) 
subtotal = (pagobase+ivatrasladado)
ivaretenido = round((2/3*ivatrasladado),2)
isr = (pagobase*0.10)
pagoneto = (subtotal-ivaretenido-isr)

#salida
print("pagobase=", pagobase, "iva trasladado=", ivatrasladado, "subtotal=", subtotal, "iva retenido=", ivaretenido, "isr=",isr)
print("El salario es = ", round(pagoneto,2)) 

