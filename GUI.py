from tkinter import *
from tkinter import messagebox

import random
import string
import time
contadorShift=True
Shift=0
ContadorTime=0
Intentos=3


Nombre=''
ContraCrudo=''
ContraCryp=''

NombrePrueba=''
ContraPrueba=''
ContraPruebaCrypt=''

Confirmacion=False
LLaveDeAcceso=False


def delete(x):
    x.delete(0, END)
def Encender(x):
    x.config(state=NORMAL)
def Apagar(x):
    x.config(state=DISABLED)
def Info(x):
    messagebox.showinfo(title='Aviso', message=x)


#VENTANAS
window=Tk()
window.geometry('1920x1080')
window.title('Cajero Automatico')
window.config(background='#A9CDD4')


#CAJERO

def Cajero():

    Label(window,text=f"Usuario: {Nombre}-{ContraCryp}",font=('arial', 10, 'bold'),fg='#477A91', bg='#FFFFFF'
                 ,bd=10, relief=SUNKEN).pack()





# INICIO DE SESION


def AbrirInicioDeSesion():
    global Nombre
    global ContraCrudo
    global ContraCryp
    global Cajero


        
    def Tiempo():
        global ContadorTime, Intentos
        for i in range(20,0,-1):
            print(i)
            time.sleep(1)


    def LittleCaesars(PlainText):
        global contadorShift,Shift
#Me aseguro que ContadorShift no cambie para poder hacer la confirmacion
        if contadorShift:
            Shift=random.randint(1,10)
            contadorShift=False
#Tan solo creo todos los caracteres
        Alfabetos=[string.ascii_lowercase,string.ascii_uppercase,string.punctuation, string.digits]
        Abcdario="".join(Alfabetos)
#Cambio el alfabeto con version alterada
        def ShiftAlfa(Alfabeto):
            return Alfabeto[Shift:]+Alfabeto[:Shift]

#Con esta tablita traduzco de un alfabeto a otro
        ShiftAbcdario=tuple(map(ShiftAlfa,Alfabetos))
        ShiftAbcdario2="".join(ShiftAbcdario)


        Tabla=str.maketrans(Abcdario,ShiftAbcdario2)
        CrypText=PlainText.translate(Tabla)
        return(CrypText)


    def Tiempo():
        global ContadorTime, Intentos
        for i in range(20,0,-1):
            print(i)
            time.sleep(1)
            
    def submitNombre():
        global Nombre, NombrePrueba
        

        if Confirmacion:
          
            NombrePrueba=NombreEntry.get()
          
            if NombrePrueba!=Nombre:
                delete(NombreEntry)
                Info('Intente de nuevo')
            else:
                Apagar(EnterNombre)
                Apagar(NombreEntry)
                Encender(EnterContra)
                Encender(ContraEntry)
                
        else:
            Nombre=NombreEntry.get()
            if Nombre=='':
                Info('Por favor entre Nombre')
            else:
                print(Nombre)
                Apagar(EnterNombre)
                Apagar(NombreEntry)
                Encender(ContraEntry)
                Encender(EnterContra)
                
    def submitContra():
        global ContraCrudo, ContraCryp,ContraPruebaCrypt,ContraPrueba, LLaveDeAcceso, Confirmacion, ContadorTime
        if Confirmacion:
            ContraPrueba=ContraEntry.get()
            ContraPruebaCrypt=LittleCaesars(ContraPrueba)
            if ContraPruebaCrypt!=ContraCryp:
                delete(ContraEntry)
                ContadorTime+=1
                if ContadorTime>Intentos-1:
                    Apagar(EnterContra)
                    Apagar(ContraEntry)
                    Info('Espere, se quedo sin intentos')
                    Tiempo()
                    Encender(EnterContra)
                    Encender(ContraEntry)
                    ContadorTime=0                    
                Info(f'Algo salio mal con su contraseña, le quedan {Intentos-ContadorTime} intentos ')
            else:
                Apagar(EnterContra)  
                Apagar(ContraEntry)
                
                Info(f"Login existoso. Bienvenido {Nombre}-{ContraCryp}")
                InicioDeSesion_window.destroy()
                IDS_Button.destroy()
                Bienvenido.destroy()
                Cajero()
              
        else:    
            ContraCrudo=ContraEntry.get()

            if ContraCrudo=='' or ContraCrudo==Nombre or len(ContraCrudo)<10:
                Info("Debe de ser distinta al Nombre de Usuario y tener mas de 10 caracteres")
                delete(ContraEntry)
            else:
                delete(ContraEntry)
                Apagar(EnterContra)
                Apagar(ContraEntry)
                ContraCryp=LittleCaesars(ContraCrudo)
                print(ContraCryp)
                Info("Confirme usuario y contraseña, cierre la ventana y presione el botón de nuevo si desea reiniciar el proceso.")
                Confirmacion=True
                Encender(EnterNombre)
                Encender(NombreEntry)
                delete(NombreEntry)

    



            

             

    
    
    InicioDeSesion_window=Toplevel()
    Apagar(IDS_Button)

    def callback_IDS():
        global Confirmacion,Nombre, ContraCryp
        if messagebox.askokcancel("Cancelar Registro", "Seguro de que quiere cancelar este proceso?"):
            InicioDeSesion_window.destroy()
            Encender(IDS_Button)
            Confirmacion=False
            Nombre=''
            ContraCryp=''

    InicioDeSesion_window.protocol("WM_DELETE_WINDOW", callback_IDS)
    InicioDeSesion_window.geometry('900x900')
    InicioDeSesion_window.title('Inicio de Sesion')
    InicioDeSesion_window.config(background='#A9CDD4')

    NombreEntry=Entry(InicioDeSesion_window,font=('Arial Black',40),bg='#111111',fg='#ffffff', width=10)
    NombreEntry.pack()
    EnterNombre=Button(InicioDeSesion_window, text='Aceptar', command=submitNombre)
    EnterNombre.pack()

    ContraEntry=Entry(InicioDeSesion_window,font=('Arial Black',40),bg='#111111',fg='#ffffff', width=10, show='*')
    ContraEntry.pack()
    EnterContra=Button(InicioDeSesion_window, text='Aceptar', command=submitContra)
    EnterContra.pack()
    Apagar(ContraEntry)
    Apagar(EnterContra)


IDS_Button= Button(window, text='Registrarse para la sesion')
IDS_Button.config(command=AbrirInicioDeSesion,  font=('Arial',20), fg='#477A91'
             ,activebackground='#E1EBF0',activeforeground='#D6AA58')
IDS_Button.place(x=770, y=500)


Bienvenido=Label(window,text='Bienvenido',font=('arial', 40, 'bold'),fg='#477A91', bg='#FFFFFF'
                 ,bd=10, relief=SUNKEN)
Bienvenido.place(x=770, y=250)




window.mainloop()