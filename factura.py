# Autor: Camila Vallejos

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad

print("\n--- Resumen de la compra ---")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:.2f}")
