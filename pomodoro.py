#Importes
from tkinter import * #Interfaz grafica
import time #Tiempo

#Declaro las variables a usar
tiempo_trabajo = 10
tiempo_descanso = 5*60
BCG_COLOR_TRABAJO= "#f26419"
BCG_COLOR_DESCANSO = "#86bbd8"

#Comenzamos con la funcion del contador
def contador(tiempo):
    estado_str.set("TRABAJO")
    cambiar_color_bg(BCG_COLOR_TRABAJO)
    ventana.update_idletasks()
    while tiempo >= 0:
        mins, secs = divmod(tiempo, 60)
        contador = '{:02d}:{:02d}'.format(mins, secs)
        tiempo_str.set(contador)
        ventana.update_idletasks()
        time.sleep(1)
        tiempo -= 1 
        if tiempo <= 0:
            if estado_str.get()== "TRABAJO":
                tiempo = tiempo_descanso
                estado_str.set("DESCANSO")
                cambiar_color_bg(BCG_COLOR_DESCANSO)
                
            else:
                tiempo = tiempo_trabajo
                cambiar_color_bg(BCG_COLOR_TRABAJO)
                estado_str.set("TRABAJO")

#Esta funcion permite cambiar el fondo de la interfaz
def cambiar_color_bg(color):
    ventana.config(bg=color)
    pomodoro_label.config(bg=color, fg='#fff')
    contador_label.config(bg=color, fg='#fff')
    estado_label.config(bg=color, fg='#fff', padx=0, pady=0)

#Tkinter nos permite crear la ventana
ventana = Tk()
ventana.title("Pomodoro")
ventana.config(bg=BCG_COLOR_TRABAJO)
ventana.geometry("500x500")
ventana.resizable(width=False, height=False)

#Titulo en la interfaz diciendo POMODORO
pomodoro_label = Label(ventana, text="POMODORO", font =('Roboto',35,'bold'))
pomodoro_label.config(bg=BCG_COLOR_TRABAJO, fg='#fff')
pomodoro_label.pack(side=TOP, pady=30)

#Contador
tiempo_str = StringVar()
tiempo_str.set("25:00")
contador_label = Label(ventana, font = ('Roboto',70,'bold'), textvariable=tiempo_str)
contador_label.config(bg=BCG_COLOR_TRABAJO, fg='#fff')
contador_label.pack(anchor="center")

#Titulo que cambia entre 'Trabajando' y 'Descansando'
estado_str = StringVar()
estado_str.set("PAUSADO")
estado_label = Label(ventana, textvariable=estado_str, font = 'Roboto 15')
estado_label.config(bg=BCG_COLOR_TRABAJO, fg='#fff', padx=0, pady=0)
estado_label.pack()

#Boton de inicio
start = Button(ventana, text="START", 
        font = ('Roboto',20,'bold'), 
        command = lambda: contador(int(tiempo_trabajo)))
start.config(bg='#f6ae2d', fg='#000', borderwidth=0)
start.pack(side=BOTTOM, pady=50)

ventana.mainloop()
