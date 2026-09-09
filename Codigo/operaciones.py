def matrizInicializador (matriz, filas, columnas, valor):
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(valor)

def matrizPrincipal():

    Lola = []
    matrizInicializador(Lola, 4, 4, 0)
    return Lola

def matrizInformes(matriz):
    print("Índice\tCódigo\tNombre\tCapacidad simulada")
    for f in range(len(matriz)):
        print(f"{matriz[f][0]}\t{matriz[f][1]}\t{matriz[f][2]}\t{matriz[f][3]}")

Lola = matrizPrincipal()
matrizInformes(Lola)