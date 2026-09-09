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

<<<<<<< HEAD
    print ("")
    print ("")

    eleccion = input("Eliga una opcion (del 1 al 9 y 10 para EXIT): ")
    return eleccion

print ("")
print ("")

=======
    eleccion = input("Eliga una opción (del 1 al 9 y 10 para EXIT): ")
    return eleccion

#Ejecución del programa principal:
>>>>>>> 1c32c2af143ee5bd489f157d3816d227a38291f6
if __name__ == "__main__":
    while True:
        opcion = menu_principal()

        print ("")
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
<<<<<<< HEAD
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
=======
            print("Actualización manual de concurrencia: ")
            print("Seleccione escenario (E1, E2, E3, E4): ")
            print("Seleccione dia (Viernes, Sabado, Domingo): ")
            print("Ingrese nueva cantidad de asistentes: ")
        elif opcion == "3":
            print("Busqueda puntual de escenario: ")
            print("Ingrese codigo unico (ej. E1) o nombre del escenario: ")
>>>>>>> 1c32c2af143ee5bd489f157d3816d227a38291f6
        elif opcion == "4":
            print("Consulta de concurrencia por dia: ")
            print("Seleccione el dia a consultar (Viernes, Sabado, Domingo): ")
        elif opcion == "5":
            print("Registro de entradas vendidas: ")
            print("Seleccione categoria de acceso (Campo General, VIP Lounge, LollaFam, Prensa): ")
            print("Seleccione dia (Viernes, Sabado, Domingo): ")
            print("Ingrese cantidad de entradas vendidas a registrar: ")
        elif opcion == "6":
            print("Consultar entradas vendidas y disponibles por categoría")
        elif opcion == "7":
            print("Consultar estadísticas e indicadores")
        elif opcion == "8":
            print("Consultar ranking y Top 3 de escenarios")
        elif opcion == "9":
            print("Generar informes finales")
        elif opcion == "10":
            print("Gracias por utilizar el sistema de gestion de Lollapalooza.")
            break
        else:
            print("Opcion invalida, debe ingresar un número del 1 al 10.")

        

    



