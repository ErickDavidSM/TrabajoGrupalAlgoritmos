productos = [
    ["Zanahoria", 5, 20],
    ["Tomate", 10, 20],
    ["Papa", 8, 15],
    ["Cebolla", 6, 15],
    ["Lechuga", 4, 10]
]

factura = []
continuar = True

while continuar:
    print("CAJERO")
    print("PRODUCTOS DISPONIBLES")

    for i in range(len(productos)):
        print(i + 1, "-", productos[i][0],
              "Precio: Q", productos[i][1],
              "Disponibles:", productos[i][2])

    print("0 - Terminar compra")

    opcion = input("Seleccione un producto: ")

    if opcion.isdigit():
        opcion = int(opcion)

        if opcion == 0:
            continuar = False

        elif opcion >= 1 and opcion <= len(productos):
            posicion = opcion - 1

            nombre = productos[posicion][0]
            precio = productos[posicion][1]
            disponible = productos[posicion][2]

            if disponible > 0:
                cantidad_texto = input("Ingrese la cantidad: ")

                if cantidad_texto.isdigit():
                    cantidad = int(cantidad_texto)

                    if cantidad > 0 and cantidad <= disponible:
                        factura.append([nombre, precio, cantidad])
                        productos[posicion][2] -= cantidad

                        print("Producto agregado correctamente.")
                    else:
                        print("Cantidad incorrecta o insuficiente.")
                else:
                    print("Ingrese una cantidad numerica.")
            else:
                print("Producto agotado.")

        else:
            print("Opcion incorrecta.")
    else:
        print("Debe ingresar un numero.")

print("FACTURA")

subtotal = 0

if len(factura) == 0:
    print("No se compraron productos.")
else:
    print("Producto | Cantidad | Precio | Total")

    for producto in factura:
        nombre = producto[0]
        precio = producto[1]
        cantidad = producto[2]

        total = precio * cantidad
        subtotal += total

        print(nombre, "|", cantidad, "| Q", precio, "| Q", total)

    print("")
    print("SUBTOTAL: Q", subtotal)

print("")
print("Gracias por su compra.")