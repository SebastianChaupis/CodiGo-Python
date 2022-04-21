from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

class Alumno:
    
    def registrarAlumno(self):
        self.TrvAlumnos.insert("",0,text=self.nombre.get() +" "+ self.apellido.get(),values=self.email.get())
    
    def __init__(self,window):
        self.wind = window
        self.wind.title("Crud de Alumnos")
        self.wind.geometry("600x300")
        
         #Frame
        frame= LabelFrame(self.wind,text="Registro de nuevo alumno")
        frame.grid(row=0,column=0,columnspan=3,pady=10)

        #label nombre
        lbNombre = Label(frame,text="Nombre: ")
        lbNombre.grid(row=1,column=0)
        #Text nombre
        self.nombre = Entry(frame)
        self.nombre.grid(row=1,column=1)
        
        #label email
        lbEmail = Label(frame,text="Email: ")
        lbEmail.grid(row=2,column=0)
        #Text email
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)
        
        #label apellido
        lbApellido = Label(frame,text="Apellido: ")
        lbApellido.grid(row=3,column=0)
        #Text apellido
        self.apellido = Entry(frame)
        self.apellido.grid(row=3,column=1)
        
        #Boton Registrar        
        btnNuevoAlumno = Button(frame,text="Registrar",command=self.registrarAlumno)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky= W+ E)
        
        #TRERVIEW
        self.TrvAlumnos = Treeview(height=10,columns=2)
        self.TrvAlumnos.grid(row=5,column=0,columnspan=2,padx=10)
        self.TrvAlumnos.heading("#0",text="Nombre",anchor=CENTER)
        self.TrvAlumnos.heading("#1",text="Email",anchor=CENTER)
     
window = Tk()
app = Alumno(window)
window.mainloop()