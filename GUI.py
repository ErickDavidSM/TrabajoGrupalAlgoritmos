from tkinter import *
#VENTANA PRINCIPAL
window=Tk()
window.geometry('1920x1080')
window.title('Cajero Automatico')
window.config(background='#A9CDD4')
Bienvenido=Label(window,text='Bienvenido',font=('arial', 40, 'bold'),fg='#477A91', bg='#FFFFFF'
                 ,bd=10, relief=SUNKEN)

#FUNCIONES BASICAS
def disable(x):
    x.config(state=DISABLED)
def enable(x):
    x.config(state=NORMAL)
def exit(x):
    x.destroy()


#BOTON PARA INICIO DE SESION
def AbrirInicioDeSesion():
    InicioDeSesion_window=Toplevel()
    Login.config(state=DISABLED)
    InicioDeSesion_window.geometry('900x900')
    InicioDeSesion_window.title('Inicio de Sesion')
    InicioDeSesion_window.config(background='#A9CDD4')

Login= Button(window, text='Registrarse para la sesion')
Login.config(command=AbrirInicioDeSesion,  font=('Arial',20), fg='#477A91'
             ,activebackground='#E1EBF0',activeforeground='#D6AA58')
Login.place(x=770, y=500)





Bienvenido.place(x=770, y=100)
window.mainloop()