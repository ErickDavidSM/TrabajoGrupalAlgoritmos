productos = [
    ["Zanahoria", 5, 20],
    ["Tomate", 10, 20],
    ["Papa", 8, 15],
    ["Cebolla", 6, 15],
    ["Lechuga", 4, 10]
]

print("PRODUCTOS DEL INVENTARIO")
print("")

for producto in productos:
    print("Producto:", producto[0])
    print("Precio: Q", producto[1])
    print("Cantidad disponible:", producto[2])
    print("")