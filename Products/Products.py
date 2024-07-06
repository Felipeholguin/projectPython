class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.id}: {self.nombre} - ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = []

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def agregar_producto(self, nombre, precio):
        nuevo_id = len(self.productos) + 1
        nuevo_producto = Producto(nuevo_id, nombre, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado con éxito.")

    def ejecutar(self):
        while True:
            print("\n1. Mostrar productos")
            print("2. Agregar producto")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.mostrar_productos()
            elif opcion == '2':
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                self.agregar_producto(nombre, precio)
            elif opcion == '3':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    inventario = Inventario()
    inventario.ejecutar()
