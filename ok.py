from tkinter import *
from tkinter import messagebox

# -----------------------------
# ventana principal de la app
# -----------------------------
ventana_principal = Tk()
ventana_principal.title("App de Johan")
ventana_principal.geometry("650x650")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="green")

# --------------------------------
# frame entrada datos
# --------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=630, height=180)
frame_entrada.place(x=10, y=10)

titulo = Label(frame_entrada, text="Johan Stiven Fiallo Aparicio")
titulo.config(bg="white", fg="black", font=("Helvetica", 20))
titulo.place(x=230, y=30)

titulo2 = Label(frame_entrada, text="¡Holaa!, te invito a conocer un poco de mi.")
titulo2.config(bg="white", fg="black", font=("Verdana", 11))
titulo2.place(x=260, y=60)

# Cargar foto personal
try:
    logo = PhotoImage(file="img/fotopersonal.png")
    lb_logo = Label(frame_entrada, image=logo, bg="white")
    lb_logo.place(x=60, y=20)
except:
    Label(frame_entrada, text="(Imagen no encontrada)", bg="white", fg="red").place(x=60, y=20)

# --------------------------------
# frame botoncitos 1
# --------------------------------
frame_botones1 = Frame(ventana_principal)
frame_botones1.config(bg="grey", width=630, height=180)
frame_botones1.place(x=10, y=200)

# --------------------------------
# frame botoncitos 2
# --------------------------------
frame_botones2 = Frame(ventana_principal)
frame_botones2.config(bg="grey", width=630, height=245)
frame_botones2.place(x=10, y=390)

# --------------------------------
# función genérica para abrir ventanas
# --------------------------------
def abrir_ventana(num, titulo="Ventana", color="lightgray"):
    v = Toplevel()
    v.title(f"{titulo}")
    v.geometry("400x300")
    v.config(bg=color)
    Label(v, text=f"Aquí va la información de {titulo}", bg=color, font=("Arial", 14)).pack(pady=50)

# --------------------------------
# Cargar imágenes de los botones
# --------------------------------
try:
    img_btn1 = PhotoImage(file="img/btn1.png").subsample(2, 2)
    img_btn2 = PhotoImage(file="img/btn2.png").subsample(2, 2)
    img_btn3 = PhotoImage(file="img/btn3.png").subsample(2, 2)
    img_btn4 = PhotoImage(file="img/btn4.png").subsample(2, 2)
    img_btn5 = PhotoImage(file="img/btn5.png").subsample(2, 2)
    img_btn6 = PhotoImage(file="img/btn6.png").subsample(2, 2)
    img_btn7 = PhotoImage(file="img/btn7.png").subsample(2, 2)
    img_btn8 = PhotoImage(file="img/btn8.png").subsample(2, 2)
    img_btn9 = PhotoImage(file="img/btn9.png").subsample(2, 2)
    img_btn10 = PhotoImage(file="img/btn10.png").subsample(2, 2)
except:
    messagebox.showerror("Error", "No se pudieron cargar todas las imágenes.\nRevisa la carpeta img/")

# --------------------------------
# Botones en frame 1 con imágenes
# --------------------------------
btn1 = Button(frame_botones1, text="Lugar y fecha n.", image=img_btn1, compound="top", command=lambda: abrir_ventana(1, "Lugar y fecha n."))
btn1.place(x=20, y=30, width=100, height=120)

btn2 = Button(frame_botones1, text="Inf. médica", image=img_btn2, compound="top", command=lambda: abrir_ventana(2, "Inf. médica"))
btn2.place(x=140, y=30, width=100, height=120)

btn3 = Button(frame_botones1, text="Inf. familiar", image=img_btn3, compound="top", command=lambda: abrir_ventana(3, "Inf. familiar"))
btn3.place(x=260, y=30, width=100, height=120)

btn4 = Button(frame_botones1, text="Proceso edu", image=img_btn4, compound="top", command=lambda: abrir_ventana(4, "Proceso educativo"))
btn4.place(x=380, y=30, width=100, height=120)

btn5 = Button(frame_botones1, text="Amigos", image=img_btn5, compound="top", command=lambda: abrir_ventana(5, "Amigos"))
btn5.place(x=500, y=30, width=100, height=120)

# --------------------------------
# Botones en frame 2 con imágenes
# --------------------------------
btn6 = Button(frame_botones2, text="Hobbies", image=img_btn6, compound="top", command=lambda: abrir_ventana(6, "Hobbies"))
btn6.place(x=20, y=70, width=100, height=120)

btn7 = Button(frame_botones2, text="Horario esc.", image=img_btn7, compound="top", command=lambda: abrir_ventana(7, "Horario escolar"))
btn7.place(x=140, y=70, width=100, height=120)

btn8 = Button(frame_botones2, text="Prueba Saber 2026", image=img_btn8, compound="top", command=lambda: abrir_ventana(8, "Prueba Saber 2026"))
btn8.place(x=260, y=70, width=120, height=120)

btn9 = Button(frame_botones2, text="Proyección 2031", image=img_btn9, compound="top", command=lambda: abrir_ventana(9, "Proyección 2031"))
btn9.place(x=400, y=70, width=120, height=120)

btn10 = Button(frame_botones2, text="Libre", image=img_btn10, compound="top", command=lambda: abrir_ventana(10, "Libre"))
btn10.place(x=540, y=70, width=100, height=120)

# -----------------------------
# run
# -----------------------------
ventana_principal.mainloop()
