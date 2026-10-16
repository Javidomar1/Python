import math

def convertir_temperatura(temperatura: float, unidad_origen: str, unidad_destino: str) -> float:

    origen = unidad_origen.upper()
    destino = unidad_destino.upper()
    
    # Si las unidades son iguales, se devuelve la temperatura original redondeada
    if origen == destino:
        return round(float(temperatura), 2)

    # Conversión de Celsius a Fahrenheit
    if origen == "C" and destino == "F":
        resultado = (temperatura * 9/5) + 32
    # Conversión de Fahrenheit a Celsius
    elif origen == "F" and destino == "C":
        resultado = (temperatura - 32) * 5/9
    else:
        "Unidades no válidas. Utilice 'C' para Celsius o 'F' para Fahrenheit."
    return round(resultado, 2)

print(convertir_temperatura(20, "C", "F"))

def area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado.
    lado (float): La longitud de un lado del cuadrado.
    Retorna:
        float: El área del cuadrado.
    """
    lado = lado
    return lado*lado
def perimetro_cuadrado(lado: float) -> float:
    """
    Calcula el perímetro de un cuadrado.
        lado (float): La longitud de un lado del cuadrado.
    Retorna:
        float: El perímetro del cuadrado.
    """
    lado = lado
    return 4 * lado
def area_rectangulo(altura:float ,base:float)->float:
    area = altura*base
    return area
def perimetro_rectangulo(altura:float ,base:float)->float:
    perimetro = (altura*2)+(2*base)
    return perimetro
def area_circulo(radio: float)->float:
    area = math.pi*radio^2
    return area
def perimetro_circulo(radio: float)->float:
    perimetro = math.pi*radio^2
    return area
 
def analizar(*args: float) -> tuple:
    """
    Recibe un número variable de valores numéricos y devuelve sus estadísticas.
    """
    cantidad = len(args)
    minimo = min(args)
    maximo = max(args)
    suma = sum(args)
    media = suma / cantidad
    valor_absoluto = abs(suma)
    return cantidad, minimo, maximo, suma, media, valor_absoluto
resultado = analizar(10, 5, 20, 30)
print(f"Cantidad: {resultado[0]}, Mínimo: {resultado[1]}, Máximo: {resultado[2]}, Suma: {resultado[3]}, Media: {resultado[4]}, Absoluto: {resultado[5]}")
import random
import string
def aleatorio():
    def letra():
        return random.choice(string.ascii_letters)
    def numero():
        return random.randint(0,9)
    def especial():
        return random.choice(string.punctuation)
    n = random.randint(1,3)
    if n == 1 :
        return letra()
    elif n == 2 :
        return numero()
    else:
        return especial()
def generar_contraseñas(longitud: int, letras=False, numoros=False, espeaciales=False):
    if longitud < 3 and letras and numoros and espeaciales:
        print("No puedes pedir dicha contraseña")
        return[]
    contrasena=[]
    while True:
        tiene_letra = False
        tiene_numero = False
        tiene_especiales = False
        repetir = False
        contrasena.clear()
        for i in range(0,longitud):
                v:str = str(aleatorio())
                contrasena.append(aleatorio())
                if v.isalpha():
                    tiene_letra = True
                elif v.isdigit():
                    tiene_numero = True
                else:
                    tiene_especiales= True
        print(contrasena)
        if (letras and tiene_letra == False):
            repetir = True
        elif(numoros and tiene_numero == False):
            repetir = True
        elif(espeaciales and tiene_especiales == False):
            repetir = True
        if repetir == False:
                return str(contrasena)
print (generar_contraseñas(12))
print (generar_contraseñas(3,letras=False, numoros=True,espeaciales=True))



