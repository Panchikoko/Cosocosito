altura = float(input("Inserte su altura: "))

if altura > 2.00:
    print("Eres Pivote")
elif altura >= 1.80 and altura <= 2.00:
    print("Eres Alero")
elif altura >= 1.60 and altura <= 1.80:
    print("Eres Escolta")
else:
    print("Eres Base")
    
