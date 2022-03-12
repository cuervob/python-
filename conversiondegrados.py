#entrada
c=float(input("Grados Celsius: "))
f=float(input("Grados Farenheit: "))
k=float(input("Grados Kelvin: "))

#proceso
cf=((c*1.8)+32)
ck=(c+273.15)
fc=((f-32)/1.8)
fk=((5*(f-32)/9)+273.15)
kc=(k-273.15)
kf=((1.8*(k-273.15))+32)

#salida
print("Celsius a Farenheit= ", round(cf,3), "Celsius a Kelvin= ", round(ck,3))
print("Farenheit a Celsius= ", round(fc,3), "Farenheit a Kelvin=", round(fk,3))
print( "Klevin a Celsius= ", round(kc,3), "Kelvin a Farenheit= ", round(kf,3))
