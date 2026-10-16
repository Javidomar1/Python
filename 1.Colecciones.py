# Cadena original
texto: str = "P_y_t_h_o_n_ _e_s_ _e_x_c_e_l_e_n_t_e"

# 1. Extraer únicamente los caracteres descartando los guiones bajos (Slicing)
# Empieza en el índice 0 y salta de 2 en 2 para omitir los "_"
texto_slicing = texto[::2]
print(f"1. Usando slicing: {texto_slicing}")
texto_replace = texto.replace("_", "")
print(f"2. Usando replace: {texto_replace}")
frase_limpia = texto_slicing 
print(f"3. Frase limpia guardada: {frase_limpia}")
frase_invertida = frase_limpia[::-1]
print(f"4. Frase invertida: {frase_invertida}")
cantidad_e = frase_limpia.count("e")
print(f"5. La letra 'e' aparece: {cantidad_e} veces")


notas: list[float] = [7.5, 4.0, 8.5, 6.0, 9.0, 4.0, 7.5, 10.0] 
max = max(notas)
min = min(notas)
media = sum(notas)/len(notas)
aprobados = [x for x in notas if x >5]
print(aprobados)

usuario: dict[str, object] = { 
"nombre": "Ana", 
"edad": 30, 
"ciudad": "Salamanca" 
} 
claves = usuario.keys()
valores = usuario.values()
clava-valor = usuario.items()
clave-va