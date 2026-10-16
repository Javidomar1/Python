Nombre = input("Escribe tu nombre")
Apellido1 = input("Escribe tu 1ºApellido")
Apellido2 = input("Escribe tu 2ºApellido")
Nacimiento = input("El año de nacimiento")
Usuario = input("Escribe el nº de usuario")
codigo_usuario = f"{Nacimiento:1}{Usuario:1.5}"
inicialNombre = Nombre[0]
print ("Expediente " + Nombre + "_" + Apellido1 + "_" + 
       inicialNombre)
print ("Codigo de usuario:" + Nacimiento +"_"+ codigo_usuario)