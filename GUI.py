from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
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

## APORTE DE JOSUE: Modo admin. Josue informo de haber tenido un accidente y haber estado hospitalizado 
## la semana que le tocaba entregar su aporte, me envio su codigo por whatsapp y lo pegue en el archivo
## Josue_Aporte.


#Aporte Josue
def administrar_productos(productos):
    global Admin, Admin_Opcion
    def reiniciar():
        global Adcant, Adprecio, Adnombre, Admin_Opcion, cantidad_texto, seleccion
        Encender(SubOpc_Button)
        Encender(opcion_Box)
        Admin.destroy()
        Adcant=0
        Adprecio=0
        Adnombre=''
        Admin_Opcion=''
        cantidad_texto=''
        seleccion=''
        Actualizar()

    Apagar(SubOpc_Button)
    Apagar(opcion_Box)


    Admin=Toplevel()
    def callback_IDS():
        if messagebox.askokcancel('Aviso','Saliendo del modo administrador'):
            reiniciar()
    Admin.protocol("WM_DELETE_WINDOW", callback_IDS)
    Admin_Opcion=''

    Label(Admin,text="ADMINISTRAR PRODUCTOS", bg='black', fg='white').pack()
    Label(Admin, text="1 - Agregar nuevo producto", bg='black', fg='white' ).pack()
    Label(Admin,text= "0 - Modificar cantidad de un producto", bg='black', fg='white').pack()


    def SubmitAdOpc():
        global Admin_Opcion
        Admin_Opcion=AdOpc_Box.get()
        delete(AdOpc_Box)

        if Admin_Opcion == "1":
            

            
            # Ingresar el nombre del nuevo producto.
 # Ingresar un precio positivo.
            def CantidadInicial():
                 global Adcant, Adnombre, Adprecio
    
                
                 
                 cantidad_texto = AdOpc_Box.get()
 
                 if cantidad_texto.isdecimal():
                     Adcant = int(cantidad_texto)
                     productos.append([Adnombre, Adprecio, Adcant])  
                     Info("Producto agregado correctamente.")
                     reiniciar()
                 else:
                     Info("Ingrese una cantidad entera igual o mayor que cero.")
 
           
            def Precio():
                global Adprecio
                precio_texto = AdOpc_Box.get()
                try:
                    Adprecio = float(precio_texto)

                    if 0 < Adprecio < float("inf"):
                        InfoLabel.config(text='Ingrese cantidad del nuevo producto')
                        delete(AdOpc_Box)
                        AdOpc_Button.config(command= CantidadInicial)


                    else:
                        Info("El precio debe ser mayor que cero.")
                except ValueError:
                    Info("Ingrese un precio numerico. Ejemplo: 5.50")

            # Ingresar la cantidad inicial.
            
            def Nombre():
                global Adnombre


                Adnombre = AdOpc_Box.get()

                if Adnombre == "":
                    Info("El nombre no puede estar vacio.")
                
                else:
                    existe = False
                    for producto in productos:
                        if producto[0].lower() == Adnombre.lower():
                            existe = True

                    if existe:
                        Info("Ese producto ya existe.")
                    else:
                        InfoLabel.config(text='Ingrese precio')
                        delete(AdOpc_Box)
                        AdOpc_Button.config(command= Precio)
                        

                    
            InfoLabel.config(text='Ingrese nombre del nuevo producto')
            AdOpc_Button.config(command= Nombre)

        
        elif Admin_Opcion=='0':


            # Modificar exclusivamente la cantidad.
            def ModificarCantidad():
                global posicion

                cantidad_texto = AdOpc_Box.get()

                if cantidad_texto.isdecimal():
                    productos[posicion][2] = int(cantidad_texto)
                    Info("Cantidad actualizada correctamente.")
                    reiniciar()
## ESTO LO HICE YO, ERICK D.S.M, NO ESTABA EN EL CODIGO ORIGINAL DE josue_Aporte
                elif cantidad_texto== 'Delete':


                    answer = messagebox.askyesno(title='confirmation',
                    message='Seguro que quiere eliminar este producto? Acto irreversible.')
                    if answer:
                        productos.remove(productos[posicion])
                        reiniciar()
                    else:
                        delete(AdOpc_Box)
