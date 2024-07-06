# Definición de la estructura básica de datos (lista de diccionarios)
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 20.0},
    {"id": 2, "nombre": "Pantalón", "precio": 35.0},
    {"id": 3, "nombre": "Zapatos", "precio": 50.0}
]

# Función para mostrar todos los productos
def mostrar_productos():
    print("Lista de productos:")
    for producto in productos:
        print(f"{producto['id']}: {producto['nombre']} - ${producto['precio']}")

# Función para agregar un nuevo producto
def agregar_producto(nombre, precio):
    nuevo_id = len(productos) + 3
    nuevo_producto = {"id": nuevo_id, "nombre": nombre, "precio": precio}
    productos.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado con éxito.")

# Función principal que ejecuta el programa
def main():
    while True:
        print("\n1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            agregar_producto(nombre, precio)
        elif opcion == '3':
            print("Saliendo del programa.")
            print("Sus productos han sido agregados exitosamente")
            print("Gracias por su compra ¡Vuelva pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
