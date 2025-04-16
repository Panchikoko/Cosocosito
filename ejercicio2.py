primerparcial = int(input("Inserte su nota del 1er parcial: "))
segundoparcial = int(input("Inserte su nota del 2do parcial: "))

notafinal = (primerparcial + segundoparcial) / 2

if notafinal >= 6:
    print("¡Promocionaste! Tu nota es: ", notafinal)
elif notafinal >= 4 and notafinal < 6:
    print("Aprobaste tu nota es: ", notafinal ,"Vas a final")
elif notafinal >= 2 and notafinal < 4:
    print("Desaprobaste tu nota es: ", notafinal)