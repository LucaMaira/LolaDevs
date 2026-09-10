from random import randint
import operaciones, datos

def menu_principal():
    print("-"*55)
    print("\tBIENVENIDO AL PROGRAMA DE LOLLAPALOOZA")
    print("-"*55)

    #Menú:
    print ("1. Escenarios y capacidades.")
    print ("2. Actualizar concurrencia de un escenario y día.")
    print ("3. Buscar un escenario por código o nombre.")
    print ("4. Consultar concurrencia por día.")
    print ("5. Registrar entradas vendidas.")
    print ("6. Consultar entradas vendidas y disponibles por categoría.")
    print ("7. Consultar estadisticas e indicadores.")
    print ("8. Consultar ranking y Top 3 de escenarios.")
    print ("9. Generar informes finales.")
    print ("10 SALIR.")
    print ("")

def main():
    menu_principal()
    bandera = True
    while bandera:
        opcion = input("Ingrese una opción del 1 al 9, 10 para EXIT: ")

        print ("")

        if opcion == "1":
            print("Escenarios del festival:")
            print("1. Main Stage 1 (Codigo: E1 - Capacidad: 50.000)")
            print("2. Main Stage 2 (Codigo: E2 - Capacidad: 45.000)")
            print("3. Perry's Stage (Codigo: E3 - Capacidad: 30.000)")
            print("4. Alternative (Codigo: E4 - Capacidad: 25.000)")
            print ("")
            print ("")
        elif opcion == "2":
            print("Actualizacion manual de concurrencia:")
            print("Seleccione escenario (E1, E2, E3, E4):")
            print("Seleccione dia (Viernes, Sabado, Domingo):")
            print("Ingrese nueva cantidad de asistentes:")
            print ("")
            print ("")
        elif opcion == "3":
            print("Busqueda puntual de escenario:")
            print("Ingrese codigo unico (ej. E1) o nombre del escenario:")
            print ("")
            print ("")
        elif opcion == "4":
            print("Consulta de concurrencia por dia: ")
            print("Seleccione el dia a consultar (Viernes, Sabado, Domingo): ")
        elif opcion == "5":
            print("Registro de entradas vendidas: ")
            print("Seleccione categoria de acceso (Campo General, VIP Lounge, LollaFam, Prensa): ")
            print("Seleccione dia (Viernes, Sabado, Domingo): ")
            print("Ingrese cantidad de entradas vendidas a registrar: ")
            print ("")
            print ("")
        elif opcion == "6":
            print("Consulta de entradas vendidas y disponibles.")
            print("Categorias: Campo General, VIP Lounge, LollaFam, Prensa")
            print("Detalle por jornada: Viernes, Sabado, Domingo")
            print("Visualizacion de: Entradas vendidas, cupo restante y total general habilitado.")
            print("")
            print("")
        elif opcion == "7":
            print("Estadisticas e Indicadores")
            print("1. Concurrencia acumulada por dia (Viernes, Sabado, Domingo)")
            print("2. Promedio diario de concurrencia por escenario (3 dias)")
            print("3. Porcentaje de ocupacion actual por escenario y dia")
            print("4. Conteo de escenarios que alcanzaron el objetivo minimo (>= 60%)")
            print("5. Total de entradas vendidas del festival")
            print("")
            print("")
        elif opcion == "8":
            print("Rankinkg y top 3 Escenarios")
            print("Criterio: Mayor a menor concurrencia acumulada durante los 3 dias")
            print("Top 3 escenarios mas convocantes:")
            print("Pico maximo de asistencia individual:")
            print("")
            print("")
        elif opcion == "9":
            print("Informes Finales")
            print("Informe 1: Concurrencia acumulada registrada por dia")
            print("Informe 2: Concurrencia acumulada por escenario")
            print("Informe 3: Ranking de escenarios")
            print("Informe 4: Alertas preventivas (ocupacion >= 90%)")
            print("Informe 5: Promedios de concurrencia")
            print("Informe 6: Entradas vendidas y disponibles por categoria")
            print("Informe 7: Cumplimiento de objetivo de convocatoria (>= 60%)")
            print("")
            print("")
        elif opcion == "10":
            print("Gracias por utilizar el sistema de gestion de Lollapalooza.")
            bandera = False
        else:
            print("Opcion invalida, debe ingresar un número del 1 al 10.")

main()
    



