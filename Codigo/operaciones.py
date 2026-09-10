from datos import Codigo, Capacidad, Escenarios

def matrizInicializador (matriz, filas, columnas, valor):
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(valor)

def cargaInicial(liCo,liNo,liCa):
    lista = []
    for i in range(len(liCo)):
        lista.append((liCo[i], liNo[i], liCa[i]))
    return lista

def listaInformes(lista):
    print("Índice\tCódigo\tNombre\t\tCapacidad simulada")
    for f in range(len(lista)):
        print(f"{f}\t{lista[f][0]}\t{lista[f][1]}\t{lista[f][2]}")