## FIN DE MI APORTE A Josue_Aporte
                else:
                    Info("Ingrese una cantidad entera igual o mayor que cero. Para eliminar escriba -- Delete")

           

            # Seleccionar el producto existente.
            def Seleccionar():
                
                global posicion
                seleccion = AdOpc_Box.get()

                if seleccion.isdecimal():
                    seleccion = int(seleccion)

                    if 1 <= seleccion <= len(productos):
                        posicion = seleccion - 1
                        AdOpc_Button.config(command=ModificarCantidad)
                        delete(AdOpc_Box)
                        InfoLabel.config(text='Ingrese nueva cantidad del producto. Eliminar: Escriba "Delete" ')
                else:
                    Info("Seleccione un numero de producto valido.")


            InfoLabel.config(text='Seleccione Producto a modificar')
            AdOpc_Button.config(command= Seleccionar)
           
        else:
            Info('opcion incorrecta')
            InfoLabel.config(text='Incorrecto, Ingrese 0 o 1')




    for i in range(len(productos)):
        Label(Admin, text=(i + 1, "-", productos[i][0],
                    "Precio: Q", productos[i][1],
                    "Disponibles:", productos[i][2])).pack()
    AdOpc_Box= Entry(Admin)
    AdOpc_Box.pack()

    InfoLabel=Label(Admin, text='Ingrese 0 o 1')
    InfoLabel.pack()

    AdOpc_Button= Button(Admin, text= 'Enter', command= SubmitAdOpc)
    AdOpc_Button.pack()






#CAJERO

productos = [
    ["Zanahoria", 5, 20],
    ["Tomate", 10, 20],
    ["Papa", 8, 15],
    ["Cebolla", 6, 15],
    ["Lechuga", 4, 10]
]

factura = []
continuar = True
Inventario= Frame(window, bd=10, background="#e8b94c", relief=SUNKEN)

def Actualizar():
    # Source - https://stackoverflow.com/a/28623781
# Posted by Tom.Slick, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-21, License - CC BY-SA 4.0
    for widget in Inventario.winfo_children():
        widget.destroy()

    for i in range(len(productos)):
        Label(Inventario, text=(i + 1, "-", productos[i][0],
                "Precio: Q", productos[i][1],
                "Disponibles:", productos[i][2])).pack()
    Label(Inventario, text="0 - Terminar compra").pack()


def cero_factura ():
    global Factura_window, subtotal
    subtotal=0

    
    

    if len(factura) == 0:
        administrar_productos(productos)
        Info("No se compraron productos, entrando a modo administrador")  
    else:
        Apagar(SubOpc_Button)
        Apagar(opcion_Box)
        Factura_window=Toplevel()
        def callback_IDS():
            global Confirmacion,Nombre, ContraCryp
            if messagebox.askokcancel("Destruir Factura", "Este proceso no puede ser revertido, guarde su factura"):
                    Factura_window.destroy()
                    for producto in factura:
                        factura.remove(producto)
                    Encender(SubOpc_Button)
                    Encender(opcion_Box)
        Factura_window.protocol("WM_DELETE_WINDOW", callback_IDS)
        
                
        Label(Factura_window, text= "FACTURA").pack()
        
        Label(Factura_window, text= "Producto | Cantidad | Precio | Total").pack()

        for producto in factura:
            nombre = producto[0]
            precio = producto[1]
            cantidad = producto[2]

            total = precio * cantidad
            subtotal += total

            Label(Factura_window, text= f'{nombre} | {cantidad} | Q.{precio} | Q.{total}').pack()

        
        Label(Factura_window, text=f"SUBTOTAL: Q.{ subtotal}").pack()

        Label(Factura_window, text="Gracias por su compra.").pack()
       

    def Guardar_Factura():
        global Factura_Archivo
        Factura_Archivo= filedialog.asksaveasfile(defaultextension='.txt')

        if Factura_Archivo is None:
            return
        for i in factura: 
            Factura_Archivo.write('  PRODUCTO, PRECIO, CANTIDAD:  ')
            Factura_Archivo.write(str(i))
            Factura_Archivo.write(' ---- ')
            Factura_Archivo.write(' TOTAL:  ')
            Factura_Archivo.write( str(total))
            Factura_Archivo.write(' ---- ')
        Factura_Archivo.write('  >>>>   SUBTOTAL: ')
        Factura_Archivo.write(str(subtotal))
        Factura_Archivo.close()

    Save= Button(Factura_window, text='GUARDAR FACTURA')
    Save.config(command=Guardar_Factura,  font=('Arial',20), fg='#477A91'
             ,activebackground='#E1EBF0',activeforeground='#D6AA58')
    Save.pack()


