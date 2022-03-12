#entrada
metros=float(input("metros de agua: "))

#proceso
if (metros < 0):
    print("FUGA DE AGUA")
elif (metros == 0):
    print("ENCENDER BOMBA")
elif (metros >0 and metros <2):
    print("ACELERAR BOMBA DE AGUA")
elif (metros >=2 and metros <4):
    print("BOMBA TRABAJANDO")
elif (metros >=4 and metros <6):
    print("DESACELERAR BOMBA")
elif (metros == 6):
    print("APAGAR BOMBA")
elif (metros>6):
    print("DESBORDAMINETO DE AGUA EN CISTERNA")
else: 
    print("ERROR")
