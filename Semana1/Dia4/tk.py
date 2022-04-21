from tkinter import *
from tkinter import messagebox

def saludar():
    print("Hola mundo tk")
    messagebox.showinfo("Title","Hola "+ txtNombre.get())
    
app = Tk()
app.title("Mi primera interfaz grafica")
app.geometry("300x100")
frame = LabelFrame(app,text="Ventana")
frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)
#Etiqueta
lbNombre = Label(frame,text="nombre")
lbNombre.grid(row=1,column=1)
#Caja de texto
txtNombre= Entry(frame)
txtNombre.grid(row=1,column=1)
#Boton
btnSaludo = Button(frame,text="saludar",command=saludar)
btnSaludo.grid(row=1,column=2)
app.mainloop()

##
       