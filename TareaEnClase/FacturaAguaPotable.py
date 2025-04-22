cargo_fijo = 7000
costo_m3_agua = 200
bonificacion = 0
recargo = 0

print ("Elija su tipo de cliente")
tipo_de_cliente = int (input ("1- Residencial " "2- Comercial " "3- Industrial "))

if tipo_de_cliente >= 4 or tipo_de_cliente <=0:
    print ("No es un tipo de cliente valido")
    exit()

consumo_m3 = int (input ("Escriba cuanto es su consumo de m3 de agua: "))

subtotal = consumo_m3 * costo_m3_agua


if tipo_de_cliente == 1:
    if consumo_m3 < 30:
        bonificacion = 0.10 * subtotal
    elif consumo_m3 > 80:
        recargo = 0.15 * subtotal
    
    if (subtotal + cargo_fijo) < 35000:
        bonificacion += 0.05 * (subtotal + cargo_fijo)

elif tipo_de_cliente == 2:
    if consumo_m3 > 150:
        bonificacion = 0.08 * subtotal
    elif consumo_m3 > 300:
        bonificacion = 0.12 * subtotal
    elif consumo_m3 < 50:
        recargo = 0.05 * subtotal

elif tipo_de_cliente == 3:
    if consumo_m3 > 500:
        bonificacion = 0.20 * subtotal
    elif consumo_m3 > 1000:
        bonificacion = 0.30 * subtotal
    elif consumo_m3 < 200:
        recargo = 0.10 * subtotal

totalsiniva = subtotal + cargo_fijo - bonificacion + recargo
iva = 0.21 * totalsiniva
total = totalsiniva + iva

if tipo_de_cliente == 1:
    tipo_de_cliente = "Residencial"
elif tipo_de_cliente == 2:
    tipo_de_cliente = "Comercial"
elif tipo_de_cliente == 3:
    tipo_de_cliente = "Industrial"

print ("------------------------------------------------")
print ("Factura del servicio")
print ("------------------------------------------------")
print ("Tipo de cliente: ", tipo_de_cliente)
print ("Consumo de agua: ", consumo_m3, "m3")
print ("Subtotal por consumo: ", subtotal)
print ("Cargo fijo: ", cargo_fijo)
print ("Bonificacion: ", bonificacion)
print ("Recargo: ", recargo)
print ("Subtotal: ", totalsiniva)
print ("IVA: ", iva)
print ("Total a pagar: ", total)