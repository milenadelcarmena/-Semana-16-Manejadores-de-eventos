import tkinter as tk
from tkinter import messagebox

# Ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Lista para almacenar las tareas
tareas = []


# Función para agregar una nueva tarea
def agregar_tarea(event=None):
    # Obtener texto del campo de entrada
    tarea = entrada_tarea.get().strip()

    # Verificar si el campo no está vacío
    if tarea:
        # Agregar tarea a la lista
        tareas.append({"texto": tarea, "completada": False})
        actualizar_lista()
        # Limpiar el campo de entrada
        entrada_tarea.delete(0, tk.END)
    else:
        # Mostrar mensaje de error si el campo está vacío
        messagebox.showerror("Error", "La tarea no puede estar vacía.")


# Función para marcar una tarea como completada
def marcar_completada(event=None):
    # Obtener índice de la tarea seleccionada
    seleccion = lista_tareas.curselection()

    if seleccion:
        indice = seleccion[0]
        # Cambiar estado de completada
        tareas[indice]["completada"] = not tareas[indice]["completada"]
        actualizar_lista()
    else:
        # Mostrar mensaje de error si no se seleccionó una tarea
        messagebox.showerror("Error", "Seleccione una tarea para marcarla como completada.")


# Función para eliminar una tarea
def eliminar_tarea(event=None):
    # Obtener índice de la tarea seleccionada
    seleccion = lista_tareas.curselection()

    if seleccion:
        indice = seleccion[0]
        # Eliminar tarea de la lista
        del tareas[indice]
        actualizar_lista()
    else:
        # Mostrar mensaje de error si no se seleccionó una tarea
        messagebox.showerror("Error", "Seleccione una tarea para eliminarla.")


# Función para actualizar la lista de tareas en la interfaz
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        estado = "(Completada)" if tarea["completada"] else "(Pendiente)"
        lista_tareas.insert(tk.END, f"{tarea['texto']} {estado}")


# Función para cerrar la aplicación
def cerrar_aplicacion(event=None):
    root.destroy()


# Widgets de la interfaz gráfica
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)

boton_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=10)

boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Atajos de teclado
root.bind("<Return>", agregar_tarea)  # Enter para añadir tarea
root.bind("<c>", marcar_completada)  # C para marcar como completada
root.bind("<Delete>", eliminar_tarea)  # Delete para eliminar tarea
root.bind("<Escape>", cerrar_aplicacion)  # Escape para cerrar la aplicación

# Iniciar el bucle principal de la aplicación
root.mainloop()

