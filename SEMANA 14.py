# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función desde el programa principal
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 200
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Mostrar los resultados
print("Resultados de la primera llamada a la función:")
print("Monto del descuento:", descuento1)
print("Monto final a pagar después del descuento:", monto_final1)

print("\nResultados de la segunda llamada a la función:")
print("Monto del descuento:", descuento2)
print("Monto final a pagar después del descuento:", monto_final2)
