def menu_principal():

    print ("BIENVENIDO AL PROGRAMA DE LOLLAPALOOZA")

    #menu:
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

    eleccion = input("Eliga una opcion (del 1 al 9 y 10 para EXIT): ")
    return eleccion


if __name__ == "__main__":
    opcion = menu_principal()
    print("Elegiste:", opcion)


    



