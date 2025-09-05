import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

imagen_original = None
imagen_procesada = None
ANCHO_PANEL = 400
ALTO_PANEL = 400

def cargar():
    global imagen_original
    ruta = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if ruta:
        imagen_original = Image.open(ruta)
        imagen_redimensionada = imagen_original.resize((ANCHO_PANEL, ALTO_PANEL))
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        label_img.config(image=imagen_tk)
        label_img.image = imagen_tk
        label_info.config(text="imagen seleccionada", fg="green", font=('Verdana', 9, 'underline'),anchor='center',justify='center')

        # Ocultar el mensaje después de 3000 milisegundos (3 segundos)
        label_info.after(1000, lambda: label_info.config(text=""))

def pasar():
    global imagen_original, imagen_procesada
    if imagen_original:
        imagen_procesada = imagen_original.resize((ANCHO_PANEL, ALTO_PANEL))
        img_tk = ImageTk.PhotoImage(imagen_procesada)
        label_img2.config(image=img_tk)
        label_img2.image = img_tk
    else:
        label_info.config(text="Primero seleccione una imagen", fg="red", font=('Verdana', 9, 'underline'))

def guardar():
    if imagen_procesada:
        ruta_guardado = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG", "*.png"),
                ("BMP", "*.bmp"),
                ("TIFF", "*.tiff")
            ],
            title="Guardar imagen procesada"
        )
        if ruta_guardado:
            try:
                imagen_procesada.save(ruta_guardado)
                print(f"Imagen guardada en: {ruta_guardado}")
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")

def salir():
    app.destroy()

# Ventana principal
app = tk.Tk()
app.title("Visualizador con Paneles")
app.configure(bg='beige')
app.geometry("1100x450")

# Configurar columnas para estructura fija
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=0)
app.grid_columnconfigure(2, weight=0)

# Etiqueta informativa superior
label_info = tk.Label(app, text="Seleccione una imagen para empezar", bg='beige', font=('Verdana', 9, 'underline'))
label_info.grid(row=0, column=0, columnspan=3, pady=5)

# Panel izquierdo (imagen original)
panel_izquierdo = tk.Frame(app, width=400, height=400, bg='white')
panel_izquierdo.grid(row=1, column=0, padx=10, pady=10)
panel_izquierdo.grid_propagate(False)
label_img = tk.Label(panel_izquierdo, bg='white')
label_img.pack(expand=True, fill='both')

# Panel central (botones)
panel_central = tk.Frame(app, width=200, height=400, bg='beige')
panel_central.grid(row=1, column=1, padx=10, pady=10)
panel_central.grid_propagate(False)

# Contenedor interno para centrar los botones
contenedor_botones = tk.Frame(panel_central, bg='beige')
contenedor_botones.place(relx=0.5, rely=0.5, anchor='center')  # Centrado absoluto

# Botones
boton_cargar = tk.Button(contenedor_botones, text="Cargar imagen", command=cargar,
                         font=('Verdana', 10), fg='black', width=20)
boton_cargar.pack(pady=10)

boton_pasar = tk.Button(contenedor_botones, text="Pasar imagen", command=pasar,
                        font=('Verdana', 10), fg='black', width=20)
boton_pasar.pack(pady=10)

boton_guardar = tk.Button(contenedor_botones, text="Guardar", command=guardar,
                          font=('Verdana', 10), fg='green', width=20)
boton_guardar.pack(pady=10)

boton_salir = tk.Button(contenedor_botones, text="Salir", command=salir,
                        font=('Verdana', 10), fg='red', width=20)
boton_salir.pack(pady=10)

# Panel derecho (imagen procesada)
panel_derecho = tk.Frame(app, width=400, height=400, bg='white')
panel_derecho.grid(row=1, column=2, padx=10, pady=10)
panel_derecho.grid_propagate(False)
label_img2 = tk.Label(panel_derecho, bg='white')
label_img2.pack(expand=True, fill='both')

# Separación inferior
espacio_inferior = tk.Frame(app, height=30, bg='beige')
espacio_inferior.grid(row=2, column=0, columnspan=3)

app.mainloop()

