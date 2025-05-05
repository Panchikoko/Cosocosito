#def es_mayor(edad):
#    if edad >= 18:
#        return "Es mayor de edad"
#    elif edad <= 0:
#        return "Dale no te haga' el boludo"
#    else:
#        return "Es menor de edad"
#
#anios = int(input("Ingresa tu edad:"))
#
#mensaje = es_mayor(anios)
#print(mensaje)

#def sumar(a, b):
#    print("resultado:", a + b)
#
#numero_1 = int(input("Introducir el sumero: "))
#
#numero_2 = int(input("Lo quieres sumar por: "))
#
#sumar(numero_1, numero_2)

def dividir(a: int, b: int) -> float:
    return a / b

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

resultado = dividir(n1, n2)

print (resultado)