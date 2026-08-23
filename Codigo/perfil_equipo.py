"""
Actividad 8
"""
#Funciones:
def contiene_digitos(texto):
    val = False
    for caracter in texto:
        if caracter.isdigit():
            val = True
    return val

def siglas(texto):
    sigla = "" #Variable vacía para almacenar las siglas

    for letra in texto.split(): #Iteración sobre cada palabra del texto, split convierte texto en una lista de palabras
        sigla+= letra[0].upper()
    return sigla

#Programa principal
def main():
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    comision = int(input("Ingrese la comisión: "))  
    nombre_integrante1 = str(input("Ingrese el nombre del integrante: "))
    rol_inicial1 = str(input("Ingrese el rol inicial en el proyecto: "))
    nombre_integrante2 = str(input("Ingrese el nombre del integrante: "))
    rol_inicial2 = str(input("Ingrese el rol inicial en el proyecto: "))
    nombre_integrante3 = str(input("Ingrese el nombre del integrante: "))
    rol_inicial3 = str(input("Ingrese el rol inicial en el proyecto: "))

    print("-"*50)
    print(f"Nombre del equipo: {nombre_equipo.upper()}, posee una cantidad de caracteres de: {len(nombre_equipo)}")
    print(f"Las siglas del equipo son: {siglas(nombre_equipo)}")
    print(f"Comisión: {comision}")
    print(f"Integrante 1: {nombre_integrante1.title()}, Rol: {rol_inicial1}")
    print(f"Integrante 2: {nombre_integrante2.title()}, Rol: {rol_inicial2}")
    print(f"Integrante 3: {nombre_integrante3.title()}, Rol: {rol_inicial3}")
    if contiene_digitos(nombre_equipo) == True:
        print("El nombre del equipo contiene dígitos")
    else:
        print("El nombre del equipo no contiene dígitos")
    print("-"*50)

main()