def matrizInicializador (matriz, filas, columnas, valor):
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(valor)