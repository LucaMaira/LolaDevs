producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad

#1 F string y formato de decimales

print(f"El total a pagar por {cantidad} unidades de {producto} es: ${total:.2f} ")

#2 Concatenacion y str

print("El total a pagar por " + str(cantidad) + " unidades de " + producto + " es de: $" + str(total))