def cantidad_submit():
     global opcion,productos,nombre,precio, posicion,disponible

     
     cantidad_texto = cantidad_Box.get()

     if cantidad_texto.isdigit():
        cantidad = int(cantidad_texto)
    
        if cantidad > 0 and cantidad <= disponible:
            factura.append([nombre, precio, cantidad])
            productos[posicion][2] -= cantidad
    
            Info("Producto agregado correctamente.")
            Encender(opcion_Box)
            Encender(SubOpc_Button)
            Apagar(cantidad_Box)
            Apagar(Cantidad_Button)
            Actualizar()
            
        else:
            Info("Cantidad incorrecta o insuficiente.")
     else:
        Info("Ingrese una cantidad numerica.")  

def opcion_submit():
    global opcion,productos,nombre,precio, posicion,disponible
    opcion = opcion_Box.get()


    if opcion.isdigit():
        opcion = int(opcion)

        if opcion == 0:
            cero_factura()

        elif opcion >= 1 and opcion <= len(productos):
            posicion = opcion - 1

            nombre = productos[posicion][0]
            precio = productos[posicion][1]
            disponible = productos[posicion][2]

            if disponible > 0:
                Apagar(opcion_Box)
                Apagar(SubOpc_Button)
                Encender(cantidad_Box)
                Encender(Cantidad_Button)
                
            else:
                Info("Producto agotado.")

        else:
            Info("Opcion incorrecta.")
    else:
        Info("Debe ingresar un numero.")

def Cajero():

    Label(window,text=f"Usuario: {Nombre}-{ContraCryp}",font=('arial', 10, 'bold'),fg='#477A91', bg='#FFFFFF'
                 ,bd=10, relief=SUNKEN).pack()

    Label(window, text="Ingrese código de producto").pack()
    opcion_Box.pack()
    SubOpc_Button.pack()
    Label(window, text="Ingresar cantidad").pack()
    cantidad_Box.pack()
    Cantidad_Button.pack()
    Apagar(Cantidad_Button)
    Apagar(cantidad_Box)
    Label(window, text="CAJERO").pack()
    Label(window,text="PRODUCTOS DISPONIBLES").pack()
    Inventario.pack()
    Actualizar()


SubOpc_Button= Button(window, text='Enter')
SubOpc_Button.config(command=opcion_submit,  font=('Arial',10), fg='#477A91')
opcion_Box=Entry(window,font=('Arial Black',40),bg='#111111',fg='#ffffff', width=10)

cantidad_Box=Entry(window, font=('Arial', 40),bg='#111111',fg='#ffffff', width=10 )
Cantidad_Button= Button(window, text='Enter')
Cantidad_Button.config(command=cantidad_submit,  font=('Arial',10), fg='#477A91')



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

    Label(InicioDeSesion_window, text="Nombre de Usuario").pack()

    NombreEntry=Entry(InicioDeSesion_window,font=('Arial Black',40),bg='#111111',fg='#ffffff', width=10)
    NombreEntry.pack()
    EnterNombre=Button(InicioDeSesion_window, text='Aceptar', command=submitNombre)
    EnterNombre.pack()

    Label(InicioDeSesion_window, text="Contraseña").pack()

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