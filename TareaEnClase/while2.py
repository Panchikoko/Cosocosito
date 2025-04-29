#1 - Mostrar 10 repeticiones de números ascendentes desde el 1 al 10. (for)

#for i in range(1, 11):
#    print(i)

#=================================================================================================
# 2 - Mostrar 10 repeticiones de números descendentes desde el 10 al 1. (for)

#for i in range(10, 0, -1):
#    print(i)

#=================================================================================================
# 3 - Mostrar la suma de los números desde el 1 hasta el 10. (for, acumulador)

#acumulador = 0
#for i in range(1, 11):
#    acumulador += i
#print("acumulador:", acumulador)

#=================================================================================================
# 4 - Mostrar la suma de los números pares desde el 1 hasta el 10. (for, acumulador, 2)
suma_pares = 0
for i in range(2, 11, 2):
    suma_pares += i
print("Suma de pares:", suma_pares)
#=================================================================================================
# 5 - Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.

#suma_numeros = 0
#for i in range(5):
#    numero = int(input(f"Ingrese el número {i + 1}: "))
#    suma_numeros += numero
#promedio = suma_numeros / 5
#print("Suma:", suma_numeros)
#print("Promedio:", promedio)

#========================================================================================================
# 6 - Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).

#suma = 0
#contador = 0
#while True:
#    numero = input("Ingrese un número (o 'n' para salir): ")
#    if numero.lower() == 'n':
#        break
#    suma += int(numero)
#    contador += 1
#if contador > 0:
#    promedio = suma / contador
#    print("Suma:", suma)
#    print("Promedio:", promedio)
#else:
#    print("No se ingresaron números.")

#==================================================================================================
# 7 - Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).

#suma_positivos = 0
#producto_negativos = 1
#hay_negativos = False
#while True:
#    numero = input("Ingrese un número (o 'n' para salir): ")
#    if numero.lower() == 'n':
#        break
#    numero = int(numero)
#    if numero > 0:
#        suma_positivos += numero
#    elif numero < 0:
#        producto_negativos *= numero
#        hay_negativos = True
#print("Suma de positivos:", suma_positivos)
#print("Producto de negativos:", producto_negativos if hay_negativos else "No hay números negativos.")

#========================================================================================================
## 8 - Ingresar 10 números enteros. Determinar el máximo y el mínimo. (for, max, min)

#numeros = []
#for i in range(10):
#    numero = int(input(f"Ingrese el número {i + 1}: "))
#    numeros.append(numero)
#print("Máximo:", max(numeros))
#print("Mínimo:", min(numeros))