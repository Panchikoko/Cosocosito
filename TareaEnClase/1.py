edad = int (input ("¿Cuántos años tenés? "))

if edad <=0 or edad >120:
    print ("Edad no válida")

elif edad <13:
    print ("Acceso denegado. Debes tener al menos 13 años para entrar")

elif edad >=13 and edad <=17:
    print ("Acceso restringido. Estás en modo adolecente")

else:
    print ("Acceso completo concedido")