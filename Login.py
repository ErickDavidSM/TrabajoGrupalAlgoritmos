import random
import string
import os
import time
contadorShift=True
Shift=0
ContadorTime=0
def LittleCaesars(PlainText):
    global contadorShift,Shift

    if contadorShift:
        Shift=random.randint(1,10)
        contadorShift=False

    Alfabetos=[string.ascii_lowercase,string.ascii_uppercase,string.punctuation, string.digits]
    Abcdario="".join(Alfabetos)

    def ShiftAlfa(Alfabeto):
        return Alfabeto[Shift:]+Alfabeto[:Shift]


    ShiftAbcdario=tuple(map(ShiftAlfa,Alfabetos))
    ShiftAbcdario2="".join(ShiftAbcdario)


    Tabla=str.maketrans(Abcdario,ShiftAbcdario2)
    CrypText=PlainText.translate(Tabla)
    return(CrypText)


Nombre=input("Entre su nombre de usuario para la sesion>>>  ")
while Nombre=='':
    Nombre=input("Entre un nombre valido>>>  ")


ContraCrudo=input("Cree una contraseña para la sesion>>>  ")
while ContraCrudo=='' or ContraCrudo==Nombre or len(ContraCrudo)<10:
    print("Debe de ser distinta al Nombre de Usuario y tener mas de 10 caracteres")
    ContraCrudo=input("Entre una contraseña valida>>>  ")
ContraCryp=LittleCaesars(ContraCrudo)

os.system('clear')

NombrePrueba=input('Confirme usuario>>>  ')
ContraPrueba=input("Confirme su contraseña>>>  ") 
ContraPruebaCrypt=LittleCaesars(ContraPrueba)

while(NombrePrueba!=Nombre or ContraPruebaCrypt!=ContraCryp):
    ContadorTime+=1
    if ContadorTime>10:
        print('Espere, se quedo sin intentos...')
        for i in range(20,0,-1):
            print(i)
            time.sleep(1)
        ContadorTime=0

    print(f'Algo salio mal con su usuario o contraseña, le quedan {10-ContadorTime} intentos ')
    NombrePrueba=input('Confirme usuario de nuevo>>>  ')
    ContraPrueba=input("Confirme su contraseña de nuevo>>> ") 
    ContraPruebaCrypt=LittleCaesars(ContraPrueba)


os.system('clear')

print(f"Login existoso. Bienvenido {Nombre}-{ContraCryp}")