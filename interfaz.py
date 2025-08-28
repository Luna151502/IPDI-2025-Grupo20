import tkinter as tk
import os
import shutil
from tkinter import filedialog
from PIL import Image, ImageTk

ruta_img=  None

carpeta_salida= r"C:\Users\Liz\proyecto1\image"

app =tk.Tk()
app.geometry('800x600')
app.configure(bg='beige')
button_font=('Verdana', 10, 'bold')

#Ventana menu
#v =tk.Tk()
#v.geometry('300x300')
#v.configure(bg='ghostwhite')
#button_font=('Verdana', 10, 'bold')

def cargar():
    global ruta_img
    archivo = filedialog.askopenfilename(
        filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )
    
    if archivo:
        # Abrir y mostrar imagen en la ventana
        ruta_img = archivo
        label_info.config(text=f"Imagen seleccionada:")
        img = Image.open(archivo)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        
        label_img.config(image=img_tk)
        label_img.image = img_tk

def pasar():
    global ruta_img
    if ruta_img:
        img = Image.open(ruta_img)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        label_img2.config(image=img_tk)
        label_img2.image = img_tk  # mantener referencia
    else:
        label_info.config(text="Primero seleccione una imagen")
        
def guardar():
    global ruta_img
    if ruta_img:
        #os.makedirs(carpeta_salida,exist_ok=True)
        nombre_archivo = os.path.basename(ruta_img)
        destino = os.path.join(carpeta_salida, nombre_archivo)
        shutil.copy(ruta_img, destino) #copia 
        label_info.config(text=f"Imagen guardada en:\n{destino}")
    else:
        label_info.config(text='No se ha seleccionado ninguna imagen')

def salir():
    app.destroy()

boton=tk.Button(app, text='Cargar imagen', command=cargar, fg='black')
boton.pack()
boton.place(x=350, y=450)

boton2=tk.Button(app, text='Pasar imagen', command=pasar, fg='black')
boton2.pack()
boton2.place(x=350, y=500)

boton3=tk.Button(app, text='Salir', command=salir, fg='red')
boton3.pack()
boton3.place(x=375, y=550)

boton4=tk.Button(app, text='Guardar', command=guardar, fg='green', pady=10, width=20)
boton4.pack()
boton4.place(x=550, y=500)

# Info de imagen seleccionada
label_info = tk.Label(app, text="Ninguna imagen seleccionada")
label_info.pack(pady=5)

label_img = tk.Label(app)
label_img.pack()
label_img.place(x=100,y=50)

label_img2 = tk.Label(app)
label_img2.pack()
label_img2.place(x=450,y=50)


app.mainloop()