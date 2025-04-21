import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

# ------------------------------ Funciones ------------------------------ #

def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    return {}

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def registrar():
    def guardar_nuevo_usuario():
        nuevo_usuario = entry_nuevo_usuario.get()
        nueva_contrasena = entry_nueva_contrasena.get()
        if nuevo_usuario and nueva_contrasena:
            if nuevo_usuario in usuarios:
                messagebox.showerror("Error", "El usuario ya existe")
            else:
                usuarios[nuevo_usuario] = nueva_contrasena
                guardar_usuarios(usuarios)
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                registro_ventana.destroy()
        else:
            messagebox.showerror("Error", "Por favor completa todos los campos")

    registro_ventana = tk.Toplevel(ventana)
    registro_ventana.title("Registrarse")
    registro_ventana.geometry("300x200")

    tk.Label(registro_ventana, text="Nuevo Usuario:").pack(pady=5)
    entry_nuevo_usuario = tk.Entry(registro_ventana)
    entry_nuevo_usuario.pack()

    tk.Label(registro_ventana, text="Contraseña:").pack(pady=5)
    entry_nueva_contrasena = tk.Entry(registro_ventana, show="*")
    entry_nueva_contrasena.pack()

    tk.Button(registro_ventana, text="Registrar", command=guardar_nuevo_usuario).pack(pady=10)

def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if usuarios.get(usuario) == contrasena:
        messagebox.showinfo("Éxito", f"¡Bienvenido, {usuario}!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ------------------------------ Interfaz ------------------------------ #

ventana = tk.Tk()
ventana.title("Administrador de Tareas - Login")
ventana.geometry("400x500")
ventana.configure(bg="#f2f2f2")

# Cargar y mostrar imagen
imagen = Image.open("C:\\Users\\Usuario\\Documents\\IV Semestre\\Estructuras de informacion\\Administrador de Tareas\\Administrador_de_tareas\\logoadmi.jpg")
imagen = imagen.resize((150, 150))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk, bg="#f2f2f2")
label_imagen.pack(pady=10)

tk.Label(ventana, text="Iniciar Sesión", font=("Arial", 18, "bold"), bg="#f2f2f2").pack(pady=10)

tk.Label(ventana, text="Usuario:", bg="#f2f2f2").pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:", bg="#f2f2f2").pack()
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack(pady=5)

tk.Button(ventana, text="Ingresar", command=iniciar_sesion, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(ventana, text="Registrarse", command=registrar, bg="#2196F3", fg="white", width=15).pack()

# Cargar usuarios desde archivo
usuarios = cargar_usuarios()

ventana.mainloop()
