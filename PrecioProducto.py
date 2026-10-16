referencia_id = 7 
nombre_producto = "Monitor 4K" 
precio_base = 249.90 
iva_porcentaje = 21 

importe_iva = precio_base * (iva_porcentaje / 100) 
precio_total = precio_base + importe_iva
print("---Factura Simplificada----")
print(f"Ref.Producto : {referencia_id:06}")
print(f"Producto     : {nombre_producto}")
print(f"Base Imponibe: {precio_base:8.2f}€")
print(f"IVA ({iva_porcentaje}%)  : {importe_iva:8.2f} €")
print(f"Total a Pagar : {precio_total:8.2f}€")