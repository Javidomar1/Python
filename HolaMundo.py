print("Hola mundo")
a = 1
b = 2
contador = 0
for i in range(5):
    if (b>a):
        print("Soy gillipollas")
while contador < 3:
    print("Primer while")
    contador += 1

num = 3.33333333333333333
print (float(num))

cad = "hola mundo"
print (cad.upper())
print (cad.split())
print (cad.upper().split())
nombre = "Javier"
print (f"tu nombre es {nombre} \n soy nuevo")
for i in range(5):
    print(nombre,num)

producto = "Salmon"
precio = 30
cantidad = 3
mensaje = f"Producto: {producto} | Precio: {precio:.2f} | Total: {precio * cantidad:.2f}€"
print (mensaje)
mensaje = f"Producto: {producto} | Precio: {precio} | Total: {precio * cantidad:.2f}€"
print (mensaje)
print (f"{'hola': =^20}")