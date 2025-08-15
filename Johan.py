# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox


#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Johan Stiven Fiallo Aparicio")

# tamaño de la ventana
ventana_principal.geometry("650x650")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="green")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=630, height=180)
frame_entrada.place(x=10, y=10)



# titulo de la app
titulo = Label(frame_entrada, text="Johan Stiven Fiallo Aparicio")
titulo.config(bg = "white",fg="black", font=("Helvetica", 20))
titulo.place(x=280,y=10)

# titulo de la app
titulo = Label(frame_entrada, text="Hola,Como estas?,Te invito a saber un poco de mi.")
titulo.config(bg = "white",fg="black", font=("Verdana", 10))
titulo.place(x=280,y=40)

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()