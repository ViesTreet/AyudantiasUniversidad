from caballo import Caballo
from random import randint
from time import sleep
import os

def limpiar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

sardinilla = Caballo("Sardinilla",randint(50,100),0)
napoleon = Caballo("Napoleon",randint(50,100),0)
argo = Caballo("Argo", randint(50,100),0)
epona = Caballo("Epona",randint(50,100),0)
peste =Caballo("Peste", randint(50,100),0)
caballosObj = [sardinilla,napoleon,argo,epona,peste]
recorrido = []
ganador=[]
comprobacion=True
while comprobacion:
    for y in range(10):
        t=[]
        for cab in caballosObj:
            if cab.posicion == y:
                t.append(cab.nombre[0])
            else:
                t.append("0")
        recorrido.append(t)
    for c in caballosObj:
        if c.posicion == 10:
            comprobacion=False
            ganador.append(c)
        if c.velocidad>=randint(50,90):
            c.posicion +=1
    for r in recorrido:
        print(r)
    sleep(2)
    limpiar()
    recorrido=[]
if len(ganador)==1:
    print("hubo un ganador unanime "+ ganador[0].nombre)
else:
    print("hubo un empate entre:")
    for g in ganador:
        print(g.nombre)

