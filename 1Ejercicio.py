texto: str = "P_y_t_h_o_n_ _e_s_ _e_x_c_e_l_e_n_t_e" 
frase_limpia = texto.replace("_","")
resultado2 = texto[::2]
resultado4 = texto[::-1]
vecesE = texto.count("e")
print(vecesE)
print(frase_limpia)        



notas : list[float] = [7.5, 4.0, 8.5, 6.0, 9.0, 4.0, 7.5, 10.0]
maxima = max(notas)
min =  min(notas)
media = sum(notas)/len(notas)
suspensos = [x for x in notas if x < 5]
aprender = [x for x in notas if x >= 5]
print(f"{maxima} {min}")
print(media)
print(f"{suspensos}")


usuario: dict[str, object]={
    "nombre " : "Ana",
    "edad" : 30,
    "ciudad":"Salamanca",
    "profesion": "Ingenieria"
}
print("1. Vista de todas las claves:")
claves = usuario.keys()
print(claves)

print("Vistaq de todos los valores")
valores = usuario.values()
print(valores)

print("todos los pares clave-valor")
pares = [(clave,valor)for clave,valor in usuario.items()]
print(pares)

edades = usuario.get("edad",object)
print(edades)

telefono = usuario.get("telefono", "No esta disponible")
print(telefono)


lenguajes: list[str] = ["Python","Java","C++"]

itearadores = iter(lenguajes)
print(next(itearadores))
print(next(itearadores))
print(next(itearadores))

grupo_a: set[str] = {"Ana", "Luis", "Marta", "Pedro", "Laura"} 
grupo_b: set[str] = {"Pedro", "Laura", "Carlos", "Javier"} 

ambosGrupos = []



