import tkinter as tk
from tkinter import messagebox

class Producto:
    def __init__(self, nombre, precio, existencias, unidad):
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias
        self.unidad = unidad

def agregar_producto():
    nombre = nombre_var.get()
    precio = float(precio_var.get())
    existencias = float(existencias_var.get())
    unidad = unidad_var.get()
    
    for producto in inventario:
        if producto.nombre == nombre:
            messagebox.showwarning("Advertencia", "El producto ya existe en el inventario.")
            return
    
    # Si el producto no existe, lo agregamos al inventario
    producto = Producto(nombre, precio, existencias, unidad)
    inventario.append(producto)
    messagebox.showinfo("Información", "Producto agregado correctamente.")
    mostrar_existencias()


def mostrar_existencias():
    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, "Productos en existencias:\n")
    for producto in inventario:
        info_text.insert(tk.END, f"\nNombre: {producto.nombre}\n", 'nombre_tag')
        info_text.insert(tk.END, f"Precio: {producto.precio}\n", 'precio_tag')
        info_text.insert(tk.END, f"Existencias: {producto.existencias}\n", 'existencias_tag')
        info_text.insert(tk.END, f"Unidad: {producto.unidad}\n", 'unidad_tag')
    
    # Crear un listbox para mostrar los nombres de los productos
    listbox = tk.Listbox(existencias_frame, selectmode=tk.SINGLE, height=10)
    for producto in inventario:
        listbox.insert(tk.END, producto.nombre)
    listbox.pack()

    # Botón para seleccionar y modificar el producto
    tk.Button(existencias_frame, text="Modificar Producto", command=lambda: modificar_producto(listbox.get(tk.ACTIVE))).pack()
def modificar_producto(nombre_producto):
    for producto in inventario:
        if producto.nombre == nombre_producto:
            nombre_var.set(producto.nombre)
            precio_var.set(producto.precio)
            existencias_var.set(producto.existencias)
            unidad_var.set(producto.unidad)
            break



def procesar_orden():
    nombre_producto = producto_var.get()
    cantidad = float(cantidad_var.get())
    for producto in inventario:
        if producto.nombre == nombre_producto:
            if producto.existencias >= cantidad:
                total = cantidad * producto.precio
                info_text.insert(tk.END, f"Orden realizada: Producto: {producto.nombre}, Cantidad: {cantidad}, {producto.unidad}, Total: {total}\n")
                producto.existencias -= cantidad
                pago = float(pago_var.get())
                cambio = pago - total
                if cambio >= 0:
                    info_text.insert(tk.END, f"Cambio: {cambio}\n")
                else:
                    messagebox.showwarning("Advertencia", "El pago es insuficiente.")
                return
            else:
                messagebox.showwarning("Advertencia", f"No hay suficientes existencias de {nombre_producto}")
                return
    messagebox.showwarning("Advertencia", f"El producto {nombre_producto} no se encuentra en el inventario.")

def mostrar_agregar_producto():
    agregar_producto_frame.pack()
    menu_frame.pack_forget()

def mostrar_mostrar_existencias():
    existencias_frame.pack()
    menu_frame.pack_forget()
    mostrar_existencias()

def mostrar_procesar_orden():
    orden_frame.pack()
    menu_frame.pack_forget()

def regresar_menu_principal(frame):
    frame.pack_forget()
    menu_frame.pack()

root = tk.Tk()
root.title("Gestión de Inventarios")

nombre_var = tk.StringVar()
precio_var = tk.StringVar()
existencias_var = tk.StringVar()
unidad_var = tk.StringVar()
producto_var = tk.StringVar()
cantidad_var = tk.StringVar()
pago_var = tk.StringVar()

inventario = []

menu_frame = tk.Frame(root)

tk.Button(menu_frame, text="Agregar Producto", command=mostrar_agregar_producto).pack()
tk.Button(menu_frame, text="Mostrar Existencias", command=mostrar_mostrar_existencias).pack()
tk.Button(menu_frame, text="Procesar Orden", command=mostrar_procesar_orden).pack()

agregar_producto_frame = tk.Frame(root)
tk.Label(agregar_producto_frame, text="Nombre del Producto:").grid(row=0, column=0, sticky="w")
tk.Entry(agregar_producto_frame, textvariable=nombre_var).grid(row=0, column=1)

tk.Label(agregar_producto_frame, text="Precio:").grid(row=1, column=0, sticky="w")
tk.Entry(agregar_producto_frame, textvariable=precio_var).grid(row=1, column=1)

tk.Label(agregar_producto_frame, text="Existencias:").grid(row=2, column=0, sticky="w")
tk.Entry(agregar_producto_frame, textvariable=existencias_var).grid(row=2, column=1)

tk.Label(agregar_producto_frame, text="Unidad de Medida:").grid(row=3, column=0, sticky="w")
tk.OptionMenu(agregar_producto_frame, unidad_var, "unidades", "kilos").grid(row=3, column=1)

tk.Button(agregar_producto_frame, text="Agregar Producto", command=agregar_producto).grid(row=4, columnspan=2, pady=5)
tk.Button(agregar_producto_frame, text="Regresar al Menú Principal", command=lambda: regresar_menu_principal(agregar_producto_frame)).grid(row=5, columnspan=2, pady=5)

existencias_frame = tk.Frame(root)
tk.Button(existencias_frame, text="Mostrar Existencias", command=mostrar_existencias).pack()
info_text = tk.Text(existencias_frame, height=10, width=50)
info_text.pack()
tk.Button(existencias_frame, text="Regresar al Menú Principal", command=lambda: regresar_menu_principal(existencias_frame)).pack()

orden_frame = tk.Frame(root)
tk.Label(orden_frame, text="Producto:").grid(row=0, column=0, sticky="w")
tk.Entry(orden_frame, textvariable=producto_var).grid(row=0, column=1)

tk.Label(orden_frame, text="Cantidad:").grid(row=1, column=0, sticky="w")
tk.Entry(orden_frame, textvariable=cantidad_var).grid(row=1, column=1)

tk.Label(orden_frame, text="Pago:").grid(row=2, column=0, sticky="w")
tk.Entry(orden_frame, textvariable=pago_var).grid(row=2, column=1)

tk.Button(orden_frame, text="Procesar Orden", command=procesar_orden).grid(row=3, columnspan=2, pady=5)
tk.Button(orden_frame, text="Regresar al Menú Principal", command=lambda: regresar_menu_principal(orden_frame)).grid(row=4, columnspan=2, pady=5)

menu_frame.pack()
root.mainloop()
