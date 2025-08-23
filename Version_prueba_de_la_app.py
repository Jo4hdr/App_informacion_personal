from tkinter import *
from tkinter import messagebox

# -----------------------------
# ventana principal de la app
# -----------------------------
ventana_principal = Tk()
ventana_principal.title("App de Johan")
ventana_principal.geometry("650x650")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

# --------------------------------
# frame entrada datos
# --------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=630, height=180)
frame_entrada.place(x=10, y=10)

# Nombre principal
titulo = Label(frame_entrada, text="Johan Stiven Fiallo Aparicio")
titulo.config(bg="white", fg="black", font=("Helvetica", 20, "bold"))
titulo.place(x=230, y=20)

# Colegio
titulo_colegio = Label(frame_entrada, text="Colegio San José de Guanentá")
titulo_colegio.config(bg="white", fg="black", font=("Verdana", 14))
titulo_colegio.place(x=230, y=55)

# Especialidad
titulo_especialidad = Label(frame_entrada, text="Especialidad en Sistemas")
titulo_especialidad.config(bg="white", fg="black", font=("Verdana", 12, "italic"))
titulo_especialidad.place(x=230, y=80)

# Texto invitación
titulo2 = Label(frame_entrada, text="¡Holaa!, te invito a conocer un poco de mí.")
titulo2.config(bg="white", fg="black", font=("Verdana", 11))
titulo2.place(x=230, y=110)

# Cargar foto personal
try:
    logo = PhotoImage(file="img/fotopersonal.png")
    lb_logo = Label(frame_entrada, image=logo, bg="white")
    lb_logo.place(x=40, y=20)
except:
    Label(frame_entrada, text="(Imagen no encontrada)", bg="white", fg="red").place(x=60, y=20)

# --------------------------------
# frame botoncitos 1
# --------------------------------
frame_botones1 = Frame(ventana_principal)
frame_botones1.config(bg="black", width=630, height=180)
frame_botones1.place(x=10, y=200)

# --------------------------------
# frame botoncitos 2
# --------------------------------
frame_botones2 = Frame(ventana_principal)
frame_botones2.config(bg="black", width=630, height=245)
frame_botones2.place(x=10, y=390)

# --------------------------------
# textos de cada ventana
# --------------------------------
informacion = {
    1: "📍 Nací el 6 de mayo de 2010 en San Gil, Santander.",
    2: "🏥 Soy de la EPS Sanitas y gracias a Dios me encuentro muy bien de salud. No sufro de ninguna enfermedad.",
    3: "👨‍👩‍👧‍👦 Actualmente vivo con mi mamá. Los domingos paso tiempo con mi papá. Además, tengo dos hermanos menores por parte de papá.",
    4: "📚 Toda mi vida he estudiado en el Colegio San José de Guanentá. Ha sido una experiencia muy bonita, llena de aprendizajes y recuerdos.",
    5: "🤝 Mi mejor amiga es Danna, ella es mi todo y sin ella no sabría qué hacer. Otra amiga muy especial es Mariana, la conocí en especialidad y se ha vuelto alguien muy importante en mi vida.",
    6: "🎶 Mi gran pasión es la música. Soy parte de la Banda Sinfónica del colegio y toco el clarinete. También me interesa entrar a un grupo de danzas.",
    7: """📅 Mi horario escolar es:\n
    - Lunes: Matemáticas (2h), Filosofía (2h), Educación Física (2h)\n
    - Martes: Estadística (1h), Español (1h), Sociales (1h), Física (1h), Valores (1h), Artística (1h)\n
    - Miércoles: Álgebra (2h), Ciencias Políticas (1h), Química (1h), Religión (1h), Inglés (1h)\n
    - Jueves: Castellano (2h), Especialidad (4h)\n
    - Viernes: Inglés (2h), Física (2h), Química (2h)""",
    8: "📖 Me estoy preparando para la Prueba Saber 2026 estudiando mucho: lectura crítica, matemáticas e inglés (que es lo que más me cuesta).",
    9: "🚀 En el 2031 me veo iniciando o ya terminando mi universidad en música. Después de eso también quiero estudiar Derecho.",
    10: """🎼 Música y Clarinete 🎶\n
- Soy parte de la Banda Sinfónica del Colegio San José de Guanentá.\n
- En San Gil y en Colombia, las bandas sinfónicas son muy importantes para la cultura musical. En muchas ciudades y colegios existen programas para jóvenes músicos.\n
- El clarinete es un instrumento de viento-madera, muy versátil y usado en bandas, orquestas y grupos de cámara.\n
- Me apasiona la música y mi meta es seguir creciendo en este arte."""
}

# --------------------------------
# función genérica para abrir ventanas
# --------------------------------
def abrir_ventana(num, titulo="Ventana", color="lightgray"):
    v = Toplevel()
    v.title(f"{titulo}")
    v.geometry("500x400")
    v.config(bg=color)

    # texto de cada ventana
    texto = informacion.get(num, "Información no disponible.")
    Label(v, text=texto, bg=color, font=("Arial", 12), justify=LEFT, wraplength=450).pack(padx=20, pady=20)

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
btn1.place(x=20, y=20, width=100, height=150)

btn2 = Button(frame_botones1, text="Inf. médica", image=img_btn2, compound="top", command=lambda: abrir_ventana(2, "Inf. médica"))
btn2.place(x=140, y=20, width=100, height=150)

btn3 = Button(frame_botones1, text="Inf. familiar", image=img_btn3, compound="top", command=lambda: abrir_ventana(3, "Inf. familiar"))
btn3.place(x=260, y=20, width=100, height=150)

btn4 = Button(frame_botones1, text="Proceso edu", image=img_btn4, compound="top", command=lambda: abrir_ventana(4, "Proceso educativo"))
btn4.place(x=380, y=20, width=100, height=150)

btn5 = Button(frame_botones1, text="Amigos", image=img_btn5, compound="top", command=lambda: abrir_ventana(5, "Amigos"))
btn5.place(x=500, y=20, width=100, height=150)

# --------------------------------
# Botones en frame 2 con imágenes
# --------------------------------
btn6 = Button(frame_botones2, text="Hobbies", image=img_btn6, compound="top", command=lambda: abrir_ventana(6, "Hobbies"))
btn6.place(x=20, y=60, width=100, height=150)

btn7 = Button(frame_botones2, text="Horario esc.", image=img_btn7, compound="top", command=lambda: abrir_ventana(7, "Horario escolar"))
btn7.place(x=140, y=60, width=100, height=150)

btn8 = Button(frame_botones2, text="Prueba Saber 2026", image=img_btn8, compound="top", command=lambda: abrir_ventana(8, "Prueba Saber 2026"))
btn8.place(x=260, y=60, width=100, height=150)

btn9 = Button(frame_botones2, text="Proyección 2031", image=img_btn9, compound="top", command=lambda: abrir_ventana(9, "Proyección 2031"))
btn9.place(x=380, y=60, width=100, height=150)

btn10 = Button(frame_botones2, text="Artes Musicales", image=img_btn10, compound="top", command=lambda: abrir_ventana(10, "Artes Músicales"))
btn10.place(x=500, y=60, width=100, height=150)

# -----------------------------
# run
# -----------------------------
ventana_principal.mainloop()


